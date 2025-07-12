import os
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
import pandas as pd
import numpy as np
from utils import tr 

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Enhanced Skills Data with proficiency levels and business impact
skills_data = [
    {
        "category": tr("SKILLS_PROGRAMMING_LANGUAGES_CATEGORY"),
        "description": tr("SKILLS_PROGRAMMING_LANGUAGES_DESC"),
        "skills": [
            {"name": "Python", "proficiency": 95, "years": 8, "projects": 50, "icon": os.path.join(current_dir, "icons", "python.svg")},
            {"name": "R", "proficiency": 80, "years": 4, "projects": 15, "icon": os.path.join(current_dir, "icons", "R.svg")},
            {"name": "Java", "proficiency": 75, "years": 5, "projects": 12, "icon": os.path.join(current_dir, "icons", "java.svg")},
            {"name": "C++", "proficiency": 70, "years": 3, "projects": 8, "icon": os.path.join(current_dir, "icons", "CPlusPlus.svg")},
            {"name": "SQL", "proficiency": 90, "years": 6, "projects": 35, "icon": os.path.join(current_dir, "icons", "sql-azure.svg")},
            {"name": "JavaScript", "proficiency": 85, "years": 4, "projects": 20, "icon": os.path.join(current_dir, "icons", "javascript.svg")},
        ]
    },
    {
        "category": tr("SKILLS_ML_FRAMEWORKS_CATEGORY"),
        "description": tr("SKILLS_ML_FRAMEWORKS_DESC"),
        "skills": [
            {"name": "TensorFlow", "proficiency": 90, "years": 7, "projects": 40, "icon": os.path.join(current_dir, "icons", "tensorflow.svg")},
            {"name": "PyTorch", "proficiency": 88, "years": 6, "projects": 30, "icon": os.path.join(current_dir, "icons", "pytorch.svg")},
            {"name": "Scikit-learn", "proficiency": 95, "years": 8, "projects": 50, "icon": os.path.join(current_dir, "icons", "scikitlearn.svg")},
            {"name": "Keras", "proficiency": 92, "years": 6, "projects": 35, "icon": os.path.join(current_dir, "icons", "keras.svg")},
            {"name": "XGBoost/LightGBM", "proficiency": 87, "years": 5, "projects": 25, "icon": os.path.join(current_dir, "icons", "xgboost.svg")},
        ]
    },
    {
        "category": tr("SKILLS_DATA_TOOLS_CATEGORY"),
        "description": tr("SKILLS_DATA_TOOLS_DESC"),
        "skills": [
            {"name": "Pandas", "proficiency": 98, "years": 8, "projects": 50, "icon": os.path.join(current_dir, "icons", "pandas.svg")},
            {"name": "NumPy", "proficiency": 97, "years": 8, "projects": 50, "icon": os.path.join(current_dir, "icons", "numpy.svg")},
            {"name": "Spark", "proficiency": 85, "years": 5, "projects": 18, "icon": os.path.join(current_dir, "icons", "spark.svg")},
            {"name": "Kafka", "proficiency": 80, "years": 4, "projects": 10, "icon": os.path.join(current_dir, "icons", "kafka.svg")},
            {"name": "Tableau", "proficiency": 75, "years": 3, "projects": 8, "icon": os.path.join(current_dir, "icons", "tableau.svg")},
        ]
    },
    {
        "category": tr("SKILLS_CLOUD_DEVOPS_CATEGORY"),
        "description": tr("SKILLS_CLOUD_DEVOPS_DESC"),
        "skills": [
            {"name": "AWS", "proficiency": 90, "years": 6, "projects": 30, "icon": os.path.join(current_dir, "icons", "aws.svg")},
            {"name": "GCP", "proficiency": 85, "years": 5, "projects": 20, "icon": os.path.join(current_dir, "icons", "gcp.svg")},
            {"name": "Docker", "proficiency": 92, "years": 5, "projects": 25, "icon": os.path.join(current_dir, "icons", "docker.svg")},
            {"name": "Kubernetes", "proficiency": 80, "years": 4, "projects": 15, "icon": os.path.join(current_dir, "icons", "kubernetes.svg")},
            {"name": "MLflow", "proficiency": 88, "years": 4, "projects": 12, "icon": os.path.join(current_dir, "icons", "mlflow.svg")},
            {"name": "Git", "proficiency": 95, "years": 8, "projects": 50, "icon": os.path.join(current_dir, "icons", "git.svg")},
        ]
    },
    {
        "category": tr("SKILLS_NLP_LLM_CATEGORY"),
        "description": tr("SKILLS_NLP_LLM_DESC"),
        "skills": [
            {"name": "Hugging Face", "proficiency": 90, "years": 4, "projects": 20, "icon": os.path.join(current_dir, "icons", "huggingface.svg")},
            {"name": "LangChain", "proficiency": 85, "years": 2, "projects": 10, "icon": os.path.join(current_dir, "icons", "langchain.svg")},
            {"name": "Vector DBs", "proficiency": 87, "years": 3, "projects": 15, "icon": os.path.join(current_dir, "icons", "vectordb.svg")},
            {"name": "RAG", "proficiency": 90, "years": 2, "projects": 10, "icon": os.path.join(current_dir, "icons", "rag.svg")},
        ]
    }
]

