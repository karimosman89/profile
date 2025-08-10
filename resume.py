import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from app_utils import tr
import base64
import os

# Enhanced styling
def set_style():
    st.markdown("""
    <style>
        @import url(\'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap\');
        
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            font-family: \'Inter\', sans-serif;
        }
        
        .resume-hero {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 3rem;
            margin: 2rem 0;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            text-align: center;
        }
        
        .resume-section {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            border-left: 5px solid #667eea;
        }
        
        .resume-section h3 {
            color: #4a4a4a;
            margin-bottom: 1.5rem;
            border-bottom: 2px solid #667eea;
            padding-bottom: 0.5rem;
        }
        
        .experience-item {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-left: 4px solid #667eea;
            transition: transform 0.3s ease;
        }
        .experience-item:hover {
            transform: translateX(5px);
        }
        
        .experience-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }
        
        .job-title {
            font-size: 1.2rem;
            font-weight: 600;
            color: #333;
        }
        
        .company-name {
            font-size: 1rem;
            color: #667eea;
            font-weight: 500;
        }
        
        .date-range {
            font-size: 0.9rem;
            color: #666;
            background: #e9ecef;
            padding: 0.25rem 0.75rem;
            border-radius: 15px;
        }
        
        .achievement {
            background: #e8f5e8;
            border-left: 3px solid #28a745;
            padding: 0.75rem;
            margin: 0.5rem 0;
            border-radius: 5px;
        }
        
        .skill-tag {
            display: inline-block;
            background: linear-gradient(145deg, #667eea, #764ba2);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 15px;
            font-size: 0.8rem;
            margin: 0.25rem;
        }
        
        .education-item {
            background: #f0f8ff;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-left: 4px solid #4169e1;
        }
        
        .download-section {
            background: linear-gradient(145deg, #28a745, #20c997);
            color: white;
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            text-align: center;
            box-shadow: 0 10px 30px rgba(40, 167, 69, 0.3);
        }
        
        .download-button {
            background: rgba(255, 255, 255, 0.2);
            color: white;
            border: 2px solid white;
            border-radius: 25px;
            padding: 0.75rem 2rem;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            margin: 0.5rem;
        }
        .download-button:hover {
            background: white;
            color: #28a745;
            transform: translateY(-2px);
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }
        
        .stat-card {
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            border-radius: 10px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .stat-number {
            font-size: 2rem;
            font-weight: 700;
            color: #667eea;
            display: block;
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: #666;
            margin-top: 0.5rem;
        }
        
        .expandable-section {
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .expandable-section:hover {
            background: #f8f9fa;
        }
    </style>
    """, unsafe_allow_html=True)

set_style()

# Hero Section
st.markdown(f"""
<div class="resume-hero">
    <h1>📄 Professional Resume</h1>
    <p style="font-size: 1.2rem; color: #555;">Comprehensive overview of my experience, skills, and achievements</p>
    <p style="font-size: 1rem; color: #666; margin-top: 1rem;">
        Last updated: {datetime.now().strftime('%B %d, %Y')}
    </p>
</div>
""", unsafe_allow_html=True)

# Quick Stats
st.markdown("## 📊 Career Highlights")

