import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse
from app_utils import tr
import smtplib
from email.message import EmailMessage



# Enhanced styling
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
        
        .availability-badge {
            background: linear-gradient(145deg, #28a745, #20c997);
            color: white;
            border-radius: 25px;
            padding: 1rem 2rem;
            margin: 1.5rem 0;
            display: inline-block;
            box-shadow: 0 5px 15px rgba(40, 167, 69, 0.3);
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        .contact-method-card {
            background: linear-gradient(145deg, #ffffff, #f8f9fa);
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-left: 5px solid #667eea;
        }
        .contact-method-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
        }
        .contact-method-card h3 {
            color: #4a4a4a;
            margin-bottom: 1rem;
        }
        .contact-method-card p {
            color: #666;
            font-size: 1.05rem;
            line-height: 1.6;
            margin-bottom: 1.5rem;
        }
        
        .contact-button {
            background: linear-gradient(145deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 0.75rem 1.5rem;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }
        .contact-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        .response-info-card {
            background: linear-gradient(145deg, #e3f2fd, #bbdefb);
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            color: #333;
        }
        .response-info-card h3 {
            color: #1565c0;
            margin-bottom: 1.5rem;
        }
        
        .looking-for-card {
            background: linear-gradient(145deg, #fff3e0, #ffe0b2);
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            color: #333;
        }
        .looking-for-card h3 {
            color: #ef6c00;
            margin-bottom: 1.5rem;
        }
        
        .contact-form-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            border-left: 5px solid #28a745;
        }
        
        .social-stats-card {
            background: linear-gradient(145deg, #f3e5f5, #e1bee7);
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            text-align: center;
            color: #333;
        }
        .social-stats-card h3 {
            color: #7b1fa2;
            margin-bottom: 1.5rem;
        }
        
        .stat-item {
            display: inline-block;
            margin: 1rem;
            text-align: center;
        }
        .stat-number {
            font-size: 2rem;
            font-weight: 700;
            color: #7b1fa2;
            display: block;
        }
        .stat-label {
            font-size: 0.9rem;
            color: #666;
        }
        
        .testimonial-card {
            background: linear-gradient(145deg, #e8f5e8, #c8e6c9);
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            font-style: italic;
            text-align: center;
            color: #333;
        }
        .testimonial-card p {
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 1rem;
        }
        .testimonial-author {
            font-weight: 600;
            color: #2e7d32;
        }
        
        .form-success {
            background: #d4edda;
            border: 1px solid #c3e6cb;
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
            color: #155724;
        }
        
        .form-error {
            background: #f8d7da;
            border: 1px solid #f5c6cb;
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
            color: #721c24;
        }
    </style>
    """, unsafe_allow_html=True)

set_style()

# Hero Section
st.markdown(f"""
<div class="contact-hero">
    <h1>{tr('CONTACT_HERO_TITLE')}</h1>
    <p style="font-size: 1.2rem; color: #555;">{tr('CONTACT_HERO_SUBTITLE')}</p>
    <div class="availability-badge">
        <strong>{tr('CONTACT_AVAILABILITY_TITLE')}</strong><br>
        <span style="font-size: 0.9rem;">{tr('CONTACT_AVAILABILITY_TEXT')}</span>
    </div>
    <p style="font-size: 0.9rem; color: #666; margin-top: 1rem;">
        {tr('CONTACT_AVAILABILITY_UPDATED')} {datetime.now().strftime('%B %d, %Y')} {tr('CONTACT_TIMEZONE_SHORT')}
    </p>
</div>
""", unsafe_allow_html=True)

# Contact Methods
st.markdown(f"## {tr('CONTACT_METHODS_TITLE')}")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="contact-method-card">
        <h3>{tr('CONTACT_PROFESSIONAL_TITLE')}</h3>
        <p>{tr('CONTACT_PROFESSIONAL_DESC')}</p>
        <a href="https://www.linkedin.com/in/karimosman89/" target="_blank" class="contact-button">
            {tr('CONTACT_PROFESSIONAL_BUTTON')}
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="contact-method-card">
        <h3>{tr('CONTACT_GITHUB_TITLE')}</h3>
        <p>{tr('CONTACT_GITHUB_DESC')}</p>
        <a href="https://github.com/karimosman89" target="_blank" class="contact-button">
            {tr('CONTACT_GITHUB_BUTTON')}
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="contact-method-card">
        <h3>{tr('CONTACT_DIRECT_TITLE')}</h3>
        <p>{tr('CONTACT_DIRECT_DESC')}</p>
        <a href="mailto:karim.programmer2020@gmail.com" class="contact-button">
            {tr('CONTACT_DIRECT_BUTTON')}
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="contact-method-card">
        <h3>{tr('CONTACT_CALENDLY_TITLE')}</h3>
        <p>{tr('CONTACT_CALENDLY_DESC')}</p>
        <a href="https://calendar.google.com/calendar/u/1/r" target="_blank" class="contact-button">
            {tr('CONTACT_CALENDLY_LINK_TEXT')}
        </a>
    </div>
    """, unsafe_allow_html=True)

# Enhanced Contact Form
st.markdown(f"""
<div class="contact-form-card">
    <h2>{tr('CONTACT_FORM_TITLE')}</h2>
    <p style="color: #666; margin-bottom: 2rem;">{tr('CONTACT_FORM_SUBTITLE')}</p>
</div>
""", unsafe_allow_html=True)

# Contact form
with st.form("contact_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input(
            tr('CONTACT_FORM_NAME'),
            placeholder=tr('CONTACT_FORM_NAME_PLACEHOLDER')
        )
        
        company = st.text_input(
            tr('CONTACT_FORM_COMPANY'),
            placeholder=tr('CONTACT_FORM_COMPANY_PLACEHOLDER')
        )
    
    with col2:
        email = st.text_input(
            tr('CONTACT_FORM_EMAIL'),
            placeholder=tr('CONTACT_FORM_EMAIL_PLACEHOLDER')
        )
        
        subject = st.selectbox(
            tr('CONTACT_FORM_SUBJECT'),
            [
                tr('CONTACT_FORM_SUBJECT_OPTION_JOB'),
                tr('CONTACT_FORM_SUBJECT_OPTION_CONSULTING'),
                tr('CONTACT_FORM_SUBJECT_OPTION_COLLABORATION'),
                tr('CONTACT_FORM_SUBJECT_OPTION_TECHNICAL'),
                tr('CONTACT_FORM_SUBJECT_OPTION_OTHER')
            ]
        )
    
    message = st.text_area(
        tr('CONTACT_FORM_MESSAGE'),
        placeholder=tr('CONTACT_FORM_MESSAGE_PLACEHOLDER'),
        height=150
    )
    
    submitted = st.form_submit_button(tr('CONTACT_FORM_SUBMIT'))
    
    if submitted:
        if name and email and message:
            # Create email content
            email_subject = f"Portfolio Contact: {subject} - {name}"
            email_body = f"""
Hello Karim,

You have received a new message through your portfolio website:

Name: {name}
Email: {email}
Company: {company if company else 'Not specified'}
Subject: {subject}

Message:
{message}

---
Sent from your portfolio contact form on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
            """
            
            try:
                # Configure in Streamlit secrets
                SMTP_SERVER = "smtp.gmail.com"
                SMTP_PORT = 587
                SMTP_USERNAME = st.secrets["gmail"]["username"]
                SMTP_PASSWORD = st.secrets["gmail"]["password"]
            
                # Create email
                msg = EmailMessage()
                msg.set_content(email_body)
                msg["Subject"] = email_subject
                msg["From"] = SMTP_USERNAME
                msg["To"] = "karim.programmer2020@gmail.com"
            
                # Send email
                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                    server.starttls()
                    server.login(SMTP_USERNAME, SMTP_PASSWORD)
                    server.send_message(msg)
            
                st.markdown(f"""
                <div class="form-success">
                    <h4>Message Sent Successfully!</h4>
                    <p>Your message has been delivered. I'll get back to you soon.</p>
                </div>
                """, unsafe_allow_html=True)
            
            except Exception as e:
                st.error(f"Error sending email: {str(e)}")
                # Fallback to mailto method    
                mailto_link = f"mailto:karim.programmer2020@gmail.com?subject={urllib.parse.quote(email_subject)}&body={urllib.parse.quote(email_body)}"
                
                st.markdown(f"""
                <div class="form-success">
                    <h4>Alternative Option</h4>
                    <p>Couldn't send automatically. Click below to open your email client:</p>
                    <a href="{mailto_link}" class="contact-button" style="margin-top: 1rem;">
                        Open Email Client
                    </a>
                </div>
                """, unsafe_allow_html=True)
                
                # Also show the prepared email content for copy-paste
                with st.expander("📋 Copy Email Content (Alternative)"):
                    st.text_input("Email Subject:", value=email_subject, key="subject_copy")
                    st.text_area("Email Body:",  value=email_body, height=200, key="body_copy")
        else:
            st.markdown(f"""
            <div class="form-error">
                {tr('CONTACT_FORM_ERROR')}
            </div>
            """, unsafe_allow_html=True)
            
# Response Time Information
st.markdown(f"""
<div class="response-info-card">
    <h3>{tr('CONTACT_RESPONSE_TITLE')}</h3>
    <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
        <div style="flex: 1; margin: 0.5rem;">
            <h4>{tr('CONTACT_QUICK_RESPONSE_TITLE')}</h4>
            <ul style="list-style-type: none; padding: 0;">
                <li>📧 {tr('CONTACT_EMAIL_RESPONSE')}</li>
                <li>💼 {tr('CONTACT_LINKEDIN_RESPONSE')}</li>
                <li>🚨 {tr('CONTACT_URGENT_RESPONSE')}</li>
            </ul>
        </div>
        <div style="flex: 1; margin: 0.5rem;">
            <h4>{tr('CONTACT_TIMEZONE_TITLE')}</h4>
            <ul style="list-style-type: none; padding: 0;">
                <li>🌍 {tr('CONTACT_TIMEZONE_PRIMARY')}</li>
                <li>⏰ {tr('CONTACT_TIMEZONE_AVAILABLE')}</li>
                <li>🤝 {tr('CONTACT_TIMEZONE_FLEXIBLE')}</li>
            </ul>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# What I'm Looking For
st.markdown(f"""
<div class="looking-for-card">
    <h3>{tr('CONTACT_LOOKING_TITLE')}</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; margin-top: 1.5rem;">
        <div>
            <h4>{tr('CONTACT_ROLES_TITLE')}</h4>
            <p>{tr('CONTACT_ROLES_DESC')}</p>
        </div>
        <div>
            <h4>{tr('CONTACT_CONSULTING_TITLE')}</h4>
            <p>{tr('CONTACT_CONSULTING_DESC')}</p>
        </div>
        <div>
            <h4>{tr('CONTACT_INNOVATION_TITLE')}</h4>
            <p>{tr('CONTACT_INNOVATION_DESC')}</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Professional Network Stats
st.markdown(f"""
<div class="social-stats-card">
    <h3>{tr('CONTACT_SOCIAL_TITLE')}</h3>
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
        <div class="stat-item">
            <span class="stat-number">{tr('CONTACT_CONNECTIONS')}</span>
            <span class="stat-label">{tr('CONTACT_CONNECTIONS_LABEL')}</span>
        </div>
        <div class="stat-item">
            <span class="stat-number">{tr('CONTACT_REPOS')}</span>
            <span class="stat-label">{tr('CONTACT_REPOS_LABEL')}</span>
        </div>
        <div class="stat-item">
            <span class="stat-number">{tr('CONTACT_EXPERIENCE')}</span>
            <span class="stat-label">{tr('CONTACT_EXPERIENCE_LABEL')}</span>
        </div>
        <div class="stat-item">
            <span class="stat-number">{tr('CONTACT_RESPONSE_RATE')}</span>
            <span class="stat-label">{tr('CONTACT_RESPONSE_RATE_LABEL')}</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Testimonial
st.markdown(f"""
<div class="testimonial-card">
    <h3>{tr('CONTACT_TESTIMONIAL_TITLE')}</h3>
    <p>"{tr('CONTACT_TESTIMONIAL_TEXT')}"</p>
    <p class="testimonial-author">{tr('CONTACT_TESTIMONIAL_AUTHOR')}</p>
</div>
""", unsafe_allow_html=True)

# Call to Action
st.markdown(f"""
<div class="contact-hero">
    <h2>{tr('CONTACT_CALL_TITLE')}</h2>
    <p style="font-size: 1.2rem; color: #555; margin-top: 2rem;">
        {tr('CONTACT_CALL_TEXT')}
    </p>
    <p style="font-size: 1.1rem; color: #666; margin-top: 1rem;">
        {tr('CONTACT_CALL_TEXT2')}
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown(f"<p style='text-align: center; color: #666; margin-top: 2rem;'>{tr('CONTACT_FOOTER')}</p>", unsafe_allow_html=True)

