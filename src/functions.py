import json
import streamlit as st
import re

def display_chat_history(history):
    for chat in history:

        ## User profile image and name
        st.html(f"""
        <div STYLE="text-align: right;">
            <small style="opacity: 0.5;">
                User
            </small>
            <img src="./app/static/images/chatbot/user.png" alt="User Image" style="padding: 10px; border-radius: 20px;">
        </div>
        """)

        ## User prompt
        st.html("""
        <div style="text-align: right; overflow-wrap: break-word;">
            <div style="text-align: left; background-color: rgb(213, 84, 127, 0.25); display: inline-block; padding-top: 10px; padding-bottom: 10px; padding-right: 15px; padding-left: 15px; border-radius: 20px; overflow-wrap: break-word;">"""
                +f"{chat[0]}"+
            """</div>
        </div>
        """)

        ## LLM profile image and name
        st.html(f"""
        <img src="./app/static/images/chatbot/openai.webp" alt="Chatbot Image" style="padding: 5px; border-radius: 10px; background-color: rgb(255, 255, 255, 0.90); max-height: 32px; max-width: 100%; height: auto; width: auto;">
        <small style="opacity: 0.5; padding: 10px;">"""
            +f"OpenAI"
        """</small>
        """)


        # ## Token Summary
        # if response_metadata:
        #     st.html(f"""
        #     <small style="opacity: 0.5;">
        #         # +f"Model: {model} <br>Prompt Tokens: {prompt_tokens} | Completion Tokens: {completion_tokens} | Total Tokens: {total_tokens} <br>Processing Time (seconds): {process_time:.2f}"
        #     </small>
        #     """)

        ## LLM Response
        st.markdown(f"{chat[1]}")

def parse_json(file_path):

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    def parse_list(tup):
        return (tup[0][7:], tup[1][4:])

    return list(map(lambda x: parse_list(x), data))

def parse_memory(memory):
    pattern = r'(Human:.*?)(?=\nAI:|$)\n(AI:.*?)(?=\nHuman:|$)'
    return re.findall(pattern, memory)