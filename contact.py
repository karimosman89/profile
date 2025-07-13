import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import time
from utils import tr 

# Enhanced styling for modern contact page
def set_style():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            font-family: 'Inter', sans-serif;
        }
        
        .contact-hero {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 3rem;
            margin: 2rem 0;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            text-align: center;
        }
        
        .contact-card {
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .contact-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
        }
        .contact-card h3 {
            color: #4a4a4a;
            margin-bottom: 1.5rem;
        }
        .contact-card p {
            color: #666;
            font-size: 1.05rem;
            line-height: 1.6;
        }
        .contact-card a {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
        }
        .contact-card a:hover {
            text-decoration: underline;
        }
        
        .social-stats-container {
            display: flex;
            justify-content: space-around;
            margin-top: 2rem;
            flex-wrap: wrap;
        }
        .social-stat {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 0.5rem;
            flex: 1;
            min-width: 180px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        }
        .social-number {
            font-size: 2.2rem;
            font-weight: 700;
            color: #764ba2;
        }
        .social-label {
            font-size: 0.9rem;
            color: #555;
            margin-top: 0.5rem;
        }

        .testimonial-card {
            background: linear-gradient(145deg, #764ba2, #5d3f6a);
            border-radius: 20px;
            padding: 3rem;
            margin: 2rem 0;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
            text-align: center;
            color: white;
            font-style: italic;
        }
        .testimonial-card p {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.15rem;
            line-height: 1.7;
        }
    </style>
    """, unsafe_allow_html=True)

set_style()

# Hero Section
st.markdown(f"""
<div class="contact-hero">
    <h1>{tr('CONTACT_HERO_TITLE')}</h1>
    <p style="font-size: 1.2rem; color: #555;">{tr('CONTACT_HERO_SUBTITLE')}</p>
</div>
""", unsafe_allow_html=True)

# Contact Information Section
st.markdown(f"## {tr('CONTACT_INFO_TITLE')}")
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="contact-card">
        <h3>{tr('CONTACT_EMAIL_TITLE')}</h3>
        <p>
            {tr('CONTACT_EMAIL_DESC')}
            <br><br>
            <a href="mailto:karim.programmer2020@gmail.com">karim.programmer2020@gmail.com</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="contact-card">
        <h3>{tr('CONTACT_LINKEDIN_TITLE')}</h3>
        <p>
            {tr('CONTACT_LINKEDIN_DESC')}
            <br><br>
            <a href="https://www.linkedin.com/in/karimosman89" target="_blank">linkedin.com/in/karimosman89</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.markdown(f"""
    <div class="contact-card">
        <h3>{tr('CONTACT_GITHUB_TITLE')}</h3>
        <p>
            {tr('CONTACT_GITHUB_DESC')}
            <br><br>
            <a href="https://github.com/karimosman89" target="_blank">github.com/karimosman89</a>
        </p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div class="contact-card">
        <h3>{tr('CONTACT_CALENDLY_TITLE')}</h3>
        <p>
            {tr('CONTACT_CALENDLY_DESC')}
            <br><br>
            <a href="https://calendly.com/karim-osman/30min" target="_blank">{tr('CONTACT_CALENDLY_LINK_TEXT')}</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Quick Contact Form (if applicable, simplified for demo)
st.markdown(f"## {tr('CONTACT_FORM_TITLE')}")
with st.form("contact_form"):
    name = st.text_input(tr("CONTACT_FORM_NAME_LABEL"), placeholder=tr("CONTACT_FORM_NAME_PLACEHOLDER"))
    email = st.text_input(tr("CONTACT_FORM_EMAIL_LABEL"), placeholder=tr("CONTACT_FORM_EMAIL_PLACEHOLDER"))
    message = st.text_area(tr("CONTACT_FORM_MESSAGE_LABEL"), placeholder=tr("CONTACT_FORM_MESSAGE_PLACEHOLDER"))
    submit_button = st.form_submit_button(tr("CONTACT_FORM_SUBMIT_BUTTON"))

    if submit_button:
        # In a real application, you would send this email (e.g., using smtplib or a service like SendGrid)
        st.success(tr("CONTACT_FORM_SUCCESS_MESSAGE").format(name=name))
        time.sleep(2) # Simulate sending
        st.experimental_rerun() # Clear form after submission

# Social Proof/Engagement Metrics (Example)
st.markdown(f"## {tr('CONTACT_STATS_TITLE')}")
st.markdown(f"""
<div class="social-stats-container">
    <div class="social-stat">
        <div class="social-number">50+</div>
        <div class="social-label">{tr('CONTACT_STATS_PROJECTS_LABEL')}</div>
    </div>
    <div class="social-stat">
        <div class="social-number">8+</div>
        <div class="social-label">{tr('CONTACT_STATS_EXPERIENCE_LABEL')}</div>
    </div>
    <div class="social-stat">
        <div class="social-number">100%</div>
        <div class="social-label">{tr('CONTACT_STATS_RESPONSE_LABEL')}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Testimonial section
st.markdown(f"""
<div class="testimonial-card">
    <h3 style="color: white; margin-bottom: 2rem;">{tr('CONTACT_TESTIMONIAL_TITLE')}</h3>
    <p style="font-size: 1.2rem; font-style: italic; margin-bottom: 1rem;">
        {tr('CONTACT_TESTIMONIAL_QUOTE')}
    </p>
    <p style="font-size: 1rem; opacity: 0.9;">
        {tr('CONTACT_TESTIMONIAL_AUTHOR')}
    </p>
</div>
""", unsafe_allow_html=True)

# Call to action
st.markdown(f"""
<div class="contact-hero">
    <h2>{tr('CONTACT_CALL_TITLE')}</h2>
    <p style="font-size: 1.2rem; color: #555; margin: 2rem 0;">
        {tr('CONTACT_CALL_TEXT1')}
    </p>
    <p style="font-size: 1rem; color: #666;">
        {tr('CONTACT_CALL_TEXT2')}
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown(f"<p style='text-align: center; color: #666; margin-top: 2rem;'>{tr('CONTACT_FOOTER')}</p>", unsafe_allow_html=True)
