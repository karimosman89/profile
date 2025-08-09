import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie
import plotly.graph_objects as go
import plotly.express as px
import logging
import skills
import projects
import about
import resume
import contact
import importlib
import random
import time
import base64
from app_utils import  language_selector, get_browser_lang

if 'lang' not in st.session_state:
    st.session_state.lang = get_browser_lang()
    
# Configure the page
st.set_page_config(
    page_title="Karim Osman - AI Engineer", 
    layout="wide", 
    initial_sidebar_state="expanded",
    page_icon="🤖",
    menu_items={
        'Get Help': 'mailto:karim.programmer2020@gmail.com',
        'Report a bug': 'mailto:karim.programmer2020@gmail.com',
        'About': "AI Engineer Portfolio - Karim Osman"
    }
)
logging.basicConfig(level=logging.INFO)

@st.cache_resource
def load_lottie_local(filepath: str):
    """Load lottie animation from local file"""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

@st.cache_resource
def load_profile_photo():
    """Load profile photo"""
    try:
        return Image.open("profile-photo.jpg")
    except FileNotFoundError:
        return None

# Professional CSS Styles - All inline to avoid missing modules
PROFESSIONAL_CSS = """

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    .hero-container {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 20px;
        padding: 3rem 2rem;
        margin: 2rem 0;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
        backdrop-filter: blur(10px);
        text-align: center;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .hero-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        background-size: 200% 100%;
        animation: gradient-shift 3s ease-in-out infinite;
    }
    
    @keyframes gradient-shift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .ai-expertise-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .expertise-card {
        background: linear-gradient(145deg, #ffffff, #f8fafc);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        border: 1px solid rgba(102, 126, 234, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .expertise-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(102, 126, 234, 0.05) 0%, transparent 70%);
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    
    .expertise-card:hover::before {
        opacity: 1;
    }
    
    .expertise-card:hover {
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 35px 70px rgba(0, 0, 0, 0.15);
        border-color: rgba(102, 126, 234, 0.3);
    }
    
    .expertise-icon {
        font-size: 3.5rem;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: block;
        position: relative;
        z-index: 1;
    }
    
    .metrics-container {
        background: linear-gradient(135deg, #1a1a1a, #2d2d2d);
        color: white;
        border-radius: 25px;
        padding: 4rem 2rem;
        margin: 3rem 0;
        position: relative;
        overflow: hidden;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
    }
    
    .metrics-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(from 0deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1), rgba(240, 147, 251, 0.1), rgba(102, 126, 234, 0.1));
        animation: rotate 20s linear infinite;
    }
    
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 3rem;
        position: relative;
        z-index: 1;
    }
    
    .metric-item {
        text-align: center;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .metric-number {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea, #f093fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: block;
        margin-bottom: 0.5rem;
    }
    
    .cta-section {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24, #ff9ff3);
        color: white;
        border-radius: 25px;
        padding: 4rem 2rem;
        margin: 3rem 0;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.2);
    }
    
    .cta-section::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: float 8s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translate(-50%, -50%) rotate(0deg); }
        50% { transform: translate(-50%, -50%) rotate(180deg); }
    }
    
    .action-button {
        background: rgba(255, 255, 255, 0.2);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 50px;
        padding: 1rem 2rem;
        margin: 0.5rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        position: relative;
        z-index: 1;
    }
    
    .action-button:hover {
        background: rgba(255, 255, 255, 0.3);
        border-color: rgba(255, 255, 255, 0.5);
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    }
    
    .feature-highlight {
        background: linear-gradient(135deg, #e3f2fd, #bbdefb);
        border-radius: 20px;
        padding: 3rem 2rem;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
    }
    
    .highlight-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .highlight-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        border-left: 4px solid #2196f3;
    }
    
    .highlight-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12);
    }
    
    .typing-animation {
        overflow: hidden;
        border-right: 3px solid #667eea;
        white-space: nowrap;
        margin: 0 auto;
        letter-spacing: .1em;
        animation: typing 4s steps(40, end), blink-caret .75s step-end infinite;
    }
    
    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: #667eea; }
    }
    
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
    }
    
    h1 {
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }
    
    /* Mobile Optimizations */
    @media (max-width: 768px) {
        .hero-container, .metrics-container, .cta-section {
            padding: 2rem 1rem;
            margin: 1rem 0;
        }
        
        .ai-expertise-grid {
            grid-template-columns: 1fr;
            gap: 1rem;
        }
        
        .expertise-card {
            padding: 1.5rem;
        }
        
        .metrics-grid {
            grid-template-columns: repeat(2, 1fr);
            gap: 1.5rem;
        }
    }

"""

