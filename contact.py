import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import time

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
            border-left: 5px solid #667eea;
        }
        
        .contact-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        }
        
        .contact-button {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 15px 30px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            display: inline-flex;
            align-items: center;
            margin: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            font-size: 1.1em;
        }
        
        .contact-button:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            text-decoration: none;
            color: white;
        }
        
        .contact-button:active {
            transform: translateY(-1px) scale(1.02);
        }
        
        .availability-section {
            background: linear-gradient(135deg, #00b894, #00a085);
            color: white;
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            text-align: center;
        }
        
        .response-time {
            background: linear-gradient(135deg, #74b9ff, #0984e3);
            color: white;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            text-align: center;
        }
        
        .collaboration-card {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .collaboration-card:hover {
            transform: translateY(-5px);
        }
        
        .timezone-info {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
            border-left: 4px solid #667eea;
        }
        
        h1 {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }
        
        h2 {
            color: #2c3e50;
            font-weight: 600;
            margin: 2rem 0 1rem 0;
        }
        
        .icon {
            width: 24px;
            height: 24px;
            margin-right: 10px;
            vertical-align: middle;
        }
        
        .pulse {
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        .testimonial-card {
            background: linear-gradient(135deg, #ff6b6b, #ee5a24);
            color: white;
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .testimonial-card::before {
            content: '"';
            font-size: 6rem;
            position: absolute;
            top: -1rem;
            left: 1rem;
            opacity: 0.3;
        }
        
        .quick-contact-form {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }
        
        .social-proof {
            display: flex;
            justify-content: space-around;
            margin: 2rem 0;
            flex-wrap: wrap;
        }
        
        .social-stat {
            text-align: center;
            padding: 1rem;
        }
        
        .social-number {
            font-size: 2rem;
            font-weight: bold;
            color: #667eea;
        }
        
        .social-label {
            color: #666;
            font-size: 0.9rem;
        }
    </style>
    """, unsafe_allow_html=True)

set_style()

# Hero Section
st.markdown("""
<div class="contact-hero">
    <h1>🤝 Let's Build Something Amazing Together</h1>
    <p style="font-size: 1.3rem; color: #555; margin-top: 2rem;">
        Ready to transform your AI vision into reality? I'm here to collaborate, innovate, and deliver exceptional results.
    </p>
</div>
""", unsafe_allow_html=True)

# Current availability status
current_time = datetime.now()
st.markdown(f"""
<div class="availability-section pulse">
    <h2 style="color: white; margin-bottom: 1rem;">🟢 Currently Available for New Projects</h2>
    <p style="font-size: 1.2rem; margin-bottom: 1rem;">
        Actively seeking exciting AI engineering opportunities and collaborative projects
    </p>
    <p style="font-size: 1rem;">
        Last updated: {current_time.strftime('%B %d, %Y at %I:%M %p')} (CET)
    </p>
</div>
""", unsafe_allow_html=True)

# Contact methods with enhanced presentation
st.markdown("## 📞 Multiple Ways to Connect")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="contact-card">
        <h3>💼 Professional Networking</h3>
        <p>Connect with me on LinkedIn for professional discussions, industry insights, and networking opportunities.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <a href="https://linkedin.com/in/karimosman89" target="_blank" class="contact-button">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" class="icon"> 
        Connect on LinkedIn
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="contact-card">
        <h3>📧 Direct Communication</h3>
        <p>Reach out directly via email for project inquiries, collaboration proposals, or detailed discussions.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <a href="mailto:karim.programmer2020@gmail.com" target="_blank" class="contact-button">
        <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" class="icon"> 
        Send Email
    </a>
    """, unsafe_allow_html=True)

# GitHub section
st.markdown("""
<div class="contact-card">
    <h3>💻 Explore My Code</h3>
    <p>Browse my GitHub repositories to see my coding style, project architecture, and technical approach to problem-solving.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<a href="https://github.com/karimosman89" target="_blank" class="contact-button">
    <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" class="icon"> 
    View GitHub Profile
</a>
""", unsafe_allow_html=True)

# Response time and communication preferences
st.markdown("## ⏰ Response Time & Communication")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="response-time">
        <h3 style="color: white; margin-bottom: 1rem;">📱 Quick Response</h3>
        <p style="margin: 0;">Email: Within 24 hours</p>
        <p style="margin: 0;">LinkedIn: Within 48 hours</p>
        <p style="margin: 0;">Urgent matters: Same day</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="timezone-info">
        <h4>🌍 Timezone Information</h4>
        <p><strong>Primary:</strong> Central European Time (CET)</p>
        <p><strong>Available:</strong> 9:00 AM - 6:00 PM CET</p>
        <p><strong>Flexible:</strong> Can accommodate different timezones for important meetings</p>
    </div>
    """, unsafe_allow_html=True)

# What I'm looking for section
st.markdown("## 🎯 What I'm Looking For")

col1, col2, col3 = st.columns(3)

opportunities = [
    {
        "title": "🚀 AI Engineering Roles",
        "description": "Full-time positions in AI/ML engineering, focusing on production systems and scalable solutions."
    },
    {
        "title": "🤝 Consulting Projects",
        "description": "Short-term consulting engagements to help companies implement AI strategies and solutions."
    },
    {
        "title": "💡 Innovation Partnerships",
        "description": "Collaborative projects with startups or established companies pushing the boundaries of AI."
    }
]

for i, opportunity in enumerate(opportunities):
    col = [col1, col2, col3][i]
    with col:
        st.markdown(f"""
        <div class="collaboration-card">
            <h4>{opportunity['title']}</h4>
            <p>{opportunity['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Interactive contact form
st.markdown("## 📝 Quick Contact Form")

with st.form("contact_form"):
    st.markdown("""
    <div class="quick-contact-form">
        <h3 style="margin-top: 0;">Send me a message directly!</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Your Name *", placeholder="Enter your full name")
        email = st.text_input("Your Email *", placeholder="your.email@company.com")
    
    with col2:
        company = st.text_input("Company/Organization", placeholder="Your company name")
        subject = st.selectbox("Subject *", [
            "Job Opportunity",
            "Consulting Project",
            "Collaboration Proposal",
            "Technical Discussion",
            "Other"
        ])
    
    message = st.text_area("Message *", placeholder="Tell me about your project, opportunity, or how we can collaborate...", height=150)
    
    submitted = st.form_submit_button("🚀 Send Message", use_container_width=True)
    
    if submitted:
        if name and email and message:
            # Create mailto link with pre-filled information
            mailto_link = f"mailto:karim.programmer2020@gmail.com?subject={subject} - {name}&body=Name: {name}%0D%0AEmail: {email}%0D%0ACompany: {company}%0D%0A%0D%0AMessage:%0D%0A{message}"
            
            st.success("✅ Message prepared! Click the button below to send via your email client.")
            st.markdown(f"""
            <a href="{mailto_link}" class="contact-button" style="display: block; text-align: center; margin: 1rem auto; max-width: 300px;">
                📧 Open Email Client
            </a>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Please fill in all required fields (marked with *)")

# Social proof section
st.markdown("## 📊 Professional Network")

st.markdown("""
<div class="social-proof">
    <div class="social-stat">
        <div class="social-number">500+</div>
        <div class="social-label">LinkedIn Connections</div>
    </div>
    <div class="social-stat">
        <div class="social-number">50+</div>
        <div class="social-label">GitHub Repositories</div>
    </div>
    <div class="social-stat">
        <div class="social-number">5+</div>
        <div class="social-label">Years Experience</div>
    </div>
    <div class="social-stat">
        <div class="social-number">100%</div>
        <div class="social-label">Response Rate</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Testimonial section
st.markdown("""
<div class="testimonial-card">
    <h3 style="color: white; margin-bottom: 2rem;">What Colleagues Say</h3>
    <p style="font-size: 1.2rem; font-style: italic; margin-bottom: 1rem;">
        Karim brings exceptional technical expertise combined with a proactive approach to problem-solving. 
        His ability to translate complex AI concepts into practical business solutions is remarkable.
    </p>
    <p style="font-size: 1rem; opacity: 0.9;">
        - Former Team Lead at Configuratori
    </p>
</div>
""", unsafe_allow_html=True)

# Call to action
st.markdown("""
<div class="contact-hero">
    <h2>🌟 Ready to Start Our Collaboration?</h2>
    <p style="font-size: 1.2rem; color: #555; margin: 2rem 0;">
        Whether you have a specific project in mind or just want to explore possibilities, 
        I'm excited to hear from you. Let's create something extraordinary together!
    </p>
    <p style="font-size: 1rem; color: #666;">
        Every great project starts with a conversation. Let's have ours.
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: #666; margin-top: 2rem;'>© 2024 Karim Osman - Always Ready to Innovate and Collaborate</p>", unsafe_allow_html=True)
