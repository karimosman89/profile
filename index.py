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
from app_utils import tr, language_selector, get_browser_lang

if 'lang' not in st.session_state:
    st.session_state.lang = get_browser_lang()
    
# Configure the page
st.set_page_config(
    page_title="Karim Osman - AI Engineer", 
    layout="wide", 
    initial_sidebar_state="expanded",
    page_icon="🤖",
    menu_items={
        'Get Help': 'mailto:karim.osman@example.com',
        'Report a bug': 'mailto:karim.osman@example.com',
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

# Load AI showcase images
@st.cache_resource
def load_ai_images():
    """Load AI showcase images"""
    images = {}
    image_files = [
        'assets/ai_brain_network.png',
        'assets/computer_vision_demo.png', 
        'assets/nlp_processing.png',
        'assets/generative_ai_art.png'
    ]
    
    for file in image_files:
        try:
            images[file.split('/')[-1].split('.')[0]] = Image.open(file)
        except FileNotFoundError:
            images[file.split('/')[-1].split('.')[0]] = None
    
    return images

# Load Lottie animations (with error handling)
animations = {}
animation_files = [
    'data-analyisis.json', 'data-engineer.json', 'ai-engineering.json',
    'ai.json', 'deep-learning.json', 'devops.json'
]

for file in animation_files:
    animations[file.split('.')[0]] = load_lottie_local(file)

profile_photo = load_profile_photo()
ai_images = load_ai_images()

# Enhanced styles with modern design and better responsiveness
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        font-family: 'Inter', sans-serif;
    }
    
    .hero-section {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 3rem 2rem;
        margin: 2rem 0;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2, #667eea);
        background-size: 200% 100%;
        animation: gradient-shift 3s ease-in-out infinite;
    }
    
    @keyframes gradient-shift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .ai-showcase-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .ai-field-card {
        background: linear-gradient(145deg, #ffffff, #f0f0f0);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        transition: all 0.4s ease;
        cursor: pointer;
        border: 1px solid rgba(102, 126, 234, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .ai-field-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .ai-field-card:hover::before {
        left: 100%;
    }
    
    .ai-field-card:hover {
        transform: translateY(-10px) scale(1.03);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
        border-color: rgba(102, 126, 234, 0.3);
    }
    
    .ai-field-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        background: linear-gradient(145deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }
    
    .interactive-demo-section {
        background: linear-gradient(135deg, #e3f2fd, #bbdefb);
        border-radius: 20px;
        padding: 3rem 2rem;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        position: relative;
    }
    
    .demo-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        border-left: 5px solid #2196f3;
    }
    
    .demo-card:hover {
        transform: translateX(10px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
    }
    
    .stats-showcase {
        background: linear-gradient(135deg, #1a1a1a, #2d2d2d);
        color: white;
        border-radius: 20px;
        padding: 3rem 2rem;
        margin: 2rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .stats-showcase::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(102, 126, 234, 0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
    }
    
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .stat-item {
        text-align: center;
        margin: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(145deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: block;
        margin-bottom: 0.5rem;
    }
    
    .creative-showcase {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        border-radius: 20px;
        padding: 3rem 2rem;
        margin: 2rem 0;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .creative-showcase::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: float 6s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translate(-50%, -50%) rotate(0deg); }
        50% { transform: translate(-50%, -50%) rotate(180deg); }
    }
    
    .ai-capability-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .capability-card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .capability-card:hover {
        background: white;
        border-color: rgba(102, 126, 234, 0.3);
        transform: translateY(-5px);
    }
    
    .typing-effect {
        overflow: hidden;
        border-right: .15em solid #667eea;
        white-space: nowrap;
        margin: 0 auto;
        letter-spacing: .05em;
        animation: typing 3.5s steps(40, end), blink-caret .75s step-end infinite;
    }
    
    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: #667eea; }
    }
    
    .quick-action-btn {
        background: linear-gradient(145deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 1.5rem;
        margin: 0.5rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .quick-action-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    .ai-image-showcase {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .ai-image-showcase:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    }
    
    h1 {
        font-size: clamp(2rem, 5vw, 3.5rem);
        font-weight: 800;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }
    
    /* Responsive design improvements */
    @media (max-width: 768px) {
        .hero-section {
            padding: 2rem 1rem;
            margin: 1rem 0;
        }
        
        .ai-showcase-grid {
            grid-template-columns: 1fr;
            gap: 1rem;
        }
        
        .ai-field-card {
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation - returns page key ("home", "about", etc.)
page_key = language_selector()

# Main page rendering using page keys
if page_key == "home":
    # Hero section with enhanced typing effect
    st.markdown(f"""
    <div class="hero-section">
        <h1 class="typing-effect">🤖 AI Engineer & Innovation Catalyst</h1>
        <p style="text-align: center; font-size: 1.3rem; color: #555; margin-top: 2rem;">
            Transforming Complex Challenges into Intelligent Solutions Across All AI Domains
        </p>
        <p style="text-align: center; font-size: 1.1rem; color: #666; margin-top: 1rem;">
            From Computer Vision to Generative AI • From NLP to Predictive Analytics • From Research to Production
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # AI Fields Showcase
    st.markdown("## 🚀 AI Expertise Across All Domains")
    
    ai_fields = [
        {
            "icon": "👁️",
            "title": "Computer Vision",
            "description": "Real-time object detection, medical imaging, facial recognition, autonomous systems",
            "projects": "15+ Projects",
            "accuracy": "95%+ Accuracy",
            "image": "computer_vision_demo"
        },
        {
            "icon": "🗣️", 
            "title": "Natural Language Processing",
            "description": "RAG systems, sentiment analysis, chatbots, multilingual processing, content generation",
            "projects": "20+ Projects",
            "accuracy": "92%+ Accuracy",
            "image": "nlp_processing"
        },
        {
            "icon": "🎨",
            "title": "Generative AI",
            "description": "Text-to-image, AI art, synthetic data, creative content, style transfer",
            "projects": "10+ Projects", 
            "accuracy": "High Quality",
            "image": "generative_ai_art"
        },
        {
            "icon": "📊",
            "title": "Machine Learning",
            "description": "Predictive analytics, recommendation systems, fraud detection, optimization",
            "projects": "25+ Projects",
            "accuracy": "89%+ Accuracy",
            "image": "ai_brain_network"
        },
        {
            "icon": "🤖",
            "title": "Deep Learning",
            "description": "Neural networks, transformers, CNNs, RNNs, custom architectures",
            "projects": "30+ Models",
            "accuracy": "SOTA Results",
            "image": "ai_brain_network"
        },
        {
            "icon": "🔬",
            "title": "AI Research",
            "description": "Published papers, novel algorithms, experimental AI, cutting-edge research",
            "projects": "5+ Papers",
            "accuracy": "Peer Reviewed",
            "image": "ai_brain_network"
        }
    ]
    
    st.markdown('<div class="ai-showcase-grid">', unsafe_allow_html=True)
    
    for field in ai_fields:
        # Display AI field image if available
        field_image = ""
        if field["image"] in ai_images and ai_images[field["image"]] is not None:
            # Convert image to base64 for embedding
            import io
            img_buffer = io.BytesIO()
            ai_images[field["image"]].save(img_buffer, format='PNG')
            img_str = base64.b64encode(img_buffer.getvalue()).decode()
            field_image = f'<img src="data:image/png;base64,{img_str}" class="ai-image-showcase">'
        
        st.markdown(f"""
        <div class="ai-field-card">
            <div class="ai-field-icon">{field['icon']}</div>
            <h3 style="color: #333; margin-bottom: 1rem; text-align: center;">{field['title']}</h3>
            {field_image}
            <p style="color: #666; line-height: 1.6; margin-bottom: 1.5rem; text-align: center;">
                {field['description']}
            </p>
            <div style="display: flex; justify-content: space-between; margin-top: 1rem;">
                <span style="background: #e3f2fd; color: #1976d2; padding: 0.25rem 0.75rem; border-radius: 15px; font-size: 0.8rem;">
                    {field['projects']}
                </span>
                <span style="background: #e8f5e8; color: #2e7d32; padding: 0.25rem 0.75rem; border-radius: 15px; font-size: 0.8rem;">
                    {field['accuracy']}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive AI Capabilities Demo
    st.markdown(f"""
    <div class="interactive-demo-section">
        <h2 style="color: #1565c0; text-align: center; margin-bottom: 2rem;">🎯 Live AI Capabilities</h2>
        <p style="text-align: center; font-size: 1.1rem; color: #333; margin-bottom: 2rem;">
            Experience my AI expertise through interactive demonstrations
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    demo_capabilities = [
        {
            "title": "🧠 Sentiment Analysis Engine",
            "description": "Real-time emotion detection in text using state-of-the-art transformers",
            "demo_text": "Try it with any text input"
        },
        {
            "title": "🔍 Zero-Shot Classification",
            "description": "Classify text into any categories without prior training",
            "demo_text": "Dynamic category classification"
        },
        {
            "title": "☁️ Word Cloud Generator", 
            "description": "Intelligent text visualization with semantic analysis",
            "demo_text": "Visual text insights"
        },
        {
            "title": "🎨 AI Art Concepts",
            "description": "Creative AI applications and generative art examples",
            "demo_text": "Explore creative AI"
        }
    ]
    
    for demo in demo_capabilities:
        st.markdown(f"""
        <div class="demo-card">
            <h4 style="color: #1976d2; margin-bottom: 1rem;">{demo['title']}</h4>
            <p style="color: #666; margin-bottom: 1rem;">{demo['description']}</p>
            <button class="quick-action-btn" onclick="alert('Navigate to Skills page to try this demo!')">
                {demo['demo_text']} →
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    # Performance Statistics
    st.markdown(f"""
    <div class="stats-showcase">
        <h2 style="text-align: center; margin-bottom: 2rem; position: relative; z-index: 1;">📈 Performance Metrics</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; position: relative; z-index: 1;">
            <div class="stat-item">
                <span class="stat-number">50+</span>
                <p style="margin: 0; opacity: 0.9;">AI Projects Delivered</p>
            </div>
            <div class="stat-item">
                <span class="stat-number">95%</span>
                <p style="margin: 0; opacity: 0.9;">Average Model Accuracy</p>
            </div>
            <div class="stat-item">
                <span class="stat-number">$10M+</span>
                <p style="margin: 0; opacity: 0.9;">Business Value Created</p>
            </div>
            <div class="stat-item">
                <span class="stat-number">100+</span>
                <p style="margin: 0; opacity: 0.9;">Enterprise Clients</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Creative AI Showcase
    st.markdown(f"""
    <div class="creative-showcase">
        <h2 style="margin-bottom: 2rem; position: relative; z-index: 1;">🎨 Creative AI Innovation</h2>
        <p style="font-size: 1.2rem; margin-bottom: 2rem; position: relative; z-index: 1;">
            Pushing the boundaries of what's possible with artificial intelligence
        </p>
        <div class="ai-capability-grid" style="position: relative; z-index: 1;">
            <div class="capability-card">
                <h4 style="color: #333;">🖼️ Generative Art</h4>
                <p style="color: #666; font-size: 0.9rem;">Text-to-image generation with custom styles</p>
            </div>
            <div class="capability-card">
                <h4 style="color: #333;">🎵 AI Music</h4>
                <p style="color: #666; font-size: 0.9rem;">Intelligent composition and arrangement</p>
            </div>
            <div class="capability-card">
                <h4 style="color: #333;">📝 Content Creation</h4>
                <p style="color: #666; font-size: 0.9rem;">Automated writing with brand voice</p>
            </div>
            <div class="capability-card">
                <h4 style="color: #333;">🔒 Synthetic Data</h4>
                <p style="color: #666; font-size: 0.9rem;">Privacy-preserving data generation</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick navigation buttons
    st.markdown("### 🚀 Explore My AI Universe")
    nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)
    
    with nav_col1:
        if st.button("🧠 Interactive AI Demos", key="nav_skills", help="Experience live AI demonstrations"):
            st.session_state.page = "skills"
            st.rerun()
    
    with nav_col2:
        if st.button("🚀 Project Portfolio", key="nav_projects", help="Explore comprehensive AI projects"):
            st.session_state.page = "projects"
            st.rerun()
    
    with nav_col3:
        if st.button("👨‍💻 My AI Journey", key="nav_about", help="Learn about my path in AI"):
            st.session_state.page = "about"
            st.rerun()
    
    with nav_col4:
        if st.button("📞 Let's Collaborate", key="nav_contact", help="Connect for AI opportunities"):
            st.session_state.page = "contact"
            st.rerun()
    
    # Call to Action
    st.markdown(f"""
    <div class="hero-section">
        <h2>🤝 Ready to Transform Your Business with AI?</h2>
        <p style="font-size: 1.2rem; color: #555; margin-top: 2rem;">
            I bring cutting-edge AI solutions across all domains - from research to production, from concept to scale.
        </p>
        <p style="font-size: 1.1rem; color: #666; margin-top: 1rem;">
            Let's discuss how AI can drive unprecedented growth and innovation for your organization.
        </p>
        <div style="margin-top: 2rem;">
            <button class="quick-action-btn" onclick="alert('Navigate to Contact page to get in touch!')">
                🚀 Start Your AI Transformation
            </button>
        </div>
    </div>
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

