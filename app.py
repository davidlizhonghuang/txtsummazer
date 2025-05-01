import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
api_key='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'
#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key)

st.set_page_config(page_title="AI Email Assistant", layout="centered")
st.title("AI Email Summarizer")

email_text = st.text_area("Paste your email here:", height=300)

if st.button("Summarize"):
    if not email_text.strip():
        st.warning("Please enter some email content.")
    else:
        with st.spinner("Summarizing..."):
            response = client.chat.completions.create(model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You summarize emails."},
                {"role": "user", "content": f"Summarize this email:\n\n{email_text}"}
            ])
            summary = response.choices[0].message.content
            st.success("Summary:")
            st.write(summary)
