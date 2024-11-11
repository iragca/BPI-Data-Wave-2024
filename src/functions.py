def display_chat_history(response_metadata=False, message_age=False):
    for chat in st.session_state['OpenAI_history']:

        ## User profile image and name
        st.html(f"""
        <div STYLE="text-align: right;">
            <small style="opacity: 0.5;">
                User
            </small>
            <img src="./app/static/images/chatbot/user.png" alt="Placeholder Image" style="padding: 10px; border-radius: 20px;">
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
        <img src="./app/static/images/chatbot/openai.webp" alt="Placeholder Image" style="padding: 5px; border-radius: 10px; background-color: rgb(255, 255, 255, 0.90); max-height: 32px; max-width: 100%; height: auto; width: auto;">
        <small style="opacity: 0.5; padding: 10px;">"""
            +f"OpenAI"
        """</small>
        """)


        ## Token Summary
        if response_metadata:
            st.html(f"""
            <small style="opacity: 0.5;">"""
                +f"Model: {model} <br>Prompt Tokens: {prompt_tokens} | Completion Tokens: {completion_tokens} | Total Tokens: {total_tokens} <br>Processing Time (seconds): {process_time:.2f}"
            """</small>
            """)

        ## LLM Response
        st.markdown(f"{chat[2].content}")