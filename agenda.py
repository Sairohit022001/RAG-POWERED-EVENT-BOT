
import streamlit as st

def show_agenda():
    

    agenda = {
       "10:00 - 11:00 AM": "Hands On Workshop: Automation using Claude and MCP Server - Vijender P, Alumnx",
       "11:00 - 12:00 PM": "Hands On Workshop: Agentic AI - Jitendra Gupta (Google Developer Expert)",
       "12:00 - 1:00 PM": "Industry Connect Session - Ravi Babu, Apex Cura Healthcare",
       "1:00 - 2:00 PM": "Lunch",
       "2:00 - 3:00 PM": "Hands On Workshop: Build an Event Bot using RAG - Vishvas Dubey, TCS",
       "3:00 - 3:30 PM": "Industry Application of AI: Building Multi AI Agents - Surendranath Reddy, QAPilot",
       "3:30 - 4:00 PM": "Workshop: Building Multi AI Agents - Mahidhar, NexusHub"
    }

    st.header(" Meeting Agenda")
    for time, event in agenda.items():
        st.markdown(f"**{time}**: {event}")
