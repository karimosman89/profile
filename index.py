import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie
import plotly.graph_objects as go
import logging
import skills
import projects
import about
import resume
import contact
import importlib
import random
import time
from utils import tr # Corrected import

# Configure the page
st.set_page_config(page_title=tr("PAGE_TITLE"), layout="wide", initial_sidebar_state="expanded")
logging.basicConfig(level=logging.INFO)

@st.cache_resource
def load_lottie_local(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

@st.cache_resource
def load_profile_photo():
    return Image.open("profile-photo.jpg")

# Load Lottie animations
data_analysis_animation = load_lottie_local('data-analyisis.json')
data_engineer_animation = load_lottie_local('data-engineer.json')
ai_engineering_animation = load_lottie_local('ai-engineering.json')
ai_animation = load_lottie_local('ai.json')
deep_learning_animation = load_lottie_local('deep-learning.json')
dev_ops_animation = load_lottie_local('devops.json')
profile_photo = load_profile_photo()

# Enhanced styles with modern design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        font-family: 'Inter', sans-serif;
    }
    
    .hero-section {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 3rem;
        margin: 2rem 0;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
    }
    
    .interactive-card {
        background: linear-gradient(145deg, #ffffff, #f0f0f0);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
    }
    
    .interactive-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    }
    
    .proactive-section {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        border-radius: 20px;
        padding: 3rem;
        margin: 2rem 0;
        text-align: center;
    }
    
    .chat-interface {
        background: #f8f9fa;
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        border: 2px solid #e9ecef;
    }
    
    h1 {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    h2 {
        color: #2c3e50;
        font-weight: 600;
        margin: 2rem 0 1rem 0;
    }
    
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .typing-effect {
        overflow: hidden;
        border-right: .15em solid orange;
        white-space: nowrap;
        margin: 0 auto;
        letter-spacing: .15em;
        animation: typing 3.5s steps(40, end), blink-caret .75s step-end infinite;
    }
    
    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: orange; }
    }
    [lang="ar"], [lang="he"] {{
        direction: rtl;
        text-align: right;
    }}
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
# Make sure utils.language_selector returns the selected page name or handles navigation directly.
# If utils.language_selector sets st.session_state.page, then 'page' variable isn't needed here.
# Assuming it sets st.session_state.page and returns it for clarity.
page = utils.language_selector()


# Interactive AI Chat Bot Section
def ai_chat_interface():
    st.markdown(f"### {tr('AI_CHAT_TITLE')}") # Corrected tr()
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Predefined questions for quick interaction
    quick_questions = [
        tr("STRONGEST_SKILL"),
        tr("IMPACTFUL_PROJECT"),
        tr("PROBLEM_SOLVING"),
        tr("DIFFERENT"),
        tr("AI_VISION")
    ]
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_question = st.text_input(tr("AI_CHAT_PROMPT"), placeholder=tr("AI_CHAT_PLACEHOLDER")) # Corrected tr()
    
    with col2:
        if st.button(tr("AI_CHAT_RANDOM")): # Corrected tr()
            user_question = random.choice(quick_questions)
            st.session_state.random_question = user_question
    
    # Quick question buttons
    st.markdown(f"**{tr('QUICK_QUESTIONS')}**") # Corrected tr()
    cols = st.columns(len(quick_questions))
    for i, question in enumerate(quick_questions):
        if cols[i].button(f"❓ {question[:20]}...", key=f"quick_{i}"):
            user_question = question
    
    # AI responses based on questions
    ai_responses = {
        tr("STRONGEST_SKILL"): tr("STRONGEST_SKILL_RESPONSE"),
        tr("IMPACTFUL_PROJECT"): tr("IMPACTFUL_PROJECT_RESPONSE"),
        tr("PROBLEM_SOLVING"): tr("PROBLEM_SOLVING_RESPONSE"),
        tr("DIFFERENT"): tr("DIFFERENT_RESPONSE"),
        tr("AI_VISION"): tr("AI_VISION_RESPONSE")
    }
    
    if user_question:
        # Simulate typing effect
        with st.spinner("🤔 " + tr("THINKING")): # Corrected tr()
            time.sleep(1)
        
        response = ai_responses.get(user_question, 
            tr("DEFAULT_RESPONSE").format(question=user_question)) # Corrected tr()
        
        st.markdown(f"**🤖 {tr('AI_ASSISTANT')}:** {response}") # Corrected tr()
        
        # Add to chat history
        st.session_state.chat_history.append({"question": user_question, "answer": response})

