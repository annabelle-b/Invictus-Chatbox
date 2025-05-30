import streamlit as st
import time

# Predefined QnA 
questions = {
    "What types of cases do you handle?": "We handle criminal defense, appeals and pro bono cases for vulnerable communities.",
    "How can I book a consultation?": "You can call us at +65-1234-5678 or email us at info@invictuslaw.sg to schedule a consultation.",
    "Do you take pro bono cases?": "Yes, we believe everyone deserves a defense. Please fill out our intake form and we'll review your request."
}

st.title("Let us help you")

# Dynamic output area 
output_box = st.empty()

# Question buttons 
for question, answer in questions.items():
    if st.button(question):
        typed_text = ""
        output_box.text(typed_text)
        for char in answer:
            typed_text += char
            output_box.text(typed_text)
            time.sleep(0.04)  # WPM












