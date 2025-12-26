import streamlit as st
import streamlit.components.v1 as components
import os
import base64

# Page Config
st.set_page_config(
    page_title="PokeConsult",
    page_icon="logo_final.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Function to read file as base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Read index.html content
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Inject Base64 Logo into HTML
# This replaces the relative "./logo_final.png" path with the embedded Base64 data
# enabling the single-file HTML to work perfectly inside the Streamlit iframe.
try:
    logo_b64 = get_base64_of_bin_file('logo_final.png')
    html_content = html_content.replace('./logo_final.png', f"data:image/png;base64,{logo_b64}")
except Exception as e:
    print(f"Warning: Could not embed logo: {e}")

# Render the HTML
components.html(html_content, height=1000, scrolling=True)

# Hide Streamlit elements to maximize immersion
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
            }
            iframe {
                height: 100vh !important;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
