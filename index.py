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

# Configure the page
st.set_page_config(page_title="Karim Osman - AI Engineer Portfolio", layout="wide", initial_sidebar_state="expanded")
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
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation with enhanced design
st.sidebar.markdown("### 🚀 Navigation")
page = st.sidebar.radio("", ["🏠 Home", "👨‍💻 About", "🚀 Projects", "⚡ Skills", "📞 Contact", "📄 Resume"])

# Interactive AI Chat Bot Section
def ai_chat_interface():
    st.markdown("### 🤖 Ask Me Anything - Interactive AI Assistant")
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Predefined questions for quick interaction
    quick_questions = [
        "What's your strongest AI skill?",
        "Tell me about your most impactful project",
        "How do you approach problem-solving?",
        "What makes you different from other AI engineers?",
        "What's your vision for AI in the next 5 years?"
    ]
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_question = st.text_input("Ask me about my experience, skills, or approach to AI:", placeholder="Type your question here...")
    
    with col2:
        if st.button("🎲 Random Question"):
            user_question = random.choice(quick_questions)
            st.session_state.random_question = user_question
    
    # Quick question buttons
    st.markdown("**Quick Questions:**")
    cols = st.columns(len(quick_questions))
    for i, question in enumerate(quick_questions):
        if cols[i].button(f"❓ {question[:20]}...", key=f"quick_{i}"):
            user_question = question
    
    # AI responses based on questions
    ai_responses = {
        "What's your strongest AI skill?": "My strongest skill is bridging the gap between complex AI theory and practical business solutions. I excel at taking cutting-edge research and transforming it into scalable, production-ready systems that deliver measurable value.",
        
        "Tell me about your most impactful project": "At Bakerhughes, I developed a 'RAG as a service' platform that democratized AI access across the organization. This project increased AI adoption by 300% and reduced development time for new AI applications by 60%.",
        
        "How do you approach problem-solving?": "I follow a three-step approach: First, I deeply understand the business context and constraints. Second, I prototype rapidly to validate assumptions. Third, I iterate based on real-world feedback, always keeping scalability and maintainability in mind.",
        
        "What makes you different from other AI engineers?": "I combine technical depth with business acumen. I don't just build models; I create AI solutions that align with strategic objectives. My proactive approach means I often identify opportunities before they become obvious needs.",
        
        "What's your vision for AI in the next 5 years?": "I see AI becoming truly democratized - where non-technical users can leverage sophisticated AI capabilities through intuitive interfaces. I'm particularly excited about AI agents that can understand context and intent, making technology more human-centric."
    }
    
    if user_question:
        # Simulate typing effect
        with st.spinner("🤔 Thinking..."):
            time.sleep(1)
        
        response = ai_responses.get(user_question, 
            f"That's a great question about '{user_question}'. Based on my experience in AI engineering, I'd approach this by leveraging my expertise in machine learning, deep learning, and practical implementation. I believe in creating solutions that are not just technically sound but also deliver real business value.")
        
        st.markdown(f"**🤖 Karim's AI Assistant:** {response}")
        
        # Add to chat history
        st.session_state.chat_history.append({"question": user_question, "answer": response})

# Enhanced metrics display
def show_impact_metrics():
    st.markdown("### 📊 Impact Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card pulse">
            <h3 style="color: #e74c3c; margin: 0;">20%</h3>
            <p style="margin: 0;">Performance Improvement</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card pulse">
            <h3 style="color: #27ae60; margin: 0;">30%</h3>
            <p style="margin: 0;">Workflow Efficiency</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card pulse">
            <h3 style="color: #3498db; margin: 0;">25%</h3>
            <p style="margin: 0;">Data Processing Speed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card pulse">
            <h3 style="color: #f39c12; margin: 0;">5+</h3>
            <p style="margin: 0;">Years Experience</p>
        </div>
        """, unsafe_allow_html=True)

# Proactive approach showcase
def proactive_showcase():
    st.markdown("""
    <div class="proactive-section">
        <h2 style="color: white; margin-bottom: 2rem;">🚀 My Proactive Approach</h2>
        <p style="font-size: 1.2rem; margin-bottom: 2rem;">
            I don't just respond to problems - I anticipate them. Here's how I would revolutionize your company's AI capabilities:
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="interactive-card">
            <h3>🎯 Intelligent Candidate Assistant</h3>
            <p>An AI-powered system that analyzes applications beyond keywords, providing personalized feedback and creating an exceptional candidate experience.</p>
            <ul>
                <li>Semantic analysis of CVs and proposals</li>
                <li>Personalized feedback generation</li>
                <li>Interactive chatbot for candidates</li>
                <li>Hidden talent identification</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="interactive-card">
            <h3>⚡ Technical Implementation</h3>
            <p>Leveraging cutting-edge technologies to create scalable, robust solutions:</p>
            <ul>
                <li>Advanced NLP with Hugging Face models</li>
                <li>Vector databases for semantic search</li>
                <li>Cloud-native architecture (AWS/GCP)</li>
                <li>Real-time interactive interfaces</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Main page rendering
if page == "🏠 Home":
    # Hero section with typing effect
    st.markdown("""
    <div class="hero-section">
        <h1 class="typing-effect">Welcome to My AI Universe! 🌟</h1>
        <p style="text-align: center; font-size: 1.3rem; color: #555; margin-top: 2rem;">
            I'm <strong>Karim Osman</strong>, an AI Engineer who transforms complex challenges into intelligent solutions
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
    st.markdown("### 🎯 My Expertise Areas")
    
    col1, col2, col3 = st.columns(3)
    
    expertise_areas = [
        ("🤖 Machine Learning", "Building predictive models that drive business decisions", data_analysis_animation),
        ("🔧 AI Engineering", "Deploying scalable AI solutions in production", ai_engineering_animation),
        ("📊 Data Science", "Extracting insights from complex datasets", ai_animation),
        ("🧠 Deep Learning", "Creating neural networks for complex problems", deep_learning_animation),
        ("☁️ Cloud & DevOps", "Scalable infrastructure and deployment", dev_ops_animation),
        ("💡 Innovation", "Proactive problem-solving and future-thinking", data_engineer_animation)
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

elif page == "👨‍💻 About":
    logging.info("Loading About Page")
    importlib.reload(about)

elif page == "🚀 Projects":
    logging.info("Loading Projects Page")
    importlib.reload(projects)

elif page == "⚡ Skills":
    logging.info("Loading Skills Page")
    importlib.reload(skills)

elif page == "📞 Contact":
    logging.info("Loading Contact Page")
    importlib.reload(contact)

elif page == "📄 Resume":
    logging.info("Loading Resume Page")
    importlib.reload(resume)
