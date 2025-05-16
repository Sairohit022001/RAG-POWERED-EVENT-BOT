
import streamlit as st

feedback_list = []

def show_feedback():
    st.header("📝 Session Feedback")

    name = st.text_input("Your Name")
    session = st.selectbox("Session", ["Workshop 1", "Workshop 2", "Industry Talk", "Lunch"])
    rating = st.slider("Rate this session (1-5)", 1, 5, 3)
    comments = st.text_area("Additional Comments")

    if st.button("Submit Feedback"):
        if not name or not comments:
            st.warning("Please fill in your name and comments.")
        else:
            feedback = {
                "name": name,
                "session": session,
                "rating": rating,
                "comments": comments,
            }
            feedback_list.append(feedback)
            st.success("Thank you for your feedback!")

    if feedback_list:
        st.subheader("Previous Feedback")
        for fb in feedback_list:
            st.markdown(f"**{fb['name']}** on *{fb['session']}* rated: {fb['rating']}/5")
            st.write(fb['comments'])
            st.write("---")
