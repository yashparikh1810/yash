# Chatbot using Gemini on Streamlit

import os
import streamlit as st
import google.generativeai as palm



GOOGLE_API_KEY = "AIzaSyBT9gOzUp3gfJnTZHZkAtPYMeVt9qAP7ow"

if not GOOGLE_API_KEY:
    st.error("API key not found. Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

palm.configure(api_key=GOOGLE_API_KEY)

model = palm.GenerativeModel(model_name="gemini-pro")

def get_gemini_response(prompt):
    try:
        response = st.session_state["chat"].send_message(prompt, stream=False)
        if response and response.candidates: 
            first_candidate = response.candidates[0]
            if first_candidate.content and first_candidate.content.parts:
                text_parts = [part.text for part in first_candidate.content.parts if hasattr(part, 'text')]
                return "".join(text_parts) 
            else:
                st.error("Response content or parts are missing.")
                return None
        else:
            st.error("No candidates found in the response.")
            return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
