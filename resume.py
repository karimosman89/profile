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
        .summary {
            color: #555; 
            font-size: 1.1em;
            line-height: 1.6;
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
st.write("""
<div class="main-content">
    <h2>Professional Overview</h2>
    <p class="summary">
        With a strong background in data science, software engineering, and project management, 
        I bring a proven track record of delivering high-impact projects and leading cross-functional 
        teams. My expertise spans data analytics, machine learning, and scalable software solutions, 
        with a commitment to driving innovation and exceeding project goals.
    </p>
    
    <h2>Highlights</h2>
    <ul class="summary">
        <li>8+ years of experience in data science and software engineering.</li>
        <li>Skilled in Python, SQL, Machine Learning, and Cloud Technologies.</li>
        <li>Extensive experience with data visualization and stakeholder communication.</li>
        <li>Proven success in managing projects from concept to deployment.</li>
    </ul>
    
    <br>
    <a href="Resume.pdf" download class="resume-button">📥 Download My Resume</a>
</div>
""", unsafe_allow_html=True)

# Footer with additional contact
st.markdown("""
<div style="text-align: center; margin-top: 30px;">
    <p style="color: #888;">For any further inquiries or to discuss potential opportunities, 
    feel free to reach out through my <a href="/contact">Contact Page</a>.</p>
</div>
""", unsafe_allow_html=True)
