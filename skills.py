import os
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
import pandas as pd
import numpy as np

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Enhanced Skills Data with proficiency levels and business impact
skills_data = [
    {
        "category": "🐍 Programming Languages",
        "description": "Mastery across multiple programming paradigms for diverse AI applications",
        "skills": [
            {"name": "Python", "proficiency": 95, "years": 8, "projects": 50, "icon": os.path.join(current_dir, "icons", "python.svg")},
            {"name": "R", "proficiency": 80, "years": 4, "projects": 15, "icon": os.path.join(current_dir, "icons", "R.svg")},
            {"name": "Java", "proficiency": 75, "years": 5, "projects": 12, "icon": os.path.join(current_dir, "icons", "java.svg")},
            {"name": "C++", "proficiency": 70, "years": 3, "projects": 8, "icon": os.path.join(current_dir, "icons", "CPlusPlus.svg")},
            {"name": "SQL", "proficiency": 90, "years": 6, "projects": 35, "icon": os.path.join(current_dir, "icons", "sql-azure.svg")},
            {"name": "JavaScript", "proficiency": 85, "years": 4, "projects": 20, "icon": os.path.join(current_dir, "icons", "javascript.svg")},
        ],
    },
    {
        "category": "🤖 Machine Learning & AI Frameworks",
        "description": "Deep expertise in cutting-edge ML frameworks for production-ready solutions",
        "skills": [
            {"name": "TensorFlow", "proficiency": 92, "years": 5, "projects": 25, "icon": os.path.join(current_dir, "icons", "tensorflow.svg")},
            {"name": "PyTorch", "proficiency": 90, "years": 4, "projects": 22, "icon": os.path.join(current_dir, "icons", "pytorch.svg")},
            {"name": "Scikit-learn", "proficiency": 95, "years": 6, "projects": 40, "icon": os.path.join(current_dir, "icons", "scikit-learn.svg")},
            {"name": "Hugging Face", "proficiency": 88, "years": 3, "projects": 18, "icon": None},
            {"name": "XGBoost", "proficiency": 85, "years": 4, "projects": 15, "icon": os.path.join(current_dir, "icons", "XGBoost.svg")},
            {"name": "Keras", "proficiency": 90, "years": 5, "projects": 20, "icon": os.path.join(current_dir, "icons", "Keras.svg")},
        ],
    },
    {
        "category": "☁️ Cloud & DevOps Technologies",
        "description": "Scalable infrastructure and deployment expertise for enterprise AI solutions",
        "skills": [
            {"name": "AWS", "proficiency": 88, "years": 4, "projects": 20, "icon": os.path.join(current_dir, "icons", "aws.svg")},
            {"name": "Docker", "proficiency": 85, "years": 3, "projects": 25, "icon": os.path.join(current_dir, "icons", "Docker.svg")},
            {"name": "Kubernetes", "proficiency": 80, "years": 2, "projects": 12, "icon": os.path.join(current_dir, "icons", "kubernetes.svg")},
            {"name": "GCP", "proficiency": 82, "years": 3, "projects": 15, "icon": os.path.join(current_dir, "icons", "gcp.svg")},
            {"name": "MLflow", "proficiency": 85, "years": 2, "projects": 10, "icon": os.path.join(current_dir, "icons", "MLflow.svg")},
            {"name": "Apache Airflow", "proficiency": 78, "years": 2, "projects": 8, "icon": os.path.join(current_dir, "icons", "Apache Airflow.svg")},
        ],
    },
    {
        "category": "📊 Data Engineering & Big Data",
        "description": "Robust data pipeline and processing capabilities for large-scale analytics",
        "skills": [
            {"name": "Apache Spark", "proficiency": 85, "years": 3, "projects": 15, "icon": os.path.join(current_dir, "icons", "Apache Spark.svg")},
            {"name": "Apache Kafka", "proficiency": 80, "years": 2, "projects": 10, "icon": os.path.join(current_dir, "icons", "Apache Kafka.svg")},
            {"name": "PostgreSQL", "proficiency": 88, "years": 5, "projects": 30, "icon": os.path.join(current_dir, "icons", "postgresql.svg")},
            {"name": "MongoDB", "proficiency": 82, "years": 3, "projects": 18, "icon": os.path.join(current_dir, "icons", "mongodb.svg")},
            {"name": "Elasticsearch", "proficiency": 75, "years": 2, "projects": 8, "icon": None},
            {"name": "Redis", "proficiency": 80, "years": 3, "projects": 12, "icon": os.path.join(current_dir, "icons", "dbs-redis.svg")},
        ],
    },
]

