import streamlit as st
import random

st.set_page_config(page_title="Quote Generator", layout="centered")

st.title("✨ Random Quote Generator")
st.write("Click the button to get a new inspirational quote!")

quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Dream big and dare to fail. – Norman Vaughan",
    "Do one thing every day that scares you. – Eleanor Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "Stay hungry. Stay foolish. – Steve Jobs"
]

if st.button("🔄 Get a Quote"):
    st.success(random.choice(quotes))

st.markdown("---")
