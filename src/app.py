import streamlit as st
from functions import *
from dotenv import load_dotenv; load_dotenv()
import os


from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import (ConversationBufferMemory, 
                                                  ConversationSummaryMemory)


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)




user_query = st.chat_input(f"Ask FiLEMon")

if user_query != None:
    response = chain.invoke(
    user_query,
    config={"configurable": {"session_id": "1"}},
    )  # session_id determines thread
    # response = 'Hello! How may I help you?'

display_chat_history(parse_json('responses.json'))

