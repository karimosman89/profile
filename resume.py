import streamlit as st

# Custom styling for professional look
def set_style():
    st.markdown("""
    <style>
        .main-content { 
            text-align: left; 
            font-family: 'Arial', sans-serif; 
            color: #333; 
            background-color: #f7f9fc; /* Subtle professional blue */
            padding: 30px; 
            border-radius: 10px;
        }
        h1 {
            color: #264653; /* Dark teal for title */
            font-weight: bold;
        }
        h2 {
            color: #2a9d8f; /* Lighter teal for section headings */
        }
        .resume-button {
            background-color: #e76f51; /* Contrasting download button color */
            color: white; 
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-size: 1.1em;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
        }
        .resume-button:hover {
            transform: scale(1.05);
        }
    </style>
    """, unsafe_allow_html=True)

# Apply styles
set_style()

# Page Title
st.title("📄 Resume")

# Introductory Text
st.markdown("""
<div class="main-content">
    <h2>Professional Overview</h2>
</div>
""", unsafe_allow_html=True)
st.write("""
With a strong background in data science, software engineering, and project management, 
I bring a proven track record of delivering high-impact projects and leading cross-functional 
teams. My expertise spans data analytics, machine learning, and scalable software solutions, 
with a commitment to driving innovation and exceeding project goals.
""")

# Display Resume PDF Inline
st.markdown("### 📑 Read My Resume")
st.markdown("Below is my resume. You can also download it for offline viewing.")

# Embed PDF for in-app viewing
st.components.v1.iframe("./Resume.pdf", height=600)

# Prepare resume for download
with open("Resume.pdf", "rb") as pdf_file:
    pdf_data = pdf_file.read()

# Download Button
st.download_button(
    label="📥 Download My Resume",
    data=pdf_data,  # Using the saved pdf data
    file_name="Karim_Osman_Resume.pdf",
    mime="application/pdf",
    help="Download my resume to explore more details about my experience and skills."
)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 30px;">
    <p style="color: #888;">For further inquiries or to discuss potential opportunities, 
    feel free to reach out through my <a href="./contact.py">Contact Page</a>.</p>
</div>
""", unsafe_allow_html=True)
