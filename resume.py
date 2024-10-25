import streamlit as st
from pathlib import Path

# Styles for professional look
def set_style():
    st.markdown("""
    <style>
        .centered-content {
            text-align: center;
            font-family: 'Arial', sans-serif;
            color: #333;
            margin-top: 20px;
        }
        .pdf-container {
            width: 100%;
            max-width: 800px;
            margin: auto;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
            overflow: hidden;
        }
        .pdf-download {
            background-color: #0073e6;
            color: white;
            text-decoration: none;
            padding: 8px 16px;
            border-radius: 5px;
            font-weight: bold;
            display: inline-block;
            margin: 20px 0;
        }
        .pdf-download:hover {
            background-color: #005bb5;
        }
    </style>
    """, unsafe_allow_html=True)

# Apply the styles
set_style()

# Centered header and download link
st.markdown(f"""
<div class="centered-content">
    <h3>Resume</h3>
    <p>Download my resume for detailed information on my professional experience.</p>
</div>
""", unsafe_allow_html=True)

# Updated path to your resume PDF in the `pages` directory
resume_path = "pages/Resume.pdf"

# PDF display and download section
if Path(resume_path).exists():
    # Embed PDF viewer using HTML iframe
    st.markdown(f"""
    <div class="pdf-container">
        <iframe src="{resume_path}" width="100%" height="600px"></iframe>
    </div>
    <div class="centered-content">
        <a href="{resume_path}" download="Karim_Osman_Resume.pdf" class="pdf-download">📥 Download My Resume</a>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error("Resume file not found. Please check the file path and try again.")
