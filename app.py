import streamlit as st
from agenda import show_agenda
from matching import show_matching
from directions import show_directions
from recommendations import show_recommendations
from lunch_timer import show_lunch_timer
from feedback import show_feedback
from rag_agent import show_rag_interface 

# Page config
st.set_page_config(page_title="Event Bot", page_icon="⚙︎")

# Sidebar Navigation
option = st.sidebar.selectbox("Choose an option", [
    "Agenda",
    "Matching",
    "Recommendations",
    "Directions",
    "Lunch Timer",
    "Event Feedback",
    "Event Assistant"
])

# Only show welcome message on Agenda page
if option == "Agenda":
    st.title("⚙︎ WELCOME TO RAG POWERED EVENT ASSISTANT")
    st.markdown("""
    This is your **Build with AI Workshop Event Bot** — Your Smart Assistant for Event Info, Schedule & Updates  
    1. ✅ Agenda Details  
    2. 👥 Participant Matching Engine (Resume-Based)  
    3. 📌 Session recommendations  
    4. 🗺 Washroom directions  
    5. ⏱ Real-time lunch countdown  
    6. 📝 Session Feedback (Conversational)  
    7. 🤖 Event Assistant (Chat with your Event)
    """)
    show_agenda()

elif option == "Matching":
    show_matching()
elif option == "Recommendations":
    show_recommendations()
elif option == "Directions":
    show_directions()
elif option == "Lunch Timer":
    show_lunch_timer()
elif option == "Event Feedback":
    show_feedback()
elif option == "Event Assistant":
    show_rag_interface()
