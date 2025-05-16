import streamlit as st
import time
from datetime import datetime, timedelta


def show_lunch_timer():
    st.header("⏱️ Real-time Lunch Countdown")

    lunch_end_time = datetime(year=2025, month=5, day=18, hour=13, minute=0, second=0)
  
    
    if datetime.now() > lunch_end_time:
        st.success("🍽️ Lunch time is over!")
        return
    
    placeholder = st.empty()

    while True:
        now = datetime.now()
        remaining = lunch_end_time - now

        if remaining.total_seconds() <= 0:
            placeholder.success("🍽️ Lunch time is over!")
            break

        mins, secs = divmod(int(remaining.total_seconds()), 60)
        placeholder.markdown(f"Time remaining for lunch: **{mins} minutes {secs} seconds**")
        
        time.sleep(1)
