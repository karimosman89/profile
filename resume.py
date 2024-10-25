import streamlit as st
from pathlib import Path

# Path to your resume PDF in the `pages` directory
resume_path = "assets/Resume.pdf"

# Set up page styles
def set_style():
    st.markdown("""
    <style>
        .centered-content { text-align: center; font-family: Arial, sans-serif; color: #333; margin-top: 20px; }
        .pdf-download { background-color: #0073e6; color: white; text-decoration: none; padding: 8px 16px; border-radius: 5px; font-weight: bold; display: inline-block; margin: 20px 0; }
        .pdf-container { border: 2px solid #ddd; border-radius: 8px; margin: auto; max-width: 90%; height: 800px; }
        iframe { width: 100%; height: 800px; border: none; }
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

# Embed the PDF if it exists
if Path(resume_path).exists():
    # Display PDF in an iframe
    pdf_display = f'<iframe src="{resume_path}"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

    # Download button for the full resume
    with open(resume_path, "rb") as pdf_file:
        st.download_button(
            label="📥 Download My Full Resume",
            data=pdf_file,
            file_name="Karim_Osman_Resume.pdf",
            mime="application/pdf",
        )
else:
    st.error("Resume file not found. Please check the file path and try again.")
