import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, date
import numpy as np
from PIL import Image
import base64
from io import BytesIO

def main():
    """Enhanced About page with professional design"""

    # Page header with professional styling
    st.markdown("""
    <div class="about-hero">
        <div class="about-content">
            <h1>👨‍💻 Karim Osman</h1>
            <h2>AI Engineer & Innovation Catalyst</h2>
            <p class="about-tagline">Transforming Complex Challenges into Intelligent Solutions</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Main content in two columns
    col1, col2 = st.columns([2, 1])

    with col1:
        # Professional Journey Section
        st.markdown("## 🚀 My AI Engineering Journey")

        st.markdown("""
        I am a passionate AI Engineer with extensive experience across the full spectrum of artificial intelligence, 
        from cutting-edge research to production-scale deployments. My journey began with a unique blend of 
        **financial expertise** and **technical innovation**, which has given me a distinctive perspective on how 
        AI can drive real business value.

        Currently based in **France** and working with **Bakerhughes** (via Hermes Trade company) in Florence, Italy, 
        I specialize in developing enterprise-grade AI solutions including **RAG systems**, **LLM services**, 
        and **computer vision applications**. My international experience spans multiple countries and industries, 
        allowing me to understand diverse business contexts and technical requirements.
        """)

        # Key Strengths
        st.markdown("### 💪 Core Strengths")

        strengths = [
            {
                "icon": "🎯", 
                "title": "Strategic AI Implementation", 
                "description": "Bridging the gap between AI research and practical business applications"
            },
            {
                "icon": "🌐", 
                "title": "International Expertise", 
                "description": "Experience across Europe, Asia, and multilingual project delivery"
            },
            {
                "icon": "🔧", 
                "title": "Full-Stack AI Development", 
                "description": "From data engineering to model deployment and monitoring"
            },
            {
                "icon": "📈", 
                "title": "Business Impact Focus", 
                "description": "Delivering measurable ROI through AI-driven solutions"
            }
        ]

        for strength in strengths:
            st.markdown(f"""
            <div class="strength-card">
                <div class="strength-icon">{strength['icon']}</div>
                <div class="strength-content">
                    <h4>{strength['title']}</h4>
                    <p>{strength['description']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        # Professional Photo (placeholder)
        st.markdown("""
        <div class="profile-photo-container">
            <img src="https://via.placeholder.com/300x400/667eea/ffffff?text=Karim+Osman" 
                 class="profile-photo" alt="Karim Osman - AI Engineer">
        </div>
        """, unsafe_allow_html=True)

        # Quick Facts
        st.markdown("### 📊 Quick Facts")

        facts = {
            "🎯 Current Role": "AI Engineer at Bakerhughes",
            "🌍 Location": "France (Working in Italy)",
            "🎓 Education": "ML Engineering, Finance Master's",
            "💼 Experience": "3+ Years in AI/ML",
            "🏆 Projects": "70+ Completed",
            "🌐 Languages": "5 Languages Fluent"
        }

        for fact, value in facts.items():
            st.markdown(f"**{fact}**: {value}")

        # Contact Information
        st.markdown("### 📞 Connect With Me")
        st.markdown("""
        - 📧 [karim.programmer2020@gmail.com](mailto:karim.programmer2020@gmail.com)
        - 💼 [LinkedIn Profile](https://www.linkedin.com/in/karimosman89/)
        - 🐙 [GitHub Portfolio](https://github.com/karimosman89)
        - 🌐 [Portfolio Website](https://kosman.streamlit.app/)
        """)

    # Professional Timeline
    st.markdown("## 📈 Professional Timeline")

    create_professional_timeline()

    # Skills Visualization
    st.markdown("## 🧠 Technical Expertise")

    create_skills_visualization()

    # Education & Certifications
    st.markdown("## 🎓 Education & Learning")

    create_education_section()

    # Languages & Cultural Adaptability
    st.markdown("## 🌍 Languages & Cultural Adaptability")

    create_languages_section()

    # Professional Values
    st.markdown("## 💡 Professional Philosophy")

    st.markdown("""
    <div class="philosophy-section">
        <div class="philosophy-grid">
            <div class="philosophy-card">
                <h4>🎯 Excellence-Driven</h4>
                <p>Committed to delivering high-quality AI solutions that exceed expectations</p>
            </div>
            <div class="philosophy-card">
                <h4>🤝 Collaborative</h4>
                <p>Strong believer in cross-functional teamwork and knowledge sharing</p>
            </div>
            <div class="philosophy-card">
                <h4>🚀 Innovation-Focused</h4>
                <p>Always exploring cutting-edge technologies and methodologies</p>
            </div>
            <div class="philosophy-card">
                <h4>📊 Results-Oriented</h4>
                <p>Focus on measurable business impact and practical solutions</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_professional_timeline():
    """Create interactive professional timeline"""

    timeline_data = [
        {
            "date": "Nov 2024 - Present",
            "role": "AI Engineer",
            "company": "Bakerhughes (via Hermes Trade)",
            "location": "Florence, Italy",
            "achievements": [
                "Developed enterprise RAG and LLM-as-a-Service platforms",
                "Implemented chat-with-document features for diverse document types",
                "Created comprehensive AI model benchmarking frameworks",
                "Built multi-level document summarization services",
                "Deployed computer vision solutions using YOLO and OpenCV"
            ],
            "technologies": ["Python", "LangChain", "AWS", "HuggingFace", "YOLO", "OpenCV"]
        },
        {
            "date": "Aug 2021 - Nov 2024", 
            "role": "ML Engineer & Data Scientist",
            "company": "Configuratori",
            "location": "Florence, Italy",
            "achievements": [
                "Improved predictive performance by 20% through custom ML models",
                "Enhanced data processing efficiency by 25% with specialized algorithms",
                "Increased workflow efficiency by 30% through AI system integration",
                "Developed deep learning architectures for diverse applications"
            ],
            "technologies": ["Python", "TensorFlow", "PyTorch", "scikit-learn", "Pandas", "Docker"]
        },
        {
            "date": "Feb 2021 - Jun 2021",
            "role": "Data Analyst", 
            "company": "Klimsoft",
            "location": "Siena, Italy",
            "achievements": [
                "Led data analysis projects using IBM Cognos V11",
                "Developed automation scripts reducing error rates by 15%",
                "Enhanced executive reporting accuracy by 40%",
                "Implemented continuous improvement processes"
            ],
            "technologies": ["IBM Cognos", "Python", "SQL", "Data Visualization"]
        },
        {
            "date": "Nov 2020 - Mar 2021",
            "role": "Backend Engineer",
            "company": "UniqMaster", 
            "location": "Bremen, Germany",
            "achievements": [
                "Designed RESTful APIs with 99.9% uptime",
                "Built microservices architecture for data exchange",
                "Reduced application response time by 35%",
                "Contributed to Agile development processes"
            ],
            "technologies": ["Python", "FastAPI", "PostgreSQL", "Docker", "AWS"]
        }
    ]

    # Create timeline visualization
    for idx, item in enumerate(timeline_data):
        with st.expander(f"{item['date']} - {item['role']} at {item['company']}", expanded=(idx==0)):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"**Location:** {item['location']}")
                st.markdown("**Key Achievements:**")
                for achievement in item['achievements']:
                    st.markdown(f"• {achievement}")

            with col2:
                st.markdown("**Technologies:**")
                for tech in item['technologies']:
                    st.markdown(f"`{tech}`")

def create_skills_visualization():
    """Create interactive skills visualization"""

    # Skills data
    skills_data = {
        'Machine Learning & AI': {
            'Python': 95,
            'TensorFlow': 90,
            'PyTorch': 88,
            'scikit-learn': 92,
            'HuggingFace': 85,
            'LangChain': 90
        },
        'Data Engineering': {
            'Pandas': 95,
            'NumPy': 93,
            'SQL': 90,
            'Apache Spark': 75,
            'ETL Pipelines': 88,
            'Data Warehousing': 80
        },
        'Cloud & DevOps': {
            'AWS': 85,
            'Docker': 88,
            'Kubernetes': 75,
            'CI/CD': 82,
            'Git': 95,
            'Linux': 85
        },
        'Web Development': {
            'FastAPI': 88,
            'Streamlit': 95,
            'Flask': 85,
            'REST APIs': 90,
            'JavaScript': 70,
            'HTML/CSS': 80
        }
    }

    # Create tabs for different skill categories
    tabs = st.tabs(list(skills_data.keys()))

    for idx, (category, skills) in enumerate(skills_data.items()):
        with tabs[idx]:
            # Create horizontal bar chart
            fig = go.Figure()

            skills_list = list(skills.keys())
            values_list = list(skills.values())

            fig.add_trace(go.Bar(
                y=skills_list,
                x=values_list,
                orientation='h',
                marker_color=['#667eea' if v >= 90 else '#764ba2' if v >= 80 else '#2196f3' for v in values_list],
                text=[f"{v}%" for v in values_list],
                textposition='inside'
            ))

            fig.update_layout(
                title=f"{category} Proficiency",
                xaxis_title="Proficiency Level (%)",
                height=400,
                showlegend=False,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )

            st.plotly_chart(fig, use_container_width=True)

def create_education_section():
    """Create education and learning section"""

    education_data = [
        {
            "degree": "Machine Learning Engineering",
            "institution": "Paris 1 Panthéon-Sorbonne University",
            "period": "2023-2024",
            "location": "Paris, France",
            "highlights": [
                "Specialized in deep learning architectures and LLM fine-tuning",
                "Capstone project: RAG system for legal document analysis",
                "Focus on production ML systems and MLOps"
            ]
        },
        {
            "degree": "Master's Degree in Finance",
            "institution": "Università di Siena", 
            "period": "2017-2022",
            "location": "Siena, Italy",
            "highlights": [
                "Thesis: 'Machine Learning Applications in Algorithmic Trading'",
                "Quantitative analysis and financial modeling",
                "Statistical methods and econometrics"
            ]
        },
        {
            "degree": "Overseas Exchange Program",
            "institution": "Akita International University",
            "period": "2020-2021", 
            "location": "Akita, Japan",
            "highlights": [
                "Advanced coursework in data science and NLP",
                "Cross-cultural business and technology studies",
                "Research in cross-lingual information retrieval"
            ]
        },
        {
            "degree": "Erasmus Exchange Program",
            "institution": "Universität Liechtenstein",
            "period": "Feb-Jun 2019",
            "location": "Vaduz, Liechtenstein", 
            "highlights": [
                "Quantitative financial analysis",
                "Financial technology and innovation",
                "European business practices"
            ]
        }
    ]

    for edu in education_data:
        st.markdown(f"""
        <div class="education-card">
            <div class="education-header">
                <h4>{edu['degree']}</h4>
                <span class="education-period">{edu['period']}</span>
            </div>
            <p class="education-institution">{edu['institution']} - {edu['location']}</p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("View Details"):
            for highlight in edu['highlights']:
                st.markdown(f"• {highlight}")

def create_languages_section():
    """Create languages and cultural adaptability section"""

    languages = {
        'Arabic': {'level': 100, 'description': 'Native speaker'},
        'English': {'level': 95, 'description': 'Fluent - Professional working proficiency'},
        'Italian': {'level': 90, 'description': 'Fluent - Lived and worked in Italy'},
        'French': {'level': 85, 'description': 'Advanced - Currently living in France'},
        'German': {'level': 70, 'description': 'Intermediate - Worked in Germany'}
    }

    # Create language proficiency chart
    fig = go.Figure()

    langs = list(languages.keys())
    levels = [languages[lang]['level'] for lang in langs]

    fig.add_trace(go.Bar(
        x=langs,
        y=levels,
        marker_color=['#667eea', '#764ba2', '#2196f3', '#00bcd4', '#4caf50'],
        text=[f"{level}%" for level in levels],
        textposition='inside'
    ))

    fig.update_layout(
        title="Language Proficiency",
        yaxis_title="Proficiency Level (%)",
        height=400,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

    # Cultural adaptability
    st.markdown("### 🌍 Cultural Adaptability")
    st.markdown("""
    My international experience across **Europe**, **Asia**, and **MENA** regions has developed:

    - **Cross-cultural Communication**: Ability to work effectively with diverse teams
    - **Global Business Perspective**: Understanding of different business practices and requirements  
    - **Adaptability**: Quick adjustment to new work environments and cultures
    - **Remote Collaboration**: Expert in distributed team coordination and communication
    """)

if __name__ == "__main__":
    main()
