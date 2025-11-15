import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

key = st.secrets["API_KEY"]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=key,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

st.title("🇧🇩 Bangladesh Q&A Chatbot")
st.write("Ask anything about Bangladesh. Answer to-the-point.")

user_input = st.text_input("Your Question:")

col1, col2 = st.columns(2)

if "response" not in st.session_state:
    st.session_state["response"] = ""

with col1:
    if st.button("Submit"):
        if user_input.strip():
            messages = [
                ("system", "You are a helpful assistant that knows about Bangladesh."),
                ("human", user_input),
            ]
            ai_msg = llm.invoke(messages)
            st.session_state["response"] = ai_msg.content

with col2:
    if st.button("Clear"):
        st.session_state["response"] = ""

st.subheader("Answer:")
st.write(st.session_state["response"])