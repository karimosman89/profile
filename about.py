import streamlit as st
from PIL import Image
import plotly.graph_objects as go
import plotly.express as px
from utils import tr # Make sure utils.py is accessible and contains tr()

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
            background: linear-gradient(145deg, #e6e6fa, #d0b3ff); /* Adjusted gradient to match philosophy section in previous message */
            border-radius: 20px;
            padding: 3rem;
            margin: 2rem 0;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
            text-align: center;
            color: #333;
        }
        .philosophy-section h2 {
            color: #5d3f6a; /* Darker purple for philosophy title */
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

        .value-card { /* Added from your previous script to ensure style exists */
            background: white;
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .value-card:hover {
            transform: translateY(-5px);
        }

        .quote-section { /* Added from your previous script to ensure style exists */
            background: #f8f9fa;
            border-left: 5px solid #667eea;
            padding: 2rem;
            margin: 2rem 0;
            border-radius: 10px;
            font-style: italic;
            font-size: 1.2rem;
            text-align: center;
        }
        
    </style>
    """, unsafe_allow_html=True)

set_style()

# Load profile photo (ensure 'profile-photo.jpg' is in the same directory or provide full path)
profile_photo = None
try:
    profile_photo = Image.open("profile-photo.jpg")
except FileNotFoundError:
    st.error("Profile photo not found. Please ensure 'profile-photo.jpg' is in the correct directory.")
    # No need to set to None again, it's already None if FileNotFoundError occurs.

# Convert image to base64 for embedding in markdown
import base64
encoded_image = ""
if profile_photo:
    from io import BytesIO
    buffered = BytesIO()
    profile_photo.save(buffered, format="JPEG")
    encoded_image = base64.b64encode(buffered.getvalue()).decode()

# Hero Section - About Me
st.markdown(f"""
<div class="hero-about">
    <h1>{tr('ABOUT_HERO_TITLE')}</h1>
    <p style="font-size: 1.2rem; color: #555;">{tr('ABOUT_HERO_SUBTITLE')}</p>
    {"<img src='data:image/jpeg;base64," + encoded_image + "' style='width: 150px; height: 150px; border-radius: 50%; object-fit: cover; margin-top: 1.5rem; border: 4px solid #667eea; box-shadow: 0 0 20px rgba(102, 126, 234, 0.5);' alt='Profile Photo'>" if profile_photo else ''}
</div>
""", unsafe_allow_html=True)

# Personal Philosophy Section (Corrected to use JSON keys)
st.markdown(f"""
<div class="philosophy-section">
    <h2>{tr('ABOUT_PHILOSOPHY_TITLE')}</h2>
    <p style="font-size: 1.2rem; margin-bottom: 2rem;">
        {tr('ABOUT_PHILOSOPHY_QUOTE')}
    </p>
    <p style="font-size: 1.1rem;">
        {tr('ABOUT_PHILOSOPHY_BELIEF')}
    </p>
</div>
""", unsafe_allow_html=True)

# What Drives Me Section (Corrected to use JSON keys)
st.markdown(f"## {tr('ABOUT_DRIVES_TITLE')}")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="story-card">
        <h3>{tr('ABOUT_CURIOSITY_TITLE')}</h3>
        <p>
            {tr('ABOUT_CURIOSITY_DESC')}
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="story-card">
        <h3>{tr('ABOUT_IMPACT_TITLE')}</h3>
        <p>
            {tr('ABOUT_IMPACT_DESC')}
        </p>
    </div>
    """, unsafe_allow_html=True)

# My Journey Timeline (Corrected to use JSON keys)
st.markdown(f"## {tr('ABOUT_JOURNEY_TITLE')}")

timeline_events = [
    {
        "year": tr('ABOUT_TIMELINE_EVENT1_YEAR'),
        "title": tr('ABOUT_TIMELINE_EVENT1_TITLE'),
        "description": tr('ABOUT_TIMELINE_EVENT1_DESC')
    },
    {
        "year": tr('ABOUT_TIMELINE_EVENT2_YEAR'),
        "title": tr('ABOUT_TIMELINE_EVENT2_TITLE'),
        "description": tr('ABOUT_TIMELINE_EVENT2_DESC')
    },
    {
        "year": tr('ABOUT_TIMELINE_EVENT3_YEAR'),
        "title": tr('ABOUT_TIMELINE_EVENT3_TITLE'),
        "description": tr('ABOUT_TIMELINE_EVENT3_DESC')
    },
    {
        "year": tr('ABOUT_TIMELINE_EVENT4_YEAR'),
        "title": tr('ABOUT_TIMELINE_EVENT4_TITLE'),
        "description": tr('ABOUT_TIMELINE_EVENT4_DESC')
    }
]

for event in timeline_events:
    st.markdown(f"""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-content">
            <h4>{event['year']}: {event['title']}</h4>
            <p>{event['description']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Core Values Section (Corrected to use JSON keys)
st.markdown(f"## {tr('ABOUT_VALUES_TITLE')}")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="value-card">
        <h3>{tr('ABOUT_COLLABORATION_TITLE')}</h3>
        <p>
            {tr('ABOUT_COLLABORATION_DESC')}
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="value-card">
        <h3>{tr('ABOUT_LEARNING_TITLE')}</h3>
        <p>
            {tr('ABOUT_LEARNING_DESC')}
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="value-card">
        <h3>{tr('ABOUT_RESULTS_TITLE')}</h3>
        <p>
            {tr('ABOUT_RESULTS_DESC')}
        </p>
    </div>
    """, unsafe_allow_html=True)

# Skills Evolution Chart (Title corrected)
st.markdown(f"## {tr('ABOUT_SKILLS_EVOLUTION_TITLE')}")

# Create a skills evolution chart (data is hardcoded, consider moving to JSON if dynamic)
years = [2014, 2016, 2018, 2020, 2022, 2024]
python_skills = [20, 40, 60, 80, 90, 95]
ml_skills = [0, 10, 30, 60, 85, 95]
ai_engineering = [0, 0, 20, 50, 80, 95]
cloud_devops = [0, 0, 10, 40, 70, 90]

fig = go.Figure()
fig.add_trace(go.Scatter(x=years, y=python_skills, mode='lines+markers', name='Python & Programming', line=dict(color='#667eea')))
fig.add_trace(go.Scatter(x=years, y=ml_skills, mode='lines+markers', name='Machine Learning', line=dict(color='#ff6b6b')))
fig.add_trace(go.Scatter(x=years, y=ai_engineering, mode='lines+markers', name='AI Engineering', line=dict(color='#74b9ff')))
fig.add_trace(go.Scatter(x=years, y=cloud_devops, mode='lines+markers', name='Cloud & DevOps', line=dict(color='#00b894')))

fig.update_layout(
    title=tr('ABOUT_SKILLS_EVOLUTION_TITLE'), # Title from translation
    xaxis_title='Year', # Consider translating these if needed: tr('CHART_YEAR_AXIS')
    yaxis_title='Proficiency Level (%)', # Consider translating these if needed: tr('CHART_PROFICIENCY_AXIS')
    hovermode='x unified',
    template='plotly_white'
)

st.plotly_chart(fig, use_container_width=True)

# Personal Insights Section (Corrected to use JSON keys)
st.markdown(f"""
<div class="quote-section">
    {tr('ABOUT_QUOTE')}
</div>
""", unsafe_allow_html=True)

# What I'm Working On Now (Corrected to use JSON keys)
st.markdown(f"## {tr('ABOUT_EXPLORE_TITLE')}")

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

# Call to Action (Corrected to use JSON keys)
st.markdown(f"""
<div class="philosophy-section">
    <h2 style="color: white; margin-bottom: 2rem;">{tr('ABOUT_CALL_TITLE')}</h2>
    <p style="font-size: 1.2rem; margin-bottom: 2rem;">
        {tr('ABOUT_CALL_TEXT')}
    </p>
    <p style="font-size: 1.1rem;">
        {tr('ABOUT_CALL_TEXT2')}
    </p>
</div>
""", unsafe_allow_html=True)

# Footer (Corrected to use JSON keys)
st.markdown(f"<p style='text-align: center; color: #666; margin-top: 2rem;'>{tr('ABOUT_FOOTER')}</p>", unsafe_allow_html=True)
