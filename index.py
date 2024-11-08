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

# --- Streamlit Config ---
st.set_page_config(page_title="Karim Osman - ML Engineer Portfolio", layout="wide")
logging.basicConfig(level=logging.INFO)

# --- Cache and Load Functions ---
@st.cache_resource
def load_lottie_local(filepath: str):
    """Load Lottie animation from local JSON file."""
    with open(filepath, "r") as f:
        return json.load(f)

@st.cache_resource
def load_profile_photo():
    """Load and cache profile photo."""
    return Image.open("profile-photo.jpg")

# Load Animations and Profile Photo
data_analysis_animation = load_lottie_local('data-analyisis.json')
data_engineer_animation = load_lottie_local('data-engineer.json')
ai_engineering_animation = load_lottie_local('ai-engineering.json')
ai_animation = load_lottie_local('ai.json')
deep_learning_animation = load_lottie_local('devops.json')
dev_ops_animation = load_lottie_local('deep-learning.json')
profile_photo = load_profile_photo()

# --- Helper Functions ---
def load_page(module_name):
    try:
        module = importlib.import_module(module_name)
        importlib.reload(module)
    except AttributeError as e:
        st.error(f"Error loading {module_name}: {e}")
    except ImportError as e:
        st.error(f"Module {module_name} not found: {e}")

def set_style():
    st.markdown("""
    <style>
        body { font-family: 'Helvetica Neue', sans-serif; }
        .main { background-color: #f5f5f5; padding: 2rem; }
        h1, h2, h4 { font-weight: 700; color: #003366; }
        h1 { margin-bottom: 20px; font-size: 2.5rem; }
        h2 { color: #007ACC; margin-bottom: 10px; }
        .profile-photo { border-radius: 50%; width: 150px; height: 150px; margin: 0 auto;
                         box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2); border: 3px solid #007ACC; }
        .footer { margin-top: 50px; text-align: center; color: #999; font-size: 0.9rem; }
        .button { background-color: #007ACC; color: white; padding: 10px 20px; font-size: 16px;
                  cursor: pointer; border-radius: 5px; }
        .button:hover { background-color: #005999; }
    </style>
    """, unsafe_allow_html=True)

set_style()

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Skills", "Contact", "Resume"])

# --- Home Page Content ---
if page == "Home":
    st.title("🌍 Welcome to My Portfolio!")
    st.write("I’m **Karim Osman**, a passionate **Machine Learning Engineer** dedicated to solving real-world challenges through data-driven models and algorithms.")
    
    # Display Profile Photo
    st.image(profile_photo, caption="Karim Osman", use_column_width=False, width=150)

    # Animations
    st.markdown("<h2>Explore My Expertise</h2>", unsafe_allow_html=True)
    cols = st.columns(6)
    animations = [
        (data_analysis_animation, "Machine Learning Engineer"),
        (data_engineer_animation, "Data Engineer"),
        (ai_engineering_animation, "Data Scientist"),
        (ai_animation, "AI Engineer"),
        (deep_learning_animation, "Deep Learning Engineer"),
        (dev_ops_animation, "DevOps Engineer")
    ]

    for col, (animation, title) in zip(cols, animations):
        with col:
            st_lottie(animation, height=80, width=80, key=title)
            st.markdown(f"<h4>{title}</h4>", unsafe_allow_html=True)

    # Role Descriptions and Business Scenarios
    role_descriptions = {
        "Machine Learning Engineer": ("I specialize in predictive models, analyzing datasets for strategic decisions. Tools include TensorFlow, Scikit-learn."),
        "Data Engineer": ("I design data pipelines, optimize data flow, and support analytics using Apache Kafka, Spark, SQL/NoSQL databases."),
        "Data Scientist": ("I turn data into strategic insights with statistical analysis and machine learning, using Tableau, Matplotlib."),
        "AI Engineer": ("I develop AI models using frameworks like Keras and PyTorch, focusing on user-centered applications."),
        "Deep Learning Engineer": ("I design architectures for tasks like image recognition, leveraging neural networks to solve complex problems."),
        "DevOps Engineer": ("I bridge development and operations with CI/CD practices using Docker, Kubernetes for scalable solutions."),
    }

    for role, description in role_descriptions.items():
        st.markdown(f"<h4>{role}</h4>", unsafe_allow_html=True)
        st.write(description)

    # Footer
    st.markdown("<p class='footer'>© 2024 Karim Osman</p>", unsafe_allow_html=True)

elif page == "Skills":
    logging.info("Loading Skills Page")
    load_page("skills")

elif page == "Projects":
    logging.info("Loading Projects Page")
    load_page("projects")

elif page == "About":
    logging.info("Loading About Page")
    load_page("about")

elif page == "Contact":
    logging.info("Loading Contact Page")
    load_page("contact")

elif page == "Resume":
    logging.info("Loading Resume Page")
    load_page("resume")
