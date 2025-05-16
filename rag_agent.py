

import streamlit as st
import pdfplumber
from sentence_transformers import SentenceTransformer
import faiss
from transformers import pipeline

import numpy as np


embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
generator = pipeline('text2text-generation', model='t5-small')  

embedding_dim = 384 
index = faiss.IndexFlatL2(embedding_dim)
documents = []  

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def chunk_text(text, max_length=500):
    sentences = text.split('. ')
    chunks = []
    chunk = ""
    for sent in sentences:
        if len(chunk) + len(sent) < max_length:
            chunk += sent + '. '
        else:
            chunks.append(chunk.strip())
            chunk = sent + '. '
    if chunk:
        chunks.append(chunk.strip())
    return chunks

def add_document(file):
    text = extract_text_from_pdf(file)
    chunks = chunk_text(text)
    embeddings = embedding_model.encode(chunks)
    for emb, chunk in zip(embeddings, chunks):
        index.add(np.array([emb]))
        documents.append(chunk)

def retrieve(query, top_k=3):
    query_emb = embedding_model.encode([query])
    D, I = index.search(np.array(query_emb), top_k)
    results = [documents[i] for i in I[0] if i < len(documents)]
    return results

def generate_answer(retrieved_chunks, query):
    context = " ".join(retrieved_chunks)
    input_text = f"summarize: {context} question: {query}"
    output = generator(input_text, max_length=150)[0]['generated_text']
    return output

def show_rag_interface():
    st.sidebar.header("📚 RAG Powered Event Assistant")

    uploaded_file = st.file_uploader("Upload", type=['pdf'])
    if uploaded_file is not None:
        add_document(uploaded_file)
        st.success("Document uploaded and indexed!")

    query = st.text_input("Ask anything:")

    if st.button("Get Answer") and query:
        if len(documents) == 0:
            st.warning("Please upload notes first!")
        else:
            retrieved = retrieve(query)
            answer = generate_answer(retrieved, query)
            st.markdown("**Answer:**")
            st.write(answer)
