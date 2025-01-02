import streamlit as st
from agents.Dickheadai import Dickhead Ai
from ui.streamlit_ui import StreamlitUI

class ChatApp:
    def __init__(self):
        self.ui = StreamlitUI()
        self.initialize_session_state()
        
    def initialize_session_state(self):
        api_key = self.ui.get_api_key()
        
        if "einstein_agent" not in st.session_state and api_key:
            st.session_state.Dickheadai = DickheadAi(api_key)
            
        if "messages" not in st.session_state:
            st.session_state["messages"] = [
                st.session_state.einstein_agent.get_initial_message() if api_key else 
                {"role": "assistant", "content": "Please add your Anthropic API key to continue."}
            ]

    def run(self):
        api_key = self.ui.get_api_key()
        
        # Display existing messages
        self.ui.display_messages(st.session_state.messages)
        
        # Handle new user input
        if prompt := self.ui.get_user_input():
            if not api_key:
                self.ui.show_api_key_notice()
                return
                
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            self.ui.display_messages([st.session_state.messages[-1]])
            
            # Get and display AI response
            msg = st.session_state.einstein_agent.get_response(st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": msg})
            self.ui.display_messages([st.session_state.messages[-1]])

if __name__ == "__main__":
    app = ChatApp()
    app.run()