# Enhanced metrics display
def show_impact_metrics():
    st.markdown(f"### {tr('METRICS_TITLE')}") # Corrected tr()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card pulse">
            <h3 style="color: #e74c3c; margin: 0;">20%</h3>
            <p style="margin: 0;">{tr("PERFORMANCE")}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card pulse">
            <h3 style="color: #27ae60; margin: 0;">30%</h3>
            <p style="margin: 0;">{tr("EFFICIENCY")}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card pulse">
            <h3 style="color: #3498db; margin: 0;">25%</h3>
            <p style="margin: 0;">{tr('PROCESSING')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card pulse">
            <h3 style="color: #f39c12; margin: 0;">5+</h3>
            <p style="margin: 0;">{tr('EXPERIENCE')}</p>
        </div>
        """, unsafe_allow_html=True)

# Proactive approach showcase
def proactive_showcase():
    st.markdown(f"""
    <div class="proactive-section">
        <h2 style="color: white; margin-bottom: 2rem;">{tr('PROACTIVE_TITLE')}</h2>
        <p style="font-size: 1.2rem; margin-bottom: 2rem;">
            {tr('PROACTIVE_TEXT')}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="interactive-card">
            <h3>{tr('CANDIDATE_ASSISTANT')}</h3>
            <p>{tr('CANDIDATE_DESC')}</p>
            <ul>
                <li>{tr('CANDIDATE_FEATURE1')}</li>
                <li>{tr('CANDIDATE_FEATURE2')}</li>
                <li>{tr('CANDIDATE_FEATURE3')}</li>
                <li>{tr('CANDIDATE_FEATURE4')}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="interactive-card">
            <h3>{tr('TECH_IMPLEMENTATION')}</h3>
            <p>{tr('TECH_DESC')}</p>
            <ul>
                <li>{tr('TECH_FEATURE1')}</li>
                <li>{tr('TECH_FEATURE2')}</li>
                <li>{tr('TECH_FEATURE3')}</li>
                <li>{tr('TECH_FEATURE4')}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Main page rendering
if page == tr("NAV_HOME"): # Corrected tr()
    # Hero section with typing effect
    st.markdown(f"""
    <div class="hero-section">
        <h1 class="typing-effect">{tr('WELCOME_TITLE')}</h1> # Corrected tr()
        <p style="text-align: center; font-size: 1.3rem; color: #555; margin-top: 2rem;">
            {tr('TAGLINE')} # Corrected tr()
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive AI Chat Interface
    ai_chat_interface()
    
    # Impact Metrics
    show_impact_metrics()
    
    # Proactive Approach Showcase
    proactive_showcase()
    
    # Enhanced expertise showcase
    st.markdown(f"### {tr('EXPERTISE_TITLE')}") # Corrected tr()
    
    col1, col2, col3 = st.columns(3)
    
    expertise_areas = [
        (tr("ML_TITLE"), tr("ML_DESC"), data_analysis_animation),
        (tr("AI_ENGINEERING_TITLE"), tr("AI_ENGINEERING_DESC"), ai_engineering_animation),
        (tr("DATA_SCIENCE_TITLE"), tr("DATA_SCIENCE_DESC"), ai_animation),
        (tr("DL_TITLE"), tr("DL_DESC"), deep_learning_animation),
        (tr("CLOUD_TITLE"), tr("CLOUD_DESC"), dev_ops_animation),
        (tr("INNOVATION_TITLE"), tr("INNOVATION_DESC"), data_engineer_animation)
    ]
    
    for i, (title, desc, animation) in enumerate(expertise_areas):
        col = [col1, col2, col3][i % 3]
        with col:
            st.markdown(f"""
            <div class="interactive-card">
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)
            st_lottie(animation, height=100, key=f"expertise_{i}")

elif page == tr("NAV_ABOUT"): # Corrected tr()
    logging.info("Loading About Page")
    importlib.reload(about)

elif page == tr("NAV_PROJECTS"): # Corrected tr()
    logging.info("Loading Projects Page")
    importlib.reload(projects)

elif page == tr("NAV_SKILLS"): # Corrected tr()
    logging.info("Loading Skills Page")
    importlib.reload(skills)

elif page == tr("NAV_CONTACT"): # Corrected tr()
    logging.info("Loading Contact Page")
    importlib.reload(contact)

elif page == tr("NAV_RESUME"): # Corrected tr()
    logging.info("Loading Resume Page")
    importlib.reload(resume)