# Set page style
def set_style():
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
        
        .metric-card {
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 25px rgba(0, 0, 0, 0.15);
        }
        .metric-card h3 {
            color: #4a4a4a;
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
        }
        .metric-card p {
            color: #667eea;
            font-size: 2.2rem;
            font-weight: 700;
        }
        
        .skill-category-card {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }
        .skill-category-card h3 {
            color: #4a4a4a;
            margin-bottom: 1.5rem;
            border-bottom: 2px solid #667eea;
            padding-bottom: 0.5rem;
        }
        .skill-item {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        }
        .skill-item img {
            width: 30px;
            height: 30px;
            margin-right: 1rem;
        }
        .skill-item span {
            font-size: 1.1rem;
            color: #333;
        }
        
        .business-value-card {
            background: linear-gradient(145deg, #e6e6fa, #d0b3ff);
            border-radius: 15px;
            padding: 2rem;
            margin-top: 2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            color: #333;
        }
        .business-value-card h3 {
            color: #5d3f6a;
            margin-bottom: 1.5rem;
        }
        .business-value-card p {
            font-size: 1.05rem;
            line-height: 1.6;
        }
        
        .interactive-demo {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            color: #333;
        }
        .interactive-demo h3 {
            color: #4a4a4a;
            margin-bottom: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)

set_style()

# Hero Section
st.markdown(f"""
<div class="skills-hero">
    <h1>{tr('SKILLS_HERO_TITLE')}</h1>
    <p style="font-size: 1.2rem; color: #555;">{tr('SKILLS_HERO_SUBTITLE')}</p>
</div>
""", unsafe_allow_html=True)

# Skills Overview Metrics
st.markdown(f"## {tr('SKILLS_OVERVIEW_TITLE')}")
col1, col2, col3, col4 = st.columns(4)

total_years = sum(skill['years'] for category in skills_data for skill in category['skills']) / len(skills_data) if skills_data else 0 # Simple average of years across all skills
total_projects = sum(skill['projects'] for category in skills_data for skill in category['skills'])
total_technologies = sum(len(category['skills']) for category in skills_data)
avg_proficiency = np.mean([skill['proficiency'] for category in skills_data for skill in category['skills']])

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>{tr('SKILLS_METRIC_EXPERIENCE')}</h3>
        <p>{total_years:.1f}+</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h3>{tr('SKILLS_METRIC_PROJECTS')}</h3>
        <p>{total_projects}+</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="metric-card">
        <h3>{tr('SKILLS_METRIC_TECHNOLOGIES')}</h3>
        <p>{total_technologies}+</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div class="metric-card">
        <h3>{tr('SKILLS_METRIC_AVG_PROFICIENCY')}</h3>
        <p>{avg_proficiency:.1f}%</p>
    </div>
    """, unsafe_allow_html=True)

# Skills Radar Chart
st.markdown(f"## {tr('SKILLS_RADAR_TITLE')}")
categories = [category['category'] for category in skills_data]
avg_proficiencies = [np.mean([skill['proficiency'] for skill in category['skills']]) for category in skills_data]

fig = go.Figure(data=go.Scatterpolar(
    r=avg_proficiencies,
    theta=categories,
    fill='toself',
    name='Proficiency',
    hovertemplate='<b>%{theta}</b><br>Proficiency: %{r:.1f}%<extra></extra>',
    marker=dict(color='#764ba2'),
    line_color='#667eea',
))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100],
            color='#333',
            linecolor='#555',
            gridcolor='#ccc'
        ),
        angularaxis=dict(
            linecolor='#555',
            gridcolor='#ccc',
            tickfont=dict(size=12, color='#333')
        )
    ),
    showlegend=False,
    height=400,
    margin=dict(l=70, r=70, t=70, b=70),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(family='Inter', color='#333')
)
st.plotly_chart(fig, use_container_width=True)

# Detailed Technical Skills
st.markdown(f"## {tr('SKILLS_DETAILED_TITLE')}")
for category_data in skills_data:
    st.markdown(f"""
    <div class="skill-category-card">
        <h3>{category_data['category']}</h3>
        <p style="color: #666; margin-bottom: 1.5rem;">{category_data['description']}</p>
        <div class="skill-list">
    """, unsafe_allow_html=True)
    
    # Create columns for skills within each category
    cols_per_row = 3
    skill_cols = st.columns(cols_per_row)
    
    for i, skill in enumerate(category_data['skills']):
        with skill_cols[i % cols_per_row]:
            st.markdown(f"""
            <div class="skill-item">
                <img src="{skill['icon']}" alt="{skill['name']}" title="{skill['name']}">
                <span>{skill['name']}</span>
                <div style="flex-grow: 1; margin-left: 1rem; background-color: #eee; border-radius: 5px;">
                    <div style="width: {skill['proficiency']}%; background-color: #667eea; height: 10px; border-radius: 5px;"></div>
                </div>
                <span style="margin-left: 0.5rem; font-weight: bold;">{skill['proficiency']}%</span>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True) # Close skill-list and skill-category-card divs

