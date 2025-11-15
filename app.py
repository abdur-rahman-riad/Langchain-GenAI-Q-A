import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key from Streamlit Secrets
key = st.secrets["API_KEY"]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=key,
    temperature=0,
)

st.title("🇧🇩 Bangladesh Q&A Chatbot")
st.write("Ask anything about Bangladesh. Answer to-the-point.")

# --- SESSION STATES ---
if "question" not in st.session_state:
    st.session_state["question"] = ""

if "response" not in st.session_state:
    st.session_state["response"] = ""

# --- INPUT FIELD ---
user_input = st.text_input("Your Question:", value=st.session_state["question"], key="question_input")

col1, col2 = st.columns(2)

# --- SUBMIT BUTTON ---
with col1:
    if st.button("Submit"):
        if user_input.strip():
            st.session_state["question"] = user_input

            with st.spinner("⏳ Generating answer..."):
                messages = [
                    ("system", "You are a helpful assistant that knows about Bangladesh. Answer to-the-point."),
                    ("human", user_input),
                ]
                ai_msg = llm.invoke(messages)
                st.session_state["response"] = ai_msg.content

# --- CLEAR BUTTON ---
with col2:
    if st.button("Clear"):
        st.session_state["question"] = ""
        st.session_state["response"] = ""
        st.session_state["question_input"] = ""   # Clears input field

# --- OUTPUT SECTION ---
st.subheader("Answer:")
st.write(st.session_state["response"])
