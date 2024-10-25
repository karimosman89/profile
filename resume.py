import streamlit as st
from pdf2image import convert_from_path
from io import BytesIO
from pathlib import Path

# Path to your resume PDF in the `pages` directory
resume_path = "pages/Resume.pdf"

# Set up page styles
def set_style():
    st.markdown("""
    <style>
        .centered-content { text-align: center; font-family: Arial, sans-serif; color: #333; margin-top: 20px; }
        .pdf-download { background-color: #0073e6; color: white; text-decoration: none; padding: 8px 16px; border-radius: 5px; font-weight: bold; display: inline-block; margin: 20px 0; }
        .pdf-download:hover { background-color: #005bb5; }
        .pdf-preview { box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); border-radius: 10px; margin: auto; max-width: 90%; }
    </style>
    """, unsafe_allow_html=True)

set_style()

# Header and download section
st.markdown("""
<div class="centered-content">
    <h3>Resume</h3>
    <p>Preview my resume below or download for full details.</p>
</div>
""", unsafe_allow_html=True)

# Load the resume file
if Path(resume_path).exists():
    # Convert first page to image for preview
    pages = convert_from_path(resume_path, dpi=100, first_page=1, last_page=1)
    if pages:
        # Display the first page as an image preview
        st.image(pages[0], caption="Resume Preview", use_column_width=True)

    # Display download button
    with open(resume_path, "rb") as pdf_file:
        st.download_button(
            label="📥 Download My Full Resume",
            data=pdf_file,
            file_name="Karim_Osman_Resume.pdf",
            mime="application/pdf",
        )
else:
    st.error("Resume file not found. Please check the file path and try again.")