# Deep Learning & AI Model Expertise
st.markdown(f"## {tr('SKILLS_DL_TITLE')}")
st.markdown(f"<h3>{tr('SKILLS_DL_APPLICATIONS')}</h3>")
st.markdown("""
<div class="interactive-demo">
    <ul style="list-style-type: disc; padding-left: 20px;">
        <li>Computer Vision (Object Detection, Segmentation, Image Generation - GANs, Diffusion Models)</li>
        <li>Natural Language Processing (Text Classification, Sentiment Analysis, Named Entity Recognition, LLMs, RAG)</li>
        <li>Time Series Analysis (Forecasting, Anomaly Detection)</li>
        <li>Generative AI (Content Creation, Data Augmentation)</li>
        <li>Reinforcement Learning (Optimal Control, Decision Making)</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Skills Evolution and Comparison (Placeholder for a more complex visualization)
st.markdown(f"## {tr('SKILLS_COMPARISON_TITLE')}")
st.info(tr("SKILLS_COMPARISON_INFO")) # Placeholder for a more dynamic chart

# How these skills create business value
st.markdown(f"## {tr('SKILLS_BUSINESS_TITLE')}")
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
    <div class="business-value-card">
        <h3>{tr('SKILLS_BUSINESS_TIME_TO_MARKET')}</h3>
        <p>{tr('SKILLS_BUSINESS_TIME_TO_MARKET_DESC')}</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="business-value-card">
        <h3>{tr('SKILLS_BUSINESS_COST')}</h3>
        <p>{tr('SKILLS_BUSINESS_COST_DESC')}</p>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.markdown(f"""
    <div class="business-value-card">
        <h3>{tr('SKILLS_BUSINESS_ACCURACY')}</h3>
        <p>{tr('SKILLS_BUSINESS_ACCURACY_DESC')}</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div class="business-value-card">
        <h3>{tr('SKILLS_BUSINESS_ROBUST')}</h3>
        <p>{tr('SKILLS_BUSINESS_ROBUST_DESC')}</p>
    </div>
    """, unsafe_allow_html=True)

# Continuous Learning and Innovation
st.markdown(f"## {tr('SKILLS_LEARNING_TITLE')}")
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="interactive-demo">
        <h3>{tr('SKILLS_EXPLORING_TITLE')}</h3>
        <ul style="list-style-type: disc; padding-left: 20px;">
            <li>{tr('ABOUT_AI_AGENTS_TITLE')}</li>
            <li>{tr('ABOUT_EXPLAINABLE_AI_TITLE')}</li>
            <li>Reinforcement Learning from Human Feedback (RLHF)</li>
            <li>Edge AI and TinyML for resource-constrained environments</li>
            <li>Ethical AI and bias mitigation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="interactive-demo">
        <h3>{tr('SKILLS_LEARNING_METHOD_TITLE')}</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li>📖 <strong>{tr('SKILLS_LEARNING_METHOD_RESEARCH')}</strong> - {tr('SKILLS_LEARNING_METHOD_RESEARCH_DESC')}</li>
            <li>🛠️ <strong>{tr('SKILLS_LEARNING_METHOD_HANDS_ON')}</strong> - {tr('SKILLS_LEARNING_METHOD_HANDS_ON_DESC')}</li>
            <li>🤝 <strong>{tr('SKILLS_LEARNING_METHOD_COMMUNITY')}</strong> - {tr('SKILLS_LEARNING_METHOD_COMMUNITY_DESC')}</li>
            <li>🎓 <strong>{tr('SKILLS_LEARNING_METHOD_EDUCATION')}</strong> - {tr('SKILLS_LEARNING_METHOD_EDUCATION_DESC')}</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Call to Action
st.markdown(f"""
<div class="skills-hero">
    <h2>{tr('SKILLS_CALL_TITLE')}</h2>
    <p style="font-size: 1.2rem; color: #555; margin-top: 2rem;">
        {tr('SKILLS_CALL_TEXT')}
    </p>
    <p style="font-size: 1.1rem; color: #666; margin-top: 1rem;">
        {tr('SKILLS_CALL_TEXT2')}
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown(f"<p style='text-align: center; color: #666; margin-top: 2rem;'>{tr('SKILLS_FOOTER')}</p>", unsafe_allow_html=True)
