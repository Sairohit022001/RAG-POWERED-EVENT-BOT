
import streamlit as st
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

if "resumes" not in st.session_state:
    st.session_state.resumes = {}

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def show_matching():
    
    if "resumes" not in st.session_state:
    st.session_state.resumes = {}
    st.sidebar.header("👥 Participant Matching Engine (Resume-Based)")

    uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        user_id = f"user_{len(st.session_state.resumes)+1}"
        st.session_state.resumes[user_id] = resume_text
        st.success("Resume uploaded and processed!")

        st.subheader("Your Resume Preview")
        st.text_area("Resume Content", resume_text, height=200)

    if len(st.session_state.resumes) > 1:
        st.subheader("Matching Participants")
        texts = list(st.session_state.resumes.values())
        user_ids = list(st.session_state.resumes.keys())

        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform(texts)

        similarity_matrix = cosine_similarity(tfidf_matrix)

        for idx, user_id in enumerate(user_ids):
            st.write(f"Matches for **{user_id}**:")
            sim_scores = similarity_matrix[idx]
            sim_scores[idx] = -1
            top_matches = sim_scores.argsort()[-2:][::-1]

            for match_idx in top_matches:
                st.write(f"- {user_ids[match_idx]} (Similarity: {sim_scores[match_idx]:.2f})")
            st.write("---")
    else:
        st.info("Upload at least 2 resumes to see matching results.")
