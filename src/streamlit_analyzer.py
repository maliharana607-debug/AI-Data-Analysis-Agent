import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

# Page Configuration
st.set_page_config(
    page_title="AI Data Analysis Agent",
    page_icon="📊",
    layout="centered"
)

st.title("📊 AI Data Analysis Agent")
st.markdown(
    "Upload your CSV dataset and let AI generate insights, statistics, and visualizations automatically."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "data" not in st.session_state:
    st.session_state.data = None

uploaded_file = st.file_uploader("📂 Upload Your Dataset (CSV)", type=['csv'])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.session_state.data = data
    st.success("✅ Dataset uploaded successfully!")
    st.dataframe(data.head())

if st.session_state.data is not None:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("💬 Ask any question about your data..."):
        with st.chat_message("user"):
            st.write(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        data_text = st.session_state.data.head(10).to_string()

        resp = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=500,
            system=f"Analyze this data:\n{data_text}",
            messages=st.session_state.messages
        )

        answer = resp.content[0].text

        with st.chat_message("assistant"):
            st.write(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})