import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie
from app_utils import tr
import base64

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
        
        .about-hero {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 3rem;
            margin: 2rem 0;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            text-align: center;
        }
        
        .about-section {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            border-left: 5px solid #667eea;
        }
        
        .about-section h3 {
            color: #4a4a4a;
            margin-bottom: 1.5rem;
            border-bottom: 2px solid #667eea;
            padding-bottom: 0.5rem;
        }
        
        .profile-photo {
            border-radius: 50%;
            width: 180px;
            height: 180px;
            object-fit: cover;
            border: 5px solid #667eea;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
            margin-bottom: 1.5rem;
        }
        
        .highlight-box {
            background: linear-gradient(145deg, #e3f2fd, #bbdefb);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            border-left: 5px solid #2196f3;
        }
        
        .lottie-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 200px; /* Adjust as needed */
        }
        
        .video-container {
            position: relative;
            padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
            height: 0;
            overflow: hidden;
            max-width: 100%;
            background: #000;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }
        
        .video-container iframe,
        .video-container object,
        .video-container embed {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
    </style>
    """, unsafe_allow_html=True)

set_style()

@st.cache_resource
def load_lottie_local(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

@st.cache_resource
def load_profile_photo():
    try:
        return Image.open("profile-photo.jpg")
    except FileNotFoundError:
        return None

profile_photo = load_profile_photo()

# Try to load audio data
try:
    audio_data = base64.b64encode(open('karim_introduction.wav', 'rb').read()).decode()
except FileNotFoundError:
    audio_data = ""
    st.error("Audio file not found")

# Hero Section
st.markdown(f"""
<div class="about-hero">
    <h1>{tr('ABOUT_HERO_TITLE')}</h1>
    <p style="font-size: 1.2rem; color: #555;">{tr('ABOUT_HERO_SUBTITLE')}</p>
</div>
""", unsafe_allow_html=True)

# Introduction Section
st.markdown(f"""
<div class="about-section">
    <h3>{tr('ABOUT_INTRO_TITLE')}</h3>
    <div style="display: flex; flex-direction: column; align-items: center;">
        {f'<img src="data:image/jpeg;base64,{base64.b64encode(open("profile-photo.jpg", "rb").read()).decode()}" class="profile-photo">' if profile_photo else ''}
        <p style="font-size: 1.1rem; line-height: 1.8; text-align: center;">
            {tr('ABOUT_INTRO_TEXT')}
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Video Introduction Section
st.markdown(f"""
<div class="about-section">
    <h3>{tr('ABOUT_VIDEO_TITLE')}</h3>
    <p style="font-size: 1.1rem; margin-bottom: 1.5rem;">
        {tr('ABOUT_VIDEO_TEXT')}
    </p>
    <div class="video-container">
        <p style="color: white; text-align: center; padding-top: 25%; font-size: 1.2rem;">
            {tr('ABOUT_VIDEO_PLACEHOLDER')}
        </p>
        <audio controls style="width: 100%; margin-top: 1rem;">
            <source src="data:audio/wav;base64,{audio_data}" type="audio/wav">
            Your browser does not support the audio element.
        </audio>
    </div>
    <p style="font-size: 0.9rem; color: #666; margin-top: 1rem;">
        {tr('ABOUT_VIDEO_GUIDANCE')}
    </p>
</div>
""", unsafe_allow_html=True)

# My Journey Section
st.markdown(f"""
<div class="about-section">
    <h3>{tr('ABOUT_JOURNEY_TITLE')}</h3>
    <p style="font-size: 1.1rem; line-height: 1.8;">
        {tr('ABOUT_JOURNEY_TEXT')}
    </p>
    <div class="highlight-box">
        <h4>{tr('ABOUT_JOURNEY_HIGHLIGHT_TITLE')}</h4>
        <p>{tr('ABOUT_JOURNEY_HIGHLIGHT_TEXT')}</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Education Section
st.markdown(f"""
<div class="about-section">
    <h3>{tr('ABOUT_EDUCATION_TITLE')}</h3>
    <p style="font-size: 1.1rem; line-height: 1.8;">
        <strong>Machine Learning Engineering</strong><br>
        Paris 1 Panthéon-Sorbonne University [09/2023 – 08/2024]<br>
        City: Paris | Country: France | Website: https://www.pantheonsorbonne.fr/
    </p>
    <p style="font-size: 1.1rem; line-height: 1.8;">
        <strong>Over-Seas Program</strong><br>
        Akita International University [09/2020 – 03/2021]<br>
        City: Akita | Country: Japan | Website: https://web.aiu.ac.jp/en/
    </p>
    <p style="font-size: 1.1rem; line-height: 1.8;">
        <strong>Erasmus Program</strong><br>
        Universitàt Liechtenstein [11/02/2019 – 30/06/2019]<br>
        City: Vaduz | Country: Liechtenstein | Website: https://www.uni.li
    </p>
    <p style="font-size: 1.1rem; line-height: 1.8;">
        <strong>Master Degree of Finance</strong><br>
        Università di Siena [10/2017 – 06/2022]<br>
        City: Siena | Country: Italy | Website: www.unisi.it
    </p>
</div>
""", unsafe_allow_html=True)

# Philosophy Section
st.markdown(f"""
<div class="about-section">
    <h2>{tr('ABOUT_PHILOSOPHY_TITLE')}</h2>
    <p style="font-size: 1.2rem; margin-bottom: 2rem;">
        {tr('ABOUT_PHILOSOPHY_QUOTE')}
    </p>
    <p style="font-size: 1.1rem;">
        {tr('ABOUT_PHILOSOPHY_BELIEF')}
    </p>
</div>
""", unsafe_allow_html=True)

# What Drives Me Section
st.markdown(f"## {tr('ABOUT_DRIVES_TITLE')}")

col1, col2 = st.columns(2)

with col1:
    ai_lottie = load_lottie_local('ai.json') or {}
    st.markdown(f"""
    <div class="interactive-card">
        <div class="lottie-container">
            {st_lottie(ai_lottie, height=150, key='ai_lottie')}
        </div>
        <h4>{tr('DRIVES_AI_TITLE')}</h4>
        <p>{tr('DRIVES_AI_TEXT')}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    data_lottie = load_lottie_local('data-analyisis.json') or {}
    st.markdown(f"""
    <div class="interactive-card">
        <div class="lottie-container">
            {st_lottie(data_lottie, height=150, key='data_lottie')}
        </div>
        <h4>{tr('DRIVES_DATA_TITLE')}</h4>
        <p>{tr('DRIVES_DATA_TEXT')}</p>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    dl_lottie = load_lottie_local('deep-learning.json') or {}
    st.markdown(f"""
    <div class="interactive-card">
        <div class="lottie-container">
            {st_lottie(dl_lottie, height=150, key='dl_lottie')}
        </div>
        <h4>{tr('DRIVES_DL_TITLE')}</h4>
        <p>{tr('DRIVES_DL_TEXT')}</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    devops_lottie = load_lottie_local('devops.json') or {}
    st.markdown(f"""
    <div class="interactive-card">
        <div class="lottie-container">
            {st_lottie(devops_lottie, height=150, key='devops_lottie')}
        </div>
        <h4>{tr('DRIVES_DEVOPS_TITLE')}</h4>
        <p>{tr('DRIVES_DEVOPS_TEXT')}</p>
    </div>
    """, unsafe_allow_html=True)

# Call to Action
st.markdown(f"""
<div class="about-hero">
    <h2>{tr('ABOUT_CALL_TITLE')}</h2>
    <p style="font-size: 1.2rem; color: #555; margin-top: 2rem;">
        {tr('ABOUT_CALL_TEXT')}
    </p>
    <p style="font-size: 1.1rem; color: #666; margin-top: 1rem;">
        {tr('ABOUT_CALL_TEXT2')}
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown(f"<p style='text-align: center; color: #666; margin-top: 2rem;'>{tr('ABOUT_FOOTER')}</p>", unsafe_allow_html=True)
