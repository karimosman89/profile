import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie
import plotly.graph_objects as go
import logging
import importlib

# Page configuration
st.set_page_config(page_title="Karim Osman - ML Engineer Portfolio", layout="wide")
logging.basicConfig(level=logging.INFO)

# Cache function to load animations
@st.cache_resource
def load_lottie_local(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Cache function to load profile photo
@st.cache_resource
def load_profile_photo():
    return Image.open("profile-photo.jpg")

# Load assets
data_analysis_animation = load_lottie_local('data-analyisis.json')
data_engineer_animation = load_lottie_local('data-engineer.json')
ai_engineering_animation = load_lottie_local('ai-engineering.json')
ai_animation = load_lottie_local('ai.json')
deep_learning_animation = load_lottie_local('deep-learning.json')
dev_ops_animation = load_lottie_local('devops.json')
profile_photo = load_profile_photo()

# Style configuration
def set_style():
    st.markdown("""
    <style>
        /* General styling */
        body {
            font-family: 'Helvetica Neue', sans-serif;
        }
        .main {
            background-color: #f5f5f5;
            padding: 2rem;
        }
        h1, h2, h4 {
            font-weight: 700;
            color: #003366;
        }
        h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
        }
        h2 {
            color: #007ACC;
            margin-bottom: 10px;
        }
        
        /* Profile photo styling */
        .profile-photo {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            border: 4px solid #007ACC;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
            animation: float 3s ease-in-out infinite;
            margin: 20px auto;
            display: block;
        }

        /* Footer styling */
        .footer {
            margin-top: 50px;
            text-align: center;
            color: #999;
            font-size: 0.9rem;
        }

        /* Button styling */
        .button {
            background-color: #007ACC;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }
        .button:hover {
            background-color: #005999;
        }

        /* Animation for profile photo */
        @keyframes float {
            0% { transform: translatey(0px); }
            50% { transform: translatey(-8px); }
            100% { transform: translatey(0px); }
        }
    </style>
    """, unsafe_allow_html=True)

set_style()

# Title and Introduction
st.title("🌍 Welcome to My Portfolio!")
st.write("I’m **Karim Osman**, a passionate **Machine Learning Engineer** dedicated to solving real-world challenges through data-driven models and algorithms.")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Skills", "Contact", "Resume"])

# Load modules dynamically
def load_page(module_name):
    try:
        module = importlib.import_module(module_name)
    except ImportError as e:
        st.error(f"Module {module_name} not found: {e}")

# Home Page Content
if page == "Home":
    # Profile Photo
    st.image(profile_photo, caption="Karim Osman", use_column_width=False, width=120)

    # Animations and titles for expertise areas
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    animations = [
        (data_analysis_animation, "Machine Learning Engineer"),
        (data_engineer_animation, "Data Engineer"),
        (ai_engineering_animation, "Data Scientist"),
        (ai_animation, "AI Engineer"),
        (deep_learning_animation, "Deep Learning Engineer"),
        (dev_ops_animation, "DevOps Engineer")
    ]
    for col, (animation, title) in zip([col1, col2, col3, col4, col5, col6], animations):
        with col:
            st_lottie(animation, height=80, width=80, key=title)
            st.markdown(f"<h4>{title}</h4>", unsafe_allow_html=True)

    # Role Descriptions and Business Scenarios
    role_descriptions = {
        "Machine Learning Engineer": "Description for Machine Learning Engineer...",
        "Data Engineer": "Description for Data Engineer...",
        "Data Scientist": "Description for Data Scientist...",
        "AI Engineer": "Description for AI Engineer...",
        "Deep Learning Engineer": "Description for Deep Learning Engineer...",
        "DevOps Engineer": "Description for DevOps Engineer...",
    }
    for role, description in role_descriptions.items():
        st.markdown(f"<h4>{role}</h4>", unsafe_allow_html=True)
        st.write(description)
        st.markdown("---")

    st.markdown("<p class='footer'>© 2024 Karim Osman</p>", unsafe_allow_html=True)

# Other Pages (Skills, Projects, About, Contact, Resume)
elif page == "Skills":
    logging.info("Loading Skills Page")
    importlib.reload(importlib.import_module("skills"))

elif page == "Projects":
    logging.info("Loading Projects Page")
    importlib.reload(importlib.import_module("projects"))

elif page == "About":
    logging.info("Loading About Page")
    importlib.reload(importlib.import_module("about"))

elif page == "Contact":
    logging.info("Loading Contact Page")
    importlib.reload(importlib.import_module("contact"))

elif page == "Resume":
    logging.info("Loading Resume Page")
    importlib.reload(importlib.import_module("resume"))