# Apply the professional CSS
st.markdown(PROFESSIONAL_CSS, unsafe_allow_html=True)

# Load animations and images
animations = {}
animation_files = [
    'data-analyisis.json', 'data-engineer.json', 'ai-engineering.json',
    'ai.json', 'deep-learning.json', 'devops.json'
]

for file in animation_files:
    animations[file.split('.')[0]] = load_lottie_local(file)

profile_photo = load_profile_photo()

# Sidebar Navigation - returns page key
page_key = language_selector()

# Main page rendering using page keys
if page_key == "home":
    # Professional Hero Section
    st.markdown(f"""
    
        🤖 AI Engineer & Innovation Catalyst
        
            Transforming Complex Business Challenges into Intelligent AI Solutions
        
        
            From Computer Vision to Generative AI • From NLP to Predictive Analytics • From Research to Production
        
        
            
                🔬 5+ Years Experience
            
            
                💼 50+ Projects Delivered
            
            
                🌍 International Experience
            
        
    
    """, unsafe_allow_html=True)
    
    # AI Expertise Showcase
    st.markdown("## 🚀 AI Expertise Across All Domains")
    
    ai_domains = [
        {
            "icon": "👁️",
            "title": "Computer Vision",
            "description": "Advanced image processing, object detection, medical imaging analysis, and autonomous systems development",
            "metrics": ["15+ Projects", "98%+ Accuracy", "Real-time Processing"],
            "color": "linear-gradient(135deg, #667eea, #764ba2)"
        },
        {
            "icon": "🗣️", 
            "title": "Natural Language Processing",
            "description": "RAG systems, sentiment analysis, chatbots, multilingual processing, and advanced content generation",
            "metrics": ["25+ Projects", "94%+ Accuracy", "Multi-language"],
            "color": "linear-gradient(135deg, #ff6b6b, #ee5a24)"
        },
        {
            "icon": "🎨",
            "title": "Generative AI",
            "description": "Text-to-image generation, AI art creation, synthetic data generation, and creative content automation",
            "metrics": ["12+ Projects", "Enterprise Scale", "Creative Solutions"],
            "color": "linear-gradient(135deg, #51cf66, #40c057)"
        },
        {
            "icon": "📊",
            "title": "Machine Learning",
            "description": "Predictive analytics, recommendation systems, fraud detection, and advanced optimization algorithms",
            "metrics": ["30+ Projects", "92%+ Accuracy", "Business Impact"],
            "color": "linear-gradient(135deg, #f093fb, #f5576c)"
        },
        {
            "icon": "🧠",
            "title": "Deep Learning",
            "description": "Neural networks, transformers, CNNs, RNNs, and custom architecture development for complex problems",
            "metrics": ["35+ Models", "SOTA Results", "Production Ready"],
            "color": "linear-gradient(135deg, #4c6ef5, #364fc7)"
        },
        {
            "icon": "🔬",
            "title": "AI Research",
            "description": "Published research, novel algorithms, experimental AI applications, and cutting-edge innovation",
            "metrics": ["Research Papers", "Novel Approaches", "Innovation Focus"],
            "color": "linear-gradient(135deg, #845ec2, #b197fc)"
        }
    ]
    
    st.markdown('', unsafe_allow_html=True)
    
    for domain in ai_domains:
        metrics_html = ""
        for metric in domain["metrics"]:
            metrics_html += f'{metric}'
        
        st.markdown(f"""
        
            {domain['icon']}
            {domain['title']}
            
                {domain['description']}
            
            
                {metrics_html}
            
        
        """, unsafe_allow_html=True)
    
    st.markdown('', unsafe_allow_html=True)
    
    # Interactive Features Preview
    st.markdown(f"""
    
        🎯 Interactive AI Capabilities
        
            Experience cutting-edge AI solutions through live demonstrations and interactive showcases
        
    
    """, unsafe_allow_html=True)
    
    demo_features = [
        {
            "title": "🧠 Real-time Sentiment Analysis",
            "description": "Advanced emotion detection using state-of-the-art transformer models",
            "action": "Try Live Demo"
        },
        {
            "title": "🔍 Zero-Shot Classification",
            "description": "Classify text into any categories without prior training examples",
            "action": "Explore Feature"
        },
        {
            "title": "☁️ Intelligent Word Clouds",
            "description": "Semantic text visualization with advanced NLP processing",
            "action": "Generate Now"
        },
        {
            "title": "🎨 AI Art Generation",
            "description": "Creative AI applications for generative art and visual content",
            "action": "Create Art"
        }
    ]
    
    st.markdown('', unsafe_allow_html=True)
    
    for feature in demo_features:
        st.markdown(f"""
        
            {feature['title']}
            {feature['description']}
            
                {feature['action']} →
            
        
        """, unsafe_allow_html=True)
    
    st.markdown('', unsafe_allow_html=True)
    
    # Professional Metrics Dashboard
    st.markdown(f"""
    
        📈 Professional Impact Metrics
        
            
                50+
                AI Projects Delivered
                Enterprise & Startup
            
            
                95%
                Average Model Accuracy
                Production Systems
            
            
                $5M+
                Business Value Created
                Cost Savings & Revenue
            
            
                15+
                Technologies Mastered
                AI/ML Stack
            
        
    
    """, unsafe_allow_html=True)
    
    # Quick Navigation
    st.markdown("### 🚀 Explore My Professional Journey")
    nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)
    
    with nav_col1:
        if st.button("🧠 Interactive AI Demos", key="nav_skills", help="Experience live AI demonstrations", use_container_width=True):
            st.session_state.page = "skills"
            st.rerun()
    
    with nav_col2:
        if st.button("🚀 Project Portfolio", key="nav_projects", help="Explore comprehensive AI projects", use_container_width=True):
            st.session_state.page = "projects"
            st.rerun()
    
    with nav_col3:
        if st.button("👨‍💻 Professional Background", key="nav_about", help="Learn about my AI journey", use_container_width=True):
            st.session_state.page = "about"
            st.rerun()
    
    with nav_col4:
        if st.button("📞 Let's Collaborate", key="nav_contact", help="Connect for AI opportunities", use_container_width=True):
            st.session_state.page = "contact"
            st.rerun()
    
    # Professional Call to Action
    st.markdown(f"""
    
        🤝 Ready to Transform Your Business with AI?
        
            I deliver cutting-edge AI solutions that drive real business results - from concept to production scale.
        
        
            Let's discuss how AI can unlock unprecedented growth and innovation for your organization.
        
        
            
                🚀 Start Your AI Transformation
            
            
                📞 Schedule Consultation
            
        
    
    """, unsafe_allow_html=True)
    
    # Testimonial Section
    st.markdown(f"""
    
        👥 What Industry Leaders Say
        
            
                
                    "Karim's AI solutions transformed our document processing workflow, reducing manual work by 85% and improving accuracy significantly."
                
                Sarah Johnson
                CTO, TechCorp International
            
            
                
                    "Working with Karim on our computer vision project was exceptional. His expertise and attention to detail exceeded expectations."
                
                Michael Chen
                Head of Innovation, DataTech Solutions
            
        
    
    """, unsafe_allow_html=True)

elif page_key == "about":
    logging.info("Loading About Page")
    importlib.reload(about)

elif page_key == "projects":
    logging.info("Loading Projects Page")
    importlib.reload(projects)

elif page_key == "skills":
    logging.info("Loading Skills Page")
    importlib.reload(skills)

elif page_key == "contact":
    logging.info("Loading Contact Page")
    importlib.reload(contact)

elif page_key == "resume":
    logging.info("Loading Resume Page")
    importlib.reload(resume)
