
import streamlit as st

def show_directions():
    st.header("🗺 Washroom Directions")

    st.markdown("""
     **Venue Layout**:
    -  Ground Floor:
        - 🚻 Washroom near Registration Desk
        - 🚺 Women’s Washroom next to Conference Room A
    -  First Floor:
        - 🚻 Common Washroom near Workshop Hall
        - ♿ Accessible Washroom at the stairway entrance

    🔄 Ask any volunteer if you feel lost – they’re happy to guide you!
    """)
