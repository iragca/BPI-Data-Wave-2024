import streamlit as st

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


store = {}  # memory is maintained outside the chain

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
user_query = st.chat_input(f"Ask FiLEMon")

chain = RunnableWithMessageHistory(llm, get_session_history)

if user_query != None:
    response = chain.invoke(
    user_query,
    config={"configurable": {"session_id": "1"}},
)  # session_id determines thread

