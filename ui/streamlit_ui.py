import streamlit as st
from typing import Optional

class StreamlitUI:
    def __init__(self):
        self.configure_page()
        self.setup_sidebar()
        self.setup_header()

    def configure_page(self):
        st.set_page_config(page_title="Dickhead Ai")

    def setup_sidebar(self):
        with st.sidebar:
            self.api_key = st.text_input("Anthropic API Key", key="chatbot_api_key", type="password")
            "[Get an Anthropic API key](https://console.anthropic.com/)"
            "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
            "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

    def setup_header(self):
        col1, col2 = st.columns([0.2, 0.8])
        with col1:
            st.image("Dickheadai.png", width=100)
        with col2:
            st.title("Dickhead Ai")
            st.caption("Chat with a dickhead today.")

    def get_avatar(self, role: str) -> Optional[str]:
        if role == "assistant":
            return "DickheadAi.png"
        return None

    def display_messages(self, messages: list):
        for msg in messages:
            st.chat_message(msg["role"], avatar=self.get_avatar(msg["role"])).write(msg["content"])

    def get_user_input(self) -> Optional[str]:
        return st.chat_input()

    def show_api_key_notice(self):
        st.info("Please add your Anthropic API key to continue.")

    def get_api_key(self) -> Optional[str]:
        return self.api_key 
