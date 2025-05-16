import streamlit as st

def show_recommendations():
    st.header("📌 Session Recommendations")
    st.write("Based on your interests, here are some sessions we think you’ll love:")
    recommendations = [
        "🤖 Hands On Workshop: Automation using Claude and MCP Server",
        "🧠 Agentic AI - Jitendra Gupta (Google Developer Expert)",
        "🤝 Industry Application of AI: Building Multi AI Agents - Surendranath Reddy",
        "💡 Workshop: Building Multi AI Agents - Mahidhar, NexusHub"
    ]
    for session in recommendations:
        st.markdown(f"- {session}")