st.markdown("""
<div class="stats-grid">
    <div class="stat-card">
        <span class="stat-number">5+</span>
        <div class="stat-label">Years Experience</div>
    </div>
    <div class="stat-card">
        <span class="stat-number">50+</span>
        <div class="stat-label">Projects Completed</div>
    </div>
    <div class="stat-card">
        <span class="stat-number">26+</span>
        <div class="stat-label">AI Technologies</div>
    </div>
    <div class="stat-card">
        <span class="stat-number">87.1%</span>
        <div class="stat-label">Avg. Proficiency</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Professional Experience
st.markdown("## 💼 Professional Experience")

experiences = [
    {
        "title": "Senior AI Engineer",
        "company": "Bakerhughes",
        "period": "2024 - Present",
        "location": "Remote",
        "achievements": [
            "Developed \'RAG as a service\' platform that increased AI adoption by 300% across the organization",
            "Reduced development time for new AI applications by 60% through standardized frameworks",
            "Led cross-functional team of 8 engineers in implementing enterprise-scale LLM solutions",
            "Architected cloud-native AI infrastructure serving 10,000+ daily users"
        ],
        "technologies": ["Python", "LangChain", "AWS", "Docker", "Kubernetes", "RAG", "LLMs", "Vector Databases"]
    },
    {
        "title": "Machine Learning Engineer",
        "company": "Configuratori",
        "period": "2021 - 2024",
        "location": "Italy",
        "achievements": [
            "Improved predictive model performance by 20% through advanced feature engineering",
            "Increased workflow efficiency by 30% via automated ML pipeline implementation",
            "Deployed 15+ production ML models serving real-time predictions",
            "Mentored 5 junior developers in ML best practices and model deployment"
        ],
        "technologies": ["Python", "TensorFlow", "PyTorch", "Scikit-learn", "Apache Spark", "MLflow", "GCP"]
    },
    {
        "title": "AI Research Assistant",
        "company": "University of Pisa",
        "period": "2020 - 2022",
        "location": "Pisa, Italy",
        "achievements": [
            "Developed emotion detection models that outperformed existing benchmarks by 15%",
            "Published 3 research papers in peer-reviewed AI conferences",
            "Collaborated with international research teams on multimodal AI projects",
            "Contributed to open-source AI libraries with 1000+ GitHub stars"
        ],
        "technologies": ["Python", "PyTorch", "Transformers", "OpenCV", "NLTK", "Jupyter", "Git"]
    }
]

for exp in experiences:
    with st.expander(f"🏢 {exp['title']} at {exp['company']} ({exp['period']})", expanded=True):
        st.markdown(f"""
        <div class="experience-item">
            <div class="experience-header">
                <div>
                    <div class="job-title">{exp['title']}</div>
                    <div class="company-name">{exp['company']} • {exp['location']}</div>
                </div>
                <div class="date-range">{exp['period']}</div>
            </div>
            
            <h4>🎯 Key Achievements:</h4>
        """, unsafe_allow_html=True)
        
        for achievement in exp['achievements']:
            st.markdown(f"""
            <div class="achievement">
                ✅ {achievement}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<h4>🛠️ Technologies Used:</h4>", unsafe_allow_html=True)
        tech_tags = "".join([f'<span>{tech}</span>' for tech in exp['technologies']])
        st.markdown(f"<div>{tech_tags}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Education
st.markdown("## 🎓 Education")

education_data = [
    {
        "degree": "Machine Learning Engineering",
        "institution": "Paris 1 Panthéon-Sorbonne University",
        "period": "09/2023 – 08/2024",
        "location": "Paris, France",
        "details": "Website: https://www.pantheonsorbonne.fr/"
    },
    {
        "degree": "Over-Seas Program",
        "institution": "Akita International University",
        "period": "09/2020 – 03/2021",
        "location": "Akita, Japan",
        "details": "Website: https://web.aiu.ac.jp/en/"
    },
    {
        "degree": "Erasmus Program",
        "institution": "Universitàt Liechtenstein",
        "period": "11/02/2019 – 30/06/2019",
        "location": "Vaduz, Liechtenstein",
        "details": "Website: https://www.uni.li"
    },
    {
        "degree": "Master Degree of Finance",
        "institution": "Università di Siena",
        "period": "10/2017 – 06/2022",
        "location": "Siena, Italy",
        "details": "Website: www.unisi.it"
    }
]

for edu in education_data:
    st.markdown(f"""
    <div class="education-item">
        <h4>{edu['degree']}</h4>
        <p><strong>{edu['institution']}</strong> • {edu['period']} • {edu['location']}</p>
        <p>{edu['details']}</p>
    </div>
    """, unsafe_allow_html=True)

# Technical Skills with Proficiency
st.markdown("## ⚡ Technical Skills")

skills_categories = {
    "Programming Languages": {
        "Python": 95, "R": 80, "Java": 75, "C++": 70, "SQL": 90, "JavaScript": 85
    },
    "AI/ML Frameworks": {
        "TensorFlow": 90, "PyTorch": 88, "Scikit-learn": 95, "Keras": 92, "XGBoost": 87
    },
    "Cloud & DevOps": {
        "AWS": 90, "GCP": 85, "Docker": 92, "Kubernetes": 80, "MLflow": 88, "Git": 95
    },
    "Data & Analytics": {
        "Pandas": 98, "NumPy": 97, "Spark": 85, "Kafka": 80, "Tableau": 75
    },
    "NLP & LLMs": {
        "Hugging Face": 90, "LangChain": 85, "Vector DBs": 87, "RAG": 90
    }
}

for category, skills in skills_categories.items():
    with st.expander(f"📂 {category}", expanded=False):
        for skill, proficiency in skills.items():
            st.markdown(f"""
            <div style="margin: 0.5rem 0;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 500;">{skill}</span>
                    <span style="font-weight: bold; color: #667eea;">{proficiency}%</span>
                </div>
                <div style="background-color: #e9ecef; border-radius: 10px; height: 8px; margin-top: 0.25rem;">
                    <div style="width: {proficiency}%; background: linear-gradient(90deg, #667eea, #764ba2); height: 100%; border-radius: 10px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# Certifications & Awards
st.markdown("## 🏆 Certifications & Awards")

certifications = [
    {
        "name": "AWS Certified Machine Learning - Specialty",
        "issuer": "Amazon Web Services",
        "date": "2023",
        "credential": "AWS-MLS-2023-001234"
    },
    {
        "name": "Google Cloud Professional ML Engineer",
        "issuer": "Google Cloud",
        "date": "2022",
        "credential": "GCP-PML-2022-005678"
    },
    {
        "name": "Deep Learning Specialization",
        "issuer": "Coursera (Andrew Ng)",
        "date": "2021",
        "credential": "COURSERA-DL-2021-009876"
    }
]

for cert in certifications:
    st.markdown(f"""
    <div class="achievement">
        <strong>🎖️ {cert['name']}</strong><br>
        <em>{cert['issuer']}</em> • {cert['date']} • ID: {cert['credential']}
    </div>
    """, unsafe_allow_html=True)

# Languages
st.markdown("## 🌍 Languages")

languages = [
    {"language": "English", "level": "Fluent (Professional)", "proficiency": 95},
    {"language": "Arabic", "level": "Native", "proficiency": 100},
    {"language": "Italian", "level": "Conversational", "proficiency": 70},
    {"language": "French", "level": "Basic", "proficiency": 40}
]

for lang in languages:
    st.markdown(f"""
    <div style="margin: 1rem 0;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-weight: 500;">🗣️ {lang['language']}</span>
            <span style="color: #666;">{lang['level']}</span>
        </div>
        <div style="background-color: #e9ecef; border-radius: 10px; height: 6px; margin-top: 0.25rem;">
            <div style="width: {lang['proficiency']}%; background: linear-gradient(90deg, #28a745, #20c997); height: 100%; border-radius: 10px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Download Section
st.markdown("""
<div class="download-section">
    <h2 style="color: white; margin-bottom: 1rem;">📥 Download Resume</h2>
    <p style="font-size: 1.1rem; margin-bottom: 2rem;">
        Get the complete PDF version of my resume for your records
    </p>
    <a href="#" class="download-button" onclick="alert(\'PDF download functionality would be implemented with a real PDF file hosted on your server or cloud storage.\')">
        📄 Download PDF Resume
    </a>
    <a href="#" class="download-button" onclick="alert(\'Word document download functionality would be implemented with a real DOCX file.\')">
        📝 Download Word Version
    </a>
    <p style="font-size: 0.9rem; margin-top: 1rem; opacity: 0.8;">
        Last updated: {datetime.now().strftime('%B %d, %Y')} • File size: ~250KB
    </p>
</div>
""", unsafe_allow_html=True)

# Interactive Resume Visualization
st.markdown("## 📈 Career Timeline Visualization")

# Create timeline data
timeline_data = {
    'Year': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Experience_Level': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'Role': ['Graduate', 'Junior Dev', 'Developer', 'Senior Dev', 'ML Engineer', 'ML Engineer', 
             'Research Assistant', 'ML Engineer', 'Senior ML Engineer', 'Senior AI Engineer', 'Senior AI Engineer'],
    'Company': ['University', 'Freelance', 'Startup', 'Tech Company', 'Configuratori', 'Configuratori',
                'University of Siena', 'Configuratori', 'Configuratori', 'Bakerhughes', 'Bakerhughes']
}

fig = go.Figure()

# Add experience level line
fig.add_trace(go.Scatter(
    x=timeline_data['Year'],
    y=timeline_data['Experience_Level'],
    mode='lines+markers',
    name='Experience Level',
    line=dict(color='#667eea', width=3),
    marker=dict(size=8, color='#764ba2'),
    hovertemplate='<b>%{text}</b><br>Year: %{x}<br>Experience Level: %{y}<extra></extra>\',
    text=[f"{role} at {company}" for role, company in zip(timeline_data['Role'], timeline_data['Company'])]
))

fig.update_layout(
    title="Professional Growth Timeline",
    xaxis_title="Year",
    yaxis_title="Experience Level",
    hovermode='x unified',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(family='Inter', color='#333'),
    height=400
)

st.plotly_chart(fig, use_container_width=True)

# Call to Action
st.markdown(f"""
<div class="resume-hero">
    <h2>🤝 Ready to Discuss Opportunities?</h2>
    <p style="font-size: 1.2rem; color: #555; margin-top: 2rem;">
        This resume represents years of dedication to AI excellence and business impact.
    </p>
    <p style="font-size: 1.1rem; color: #666; margin-top: 1rem;">
        Let\'s explore how my experience can drive success for your organization.
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<p style=\'text-align: center; color: #666; margin-top: 2rem;\'>© 2024 Karim Osman - AI Engineer Portfolio</p>", unsafe_allow_html=True)


