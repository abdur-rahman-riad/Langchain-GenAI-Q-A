import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API Key
key = st.secrets["API_KEY"]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=key,
    temperature=0,
)

st.title("🇧🇩 Bangladesh Q&A Chatbot")
st.write("Ask anything about Bangladesh. Answer to-the-point.")

# ---- Session State ----
if "question" not in st.session_state:
    st.session_state["question"] = ""

if "response" not in st.session_state:
    st.session_state["response"] = ""

if "clear_flag" not in st.session_state:
    st.session_state["clear_flag"] = False

# ---- Clear input UI trick ----
def get_default_input():
    """Return empty string only after clear is pressed."""
    if st.session_state.clear_flag:
        return ""
    return st.session_state.question

# ---- Input field (no widget key needed) ----
user_input = st.text_input("Your Question:", value=get_default_input())

col1, col2 = st.columns(2)

# ---- Submit Button ----
with col1:
    if st.button("Submit"):
        if user_input.strip():
            st.session_state.question = user_input

            with st.spinner("⏳ Generating answer..."):
                messages = [
                    ("system", "You are a helpful assistant that knows about Bangladesh. Answer to-the-point."),
                    ("human", user_input),
                ]
                ai_msg = llm.invoke(messages)

            st.session_state.response = ai_msg.content
            st.session_state.clear_flag = False  # reset clear flag

# ---- Clear Button ----
with col2:
    if st.button("Clear"):
        st.session_state.question = ""
        st.session_state.response = ""
        st.session_state.clear_flag = True

# ---- Output ----
st.subheader("Answer:")
st.write(st.session_state.response)