# Deep Learning Models with business applications
deep_learning_models = {
    "🧠 Natural Language Processing": {
        "models": ["BERT", "GPT-3/4", "Transformer", "LSTM", "RNN"],
        "applications": ["Sentiment Analysis", "Document Processing", "Chatbots", "Content Generation"],
        "business_value": "Automate customer service, analyze feedback, generate content",
        "proficiency": 92
    },
    "👁️ Computer Vision": {
        "models": ["CNN", "ResNet", "EfficientNet", "YOLO", "U-Net"],
        "applications": ["Object Detection", "Image Classification", "Medical Imaging", "Quality Control"],
        "business_value": "Automate visual inspection, medical diagnosis, security systems",
        "proficiency": 88
    },
    "🎯 Generative AI": {
        "models": ["GANs", "VAEs", "Diffusion Models", "StyleGAN"],
        "applications": ["Image Generation", "Data Augmentation", "Creative Content"],
        "business_value": "Create marketing content, augment training data, design automation",
        "proficiency": 85
    },
    "🎵 Audio & Video Processing": {
        "models": ["WaveNet", "ConvLSTM", "3D CNN", "Transformer"],
        "applications": ["Speech Recognition", "Video Analysis", "Audio Generation"],
        "business_value": "Voice interfaces, video analytics, content creation",
        "proficiency": 80
    }
}

# Enhanced styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        font-family: 'Inter', sans-serif;
    }
    
    .skills-hero {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 3rem;
        margin: 2rem 0;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        text-align: center;
    }
    
    .skill-category-card {
        background: linear-gradient(145deg, #ffffff, #f0f0f0);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #667eea;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .skill-category-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    }
    
    .skill-item {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        display: flex;
        align-items: center;
        justify-content: space-between;
        transition: transform 0.2s ease;
    }
    
    .skill-item:hover {
        transform: scale(1.02);
    }
    
    .proficiency-bar {
        background: #e9ecef;
        border-radius: 10px;
        height: 8px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .proficiency-fill {
        height: 100%;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 10px;
        transition: width 1s ease;
    }
    
    .model-showcase {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
    }
    
    .interactive-demo {
        background: #f8f9fa;
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        border: 2px solid #e9ecef;
    }
    
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        margin: 1rem;
    }
    
    .metric-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #667eea;
        margin: 0;
    }
    
    .metric-label {
        color: #666;
        font-size: 0.9rem;
        margin: 0;
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
    
    .tech-badge {
        background: #667eea;
        color: white;
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 0.8em;
        margin: 2px;
        display: inline-block;
    }
    
    .business-impact {
        background: linear-gradient(135deg, #00b894, #00a085);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="skills-hero">
    <h1>🚀 Technical Expertise & Innovation Arsenal</h1>
    <p style="font-size: 1.3rem; color: #555; margin-top: 2rem;">
        A comprehensive toolkit of cutting-edge technologies and proven methodologies 
        for delivering impactful AI solutions
    </p>
</div>
""", unsafe_allow_html=True)

# Skills Overview Metrics
st.markdown("## 📊 Skills at a Glance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3 class="metric-number">8+</h3>
        <p class="metric-label">Years of Experience</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3 class="metric-number">50+</h3>
        <p class="metric-label">Projects Completed</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3 class="metric-number">15+</h3>
        <p class="metric-label">Technologies Mastered</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h3 class="metric-number">92%</h3>
        <p class="metric-label">Average Proficiency</p>
    </div>
    """, unsafe_allow_html=True)

# Interactive Skills Radar Chart
st.markdown("## 🎯 Skills Proficiency Radar")

categories = [skill["category"].split(" ", 1)[1] for skill in skills_data]  # Remove emoji
avg_proficiencies = []

for category in skills_data:
    avg_prof = sum(skill["proficiency"] for skill in category["skills"]) / len(category["skills"])
    avg_proficiencies.append(avg_prof)

fig_radar = go.Figure()

fig_radar.add_trace(go.Scatterpolar(
    r=avg_proficiencies,
    theta=categories,
    fill='toself',
    name='Proficiency Level',
    line_color='#667eea'
))

fig_radar.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )),
    showlegend=False,
    title="Technical Skills Proficiency Overview"
)

st.plotly_chart(fig_radar, use_container_width=True)

# Detailed Skills Breakdown
st.markdown("## 🛠️ Detailed Technical Skills")

