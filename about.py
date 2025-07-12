import streamlit as st
from PIL import Image
import plotly.graph_objects as go
import plotly.express as px
from utils import tr 

# Enhanced styling for a more modern and engaging look
def set_style():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            font-family: 'Inter', sans-serif;
        }
        
        .hero-about {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 3rem;
            margin: 2rem 0;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            text-align: center;
        }
        
        .story-card {
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            border-left: 5px solid #667eea;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .story-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
        }
        .story-card h3 {
            color: #4a4a4a;
            margin-bottom: 1rem;
        }
        .story-card p {
            color: #666;
            font-size: 1.05rem;
            line-height: 1.6;
        }
        
        .philosophy-section {
            background: linear-gradient(145deg, #e6e6fa, #d0b3ff);
            border-radius: 20px;
            padding: 3rem;
            margin: 2rem 0;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
            text-align: center;
            color: #333;
        }
        .philosophy-section h2 {
            color: #5d3f6a;
            margin-bottom: 2rem;
        }
        .philosophy-section p {
            font-size: 1.1rem;
            line-height: 1.7;
            color: #4a4a4a;
        }
        
        .timeline-item {
            display: flex;
            margin-bottom: 2rem;
        }
        .timeline-dot {
            width: 20px;
            height: 20px;
            background-color: #667eea;
            border-radius: 50%;
            margin-right: 1.5rem;
            flex-shrink: 0;
            border: 3px solid #fff;
            box-shadow: 0 0 0 2px #667eea;
        }
        .timeline-content {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            padding: 1.5rem;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
            flex-grow: 1;
        }
        .timeline-content h4 {
            color: #4a4a4a;
            margin-top: 0;
            margin-bottom: 0.5rem;
        }
        .timeline-content p {
            color: #666;
            font-size: 0.95rem;
        }
    </style>
    """, unsafe_allow_html=True)

set_style()

# Load profile photo (ensure 'profile-photo.jpg' is in the same directory or provide full path)
try:
    profile_photo = Image.open("profile-photo.jpg")
except FileNotFoundError:
    st.error("Profile photo not found. Please ensure 'profile-photo.jpg' is in the correct directory.")
    profile_photo = None # Set to None or a placeholder if file not found

# Hero Section - About Me
st.markdown(f"""
<div class="hero-about">
    <h1>{tr('ABOUT_HERO_TITLE')}</h1>
    <p style="font-size: 1.2rem; color: #555;">{tr('ABOUT_HERO_SUBTITLE')}</p>
    {"<img src='data:image/jpeg;base64," + (Image.open("profile-photo.jpg").tobytes().hex() if profile_photo else '') + "' style='width: 150px; height: 150px; border-radius: 50%; object-fit: cover; margin-top: 1.5rem; border: 4px solid #667eea; box-shadow: 0 0 20px rgba(102, 126, 234, 0.5);' alt='Profile Photo'>" if profile_photo else ''}
</div>
""", unsafe_allow_html=True)


# My Story Section
st.markdown(f"## {tr('ABOUT_STORY_TITLE')}")
st.markdown(f"""
<div class="story-card">
    <h3>{tr('ABOUT_STORY_BACKGROUND_TITLE')}</h3>
    <p>
        {tr('ABOUT_STORY_BACKGROUND_DESC')}
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="story-card">
    <h3>{tr('ABOUT_STORY_AI_JOURNEY_TITLE')}</h3>
    <p>
        {tr('ABOUT_STORY_AI_JOURNEY_DESC')}
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="story-card">
    <h3>{tr('ABOUT_STORY_PASSION_TITLE')}</h3>
    <p>
        {tr('ABOUT_STORY_PASSION_DESC')}
    </p>
</div>
""", unsafe_allow_html=True)

# Philosophy Section
st.markdown(f"""
<div class="philosophy-section">
    <h2>{tr('ABOUT_PHILOSOPHY_TITLE')}</h2>
    <p>{tr('ABOUT_PHILOSOPHY_DESC')}</p>
    <p><strong>{tr('ABOUT_PHILOSOPHY_PRINCIPLES_TITLE')}</strong></p>
    <ul>
        <li>{tr('ABOUT_PHILOSOPHY_PRINCIPLE1')}</li>
        <li>{tr('ABOUT_PHILOSOPHY_PRINCIPLE2')}</li>
        <li>{tr('ABOUT_PHILOSOPHY_PRINCIPLE3')}</li>
        <li>{tr('ABOUT_PHILOSOPHY_PRINCIPLE4')}</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Key Milestones (Example Timeline)
st.markdown(f"## {tr('ABOUT_MILESTONES_TITLE')}")
milestones = [
    {"year": "2024", "title": tr('MILESTONE_2024_TITLE'), "description": tr('MILESTONE_2024_DESC')},
    {"year": "2022", "title": tr('MILESTONE_2022_TITLE'), "description": tr('MILESTONE_2022_DESC')},
    {"year": "2020", "title": tr('MILESTONE_2020_TITLE'), "description": tr('MILESTONE_2020_DESC')},
    {"year": "2018", "title": tr('MILESTONE_2018_TITLE'), "description": tr('MILESTONE_2018_DESC')},
]

for milestone in milestones:
    st.markdown(f"""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-content">
            <h4>{milestone['year']}: {milestone['title']}</h4>
            <p>{milestone['description']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Current Focus & Future Interests
st.markdown(f"## {tr('ABOUT_CURRENT_FOCUS_TITLE')}")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="story-card">
        <h3>{tr('ABOUT_AI_AGENTS_TITLE')}</h3>
        <p>
            {tr('ABOUT_AI_AGENTS_DESC')}
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="story-card">
        <h3>{tr('ABOUT_EXPLAINABLE_AI_TITLE')}</h3>
        <p>
            {tr('ABOUT_EXPLAINABLE_AI_DESC')}
        </p>
    </div>
    """, unsafe_allow_html=True)

# Call to Action
st.markdown(f"""
<div class="philosophy-section">
    <h2 style="color: white; margin-bottom: 2rem;">{tr('ABOUT_CALL_TITLE')}</h2>
    <p style="font-size: 1.2rem; margin-bottom: 2rem;">
        {tr('ABOUT_CALL_TEXT1')}
    </p>
    <p style="font-size: 1.1rem;">
        {tr('ABOUT_CALL_TEXT2')}
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown(f"<p style='text-align: center; color: #666; margin-top: 2rem;'>{tr('ABOUT_FOOTER')}</p>", unsafe_allow_html=True)
