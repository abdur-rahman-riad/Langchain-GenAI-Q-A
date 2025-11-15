import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# API KEY from Streamlit Secrets
key = st.secrets["API_KEY"]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=key,
    temperature=0,
)

st.title("🇧🇩 Bangladesh Q&A Chatbot")
st.write("Ask anything about Bangladesh. Answer to-the-point.")

# Session State (for question + answer)
if "question" not in st.session_state:
    st.session_state["question"] = ""

if "response" not in st.session_state:
    st.session_state["response"] = ""

# Input Box
user_input = st.text_input("Your Question:", value=st.session_state["question"])

col1, col2 = st.columns(2)

# --- Submit Button ---
with col1:
    if st.button("Submit"):
        if user_input.strip():
            st.session_state["question"] = user_input
            
            # Loading spinner
            with st.spinner("⏳ Thinking…"):
                messages = [
                    ("system", "You are a helpful assistant that knows about Bangladesh. Answer to-the-point."),
                    ("human", user_input),
                ]
                ai_msg = llm.invoke(messages)
                st.session_state["response"] = ai_msg.content

            st.experimental_rerun()

# --- Clear Button ---
with col2:
    if st.button("Clear"):
        st.session_state["question"] = ""
        st.session_state["response"] = ""
        st.experimental_rerun()

# --- Output Section ---
st.subheader("Answer:")
st.write(st.session_state["response"])