for category in skills_data:
    st.markdown(f"""
    <div class="skill-category-card">
        <h3>{category['category']}</h3>
        <p style="color: #666; margin-bottom: 2rem;">{category['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create columns for skills in this category
    cols = st.columns(2)
    
    for i, skill in enumerate(category["skills"]):
        col = cols[i % 2]
        
        with col:
            # Skill proficiency bar
            proficiency_width = skill["proficiency"]
            
            st.markdown(f"""
            <div class="skill-item">
                <div style="flex: 1;">
                    <h4 style="margin: 0; color: #2c3e50;">{skill['name']}</h4>
                    <div class="proficiency-bar">
                        <div class="proficiency-fill" style="width: {proficiency_width}%;"></div>
                    </div>
                    <small style="color: #666;">
                        {skill['proficiency']}% proficiency • {skill['years']} years • {skill['projects']} projects
                    </small>
                </div>
            </div>
            """, unsafe_allow_html=True)

# Deep Learning Models Showcase
st.markdown("## 🧠 Deep Learning & AI Models Expertise")

for model_category, details in deep_learning_models.items():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="model-showcase">
            <h3>{model_category}</h3>
            <p style="margin: 1rem 0;">{details['business_value']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Models badges
        models_html = ""
        for model in details["models"]:
            models_html += f'<span class="tech-badge">{model}</span> '
        st.markdown(models_html, unsafe_allow_html=True)
        
        # Applications
        st.markdown("**Key Applications:**")
        for app in details["applications"]:
            st.markdown(f"• {app}")
    
    with col2:
        # Proficiency gauge
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = details["proficiency"],
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Proficiency"},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "#667eea"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 80], 'color': "gray"}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90}}))
        
        fig_gauge.update_layout(height=200, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig_gauge, use_container_width=True)

# Interactive Skills Comparison
st.markdown("## 📈 Skills Evolution & Comparison")

# Create a comprehensive skills dataframe
all_skills = []
for category in skills_data:
    for skill in category["skills"]:
        all_skills.append({
            "Skill": skill["name"],
            "Category": category["category"].split(" ", 1)[1],
            "Proficiency": skill["proficiency"],
            "Years": skill["years"],
            "Projects": skill["projects"]
        })

df_skills = pd.DataFrame(all_skills)

# Interactive scatter plot
fig_scatter = px.scatter(
    df_skills, 
    x="Years", 
    y="Proficiency", 
    size="Projects",
    color="Category",
    hover_name="Skill",
    title="Skills Proficiency vs Experience",
    size_max=20
)

fig_scatter.update_layout(height=500)
st.plotly_chart(fig_scatter, use_container_width=True)

# Business Impact Section
st.markdown("""
<div class="business-impact">
    <h2 style="color: white; margin-bottom: 2rem;">💼 How These Skills Drive Business Value</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
        <div>
            <h4>🚀 Faster Time-to-Market</h4>
            <p>My expertise in cloud technologies and MLOps enables rapid deployment of AI solutions, reducing development cycles by 40-60%.</p>
        </div>
        <div>
            <h4>💰 Cost Optimization</h4>
            <p>Deep understanding of scalable architectures and efficient algorithms helps optimize infrastructure costs while maintaining performance.</p>
        </div>
        <div>
            <h4>🎯 Accurate Predictions</h4>
            <p>Advanced ML and DL expertise consistently delivers models with 85-95% accuracy, directly impacting business KPIs.</p>
        </div>
        <div>
            <h4>🔧 Robust Solutions</h4>
            <p>Full-stack capabilities ensure end-to-end solution delivery, from data ingestion to user-facing applications.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Learning & Growth Section
st.markdown("## 📚 Continuous Learning & Innovation")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="interactive-demo">
        <h3>🔬 Currently Exploring</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li>🤖 <strong>Large Language Models (LLMs)</strong> - Advanced prompt engineering and fine-tuning</li>
            <li>🧠 <strong>Multimodal AI</strong> - Vision-language models and cross-modal understanding</li>
            <li>⚡ <strong>Edge AI</strong> - Optimizing models for mobile and IoT deployment</li>
            <li>🔐 <strong>AI Safety & Ethics</strong> - Responsible AI development and bias mitigation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="interactive-demo">
        <h3>🎯 Learning Methodology</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li>📖 <strong>Research Papers</strong> - Weekly review of latest AI research</li>
            <li>🛠️ <strong>Hands-on Projects</strong> - Implementing new techniques in real projects</li>
            <li>🤝 <strong>Community Engagement</strong> - Contributing to open-source projects</li>
            <li>🎓 <strong>Continuous Education</strong> - Online courses and certifications</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Call to Action
st.markdown("""
<div class="skills-hero">
    <h2>🤝 Ready to Leverage These Skills for Your Success?</h2>
    <p style="font-size: 1.2rem; color: #555; margin-top: 2rem;">
        These technical capabilities are just tools - the real value comes from applying them strategically 
        to solve your specific business challenges and drive measurable results.
    </p>
    <p style="font-size: 1.1rem; color: #666; margin-top: 1rem;">
        Let's discuss how my expertise can accelerate your AI initiatives and create competitive advantages.
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: #666; margin-top: 2rem;'>© 2024 Karim Osman - Transforming Technical Expertise into Business Success</p>", unsafe_allow_html=True)
