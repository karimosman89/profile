import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import time
from utils import tr 



# Initialize session state for page
if 'page' not in st.session_state:
    st.session_state.page = 'contact'

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

# Current availability status
current_time = datetime.now()
st.markdown(f"""
<div class="availability-section pulse">
    <h2 style="color: white; margin-bottom: 1rem;">{tr('CONTACT_AVAILABILITY_TITLE')}</h2>
    <p style="font-size: 1.2rem; margin-bottom: 1rem;">
        {tr('CONTACT_AVAILABILITY_TEXT')}
    </p>
    <p style="font-size: 1rem;">
        {tr('CONTACT_AVAILABILITY_UPDATED')} {current_time.strftime('%B %d, %Y at %I:%M %p')} {tr('CONTACT_TIMEZONE_SHORT')}
    </p>
</div>
""", unsafe_allow_html=True)


# Contact Information Section
st.markdown(f"## {tr('CONTACT_METHODS_TITLE')}") # Using existing key from JSON
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="contact-card">
        <h3>{tr('CONTACT_PROFESSIONAL_TITLE')}</h3>
        <p>
            {tr('CONTACT_PROFESSIONAL_DESC')}
            <br><br>
            <a href="https://www.linkedin.com/in/karimosman89" target="_blank">linkedin.com/in/karimosman89</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="contact-card">
        <h3>{tr('CONTACT_DIRECT_TITLE')}</h3>
        <p>
            {tr('CONTACT_DIRECT_DESC')}
            <br><br>
            <a href="mailto:karim.programmer2020@gmail.com">karim.programmer2020@gmail.com</a>
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
with st.form(key="contact_form"):
    st.markdown(f"""
    <div class="quick-contact-form">
        <h3 style="margin-top: 0;">{tr('CONTACT_FORM_SUBTITLE')}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1_form, col2_form = st.columns(2)
    
    with col1_form:
        name = st.text_input(tr("CONTACT_FORM_NAME"), placeholder=tr("CONTACT_FORM_NAME_PLACEHOLDER"))
        email = st.text_input(tr("CONTACT_FORM_EMAIL"), placeholder=tr("CONTACT_FORM_EMAIL_PLACEHOLDER"))
    
    with col2_form:
        company = st.text_input(tr("CONTACT_FORM_COMPANY"), placeholder=tr("CONTACT_FORM_COMPANY_PLACEHOLDER"))
        subject = st.selectbox(tr("CONTACT_FORM_SUBJECT"), [
            tr("CONTACT_FORM_SUBJECT_OPTION_JOB"),
            tr("CONTACT_FORM_SUBJECT_OPTION_CONSULTING"),
            tr("CONTACT_FORM_SUBJECT_OPTION_COLLABORATION"),
            tr("CONTACT_FORM_SUBJECT_OPTION_TECHNICAL"),
            tr("CONTACT_FORM_SUBJECT_OPTION_OTHER")
        ])
    
    message = st.text_area(tr("CONTACT_FORM_MESSAGE"), placeholder=tr("CONTACT_FORM_MESSAGE_PLACEHOLDER"), height=150)
    
    submitted = st.form_submit_button(tr("CONTACT_FORM_SUBMIT"), use_container_width=True)
    
    if submitted:
        if name and email and message:
            # Create mailto link with pre-filled information
            mailto_link = f"mailto:karim.programmer2020@gmail.com?subject={subject} - {name}&body=Name: {name}%0D%0AEmail: {email}%0D%0ACompany: {company}%0D%0A%0D%0AMessage:%0D%0A{message}"
            
            st.success(tr("CONTACT_FORM_SUCCESS"))
            st.markdown(f"""
            <a href="{mailto_link}" class="contact-button" style="display: block; text-align: center; margin: 1rem auto; max-width: 300px;">
                📧 {tr('CONTACT_FORM_EMAIL_BUTTON')}
            </a>
            """, unsafe_allow_html=True)
        else:
            st.error(tr("CONTACT_FORM_ERROR"))

# Social Proof/Engagement Metrics (Example)
st.markdown(f"## {tr('CONTACT_SOCIAL_TITLE')}") # Using existing key from JSON
st.markdown(f"""
<div class="social-stats-container">
    <div class="social-stat">
        <div class="social-number">{tr('CONTACT_REPOS')}</div>
        <div class="social-label">{tr('CONTACT_REPOS_LABEL')}</div>
    </div>
    <div class="social-stat">
        <div class="social-number">{tr('CONTACT_EXPERIENCE')}</div>
        <div class="social-label">{tr('CONTACT_EXPERIENCE_LABEL')}</div>
    </div>
    <div class="social-stat">
        <div class="social-number">{tr('CONTACT_RESPONSE_RATE')}</div>
        <div class="social-label">{tr('CONTACT_RESPONSE_RATE_LABEL')}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Testimonial section
st.markdown(f"""
<div class="testimonial-card">
    <h3 style="color: white; margin-bottom: 2rem;">{tr('CONTACT_TESTIMONIAL_TITLE')}</h3>
    <p style="font-size: 1.2rem; font-style: italic; margin-bottom: 1rem;">
        {tr('CONTACT_TESTIMONIAL_TEXT')}
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
        {tr('CONTACT_CALL_TEXT')}
    </p>
    <p style="font-size: 1rem; color: #666;">
        {tr('CONTACT_CALL_TEXT2')}
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown(f"<p style='text-align: center; color: #666; margin-top: 2rem;'>{tr('CONTACT_FOOTER')}</p>", unsafe_allow_html=True)
