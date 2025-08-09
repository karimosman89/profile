
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import hashlib
from typing import Dict, List, Optional, Any
import base64
import io

# Professional Data Management
class PortfolioDataManager:
    """Advanced data management for professional portfolio"""

    def __init__(self):
        self.cache_duration = 3600  # 1 hour cache
        self.analytics_enabled = True

    @st.cache_data(ttl=3600)
    def load_professional_data(_self) -> Dict[str, Any]:
        """Load comprehensive professional portfolio data"""
        return {
            'personal_info': {
                'name': 'Karim Osman',
                'title': 'Senior AI/ML Engineer',
                'location': 'Alexandria, Egypt',
                'email': 'karim.osman.ai@gmail.com',
                'phone': '+20 123 456 7890',
                'linkedin': 'https://linkedin.com/in/karim-osman',
                'github': 'https://github.com/karimosman89',
                'twitter': 'https://twitter.com/karim_ai',
                'website': 'https://kosman.streamlit.app'
            },
            'professional_summary': {
                'experience_years': 8,
                'projects_completed': 50,
                'certifications': 12,
                'publications': 5,
                'languages': ['Arabic', 'English', 'French'],
                'specializations': [
                    'Deep Learning & Neural Networks',
                    'Computer Vision & Image Processing', 
                    'Natural Language Processing',
                    'MLOps & Production Systems',
                    'Cloud AI/ML Solutions'
                ]
            },
            'technical_skills': {
                'programming_languages': {
                    'Python': 95,
                    'JavaScript': 85,
                    'SQL': 90,
                    'R': 80,
                    'Java': 75,
                    'C++': 70
                },
                'ai_ml_frameworks': {
                    'TensorFlow': 95,
                    'PyTorch': 90,
                    'Scikit-learn': 95,
                    'Keras': 90,
                    'Hugging Face': 85,
                    'OpenCV': 90
                },
                'cloud_platforms': {
                    'AWS': 90,
                    'Google Cloud': 85,
                    'Azure': 80,
                    'Docker': 90,
                    'Kubernetes': 75
                },
                'data_tools': {
                    'Pandas': 95,
                    'NumPy': 95,
                    'Matplotlib': 90,
                    'Plotly': 85,
                    'Apache Spark': 80,
                    'Streamlit': 95
                }
            },
            'education': [
                {
                    'degree': 'Master of Science in Computer Science',
                    'institution': 'Alexandria University',
                    'location': 'Alexandria, Egypt',
                    'year': '2018-2020',
                    'gpa': '3.9/4.0',
                    'thesis': 'Deep Learning Applications in Medical Image Analysis',
                    'relevant_coursework': [
                        'Machine Learning',
                        'Computer Vision',
                        'Natural Language Processing',
                        'Statistical Learning Theory'
                    ]
                },
                {
                    'degree': 'Bachelor of Engineering in Computer Engineering',
                    'institution': 'Alexandria University',
                    'location': 'Alexandria, Egypt', 
                    'year': '2014-2018',
                    'gpa': '3.8/4.0',
                    'honors': 'Magna Cum Laude',
                    'relevant_coursework': [
                        'Data Structures & Algorithms',
                        'Software Engineering',
                        'Database Systems',
                        'Web Development'
                    ]
                }
            ],
            'certifications': [
                {
                    'name': 'Google Cloud Professional ML Engineer',
                    'issuer': 'Google Cloud',
                    'date': '2023',
                    'credential_id': 'GCP-ML-2023-KO',
                    'skills': ['ML Engineering', 'Cloud Computing', 'Model Deployment']
                },
                {
                    'name': 'AWS Certified Solutions Architect',
                    'issuer': 'Amazon Web Services',
                    'date': '2022',
                    'credential_id': 'AWS-SA-2022-KO',
                    'skills': ['Cloud Architecture', 'AWS Services', 'System Design']
                },
                {
                    'name': 'Deep Learning Specialization',
                    'issuer': 'Coursera/DeepLearning.AI',
                    'date': '2021',
                    'credential_id': 'DL-SPEC-2021-KO',
                    'skills': ['Neural Networks', 'Deep Learning', 'TensorFlow']
                }
            ],
            'work_experience': [
                {
                    'position': 'Senior AI/ML Engineer',
                    'company': 'TechCorp Solutions',
                    'location': 'Remote',
                    'duration': '2022 - Present',
                    'type': 'Full-time',
                    'achievements': [
                        'Led development of computer vision system increasing accuracy by 35%',
                        'Built scalable ML pipeline processing 1M+ daily transactions',
                        'Mentored junior engineers and established ML best practices',
                        'Reduced model inference time by 60% through optimization'
                    ],
                    'technologies': ['Python', 'TensorFlow', 'AWS', 'Docker', 'Kubernetes']
                },
                {
                    'position': 'ML Engineer',
                    'company': 'AI Innovations Ltd.',
                    'location': 'Alexandria, Egypt',
                    'duration': '2020 - 2022',
                    'type': 'Full-time', 
                    'achievements': [
                        'Developed NLP models for customer sentiment analysis',
                        'Implemented MLOps pipelines reducing deployment time by 50%',
                        'Created recommendation system improving user engagement by 25%',
                        'Published 3 research papers in top-tier conferences'
                    ],
                    'technologies': ['Python', 'PyTorch', 'Apache Spark', 'MLflow', 'GCP']
                }
            ]
        }

    def get_portfolio_metrics(self) -> List[Dict[str, str]]:
        """Get professional portfolio metrics"""
        data = self.load_professional_data()
        return [
            {'value': f"{data['professional_summary']['experience_years']}+", 'label': 'Years Experience'},
            {'value': f"{data['professional_summary']['projects_completed']}+", 'label': 'Projects Completed'},
            {'value': f"{data['professional_summary']['certifications']}", 'label': 'Certifications'},
            {'value': f"{data['professional_summary']['publications']}", 'label': 'Publications'},
        ]

# Advanced Analytics & Visualization
class PortfolioAnalytics:
    """Professional analytics and visualization utilities"""

    @staticmethod
    @st.cache_data
    def create_skills_radar_chart(skills_data: Dict[str, Dict[str, int]]) -> go.Figure:
        """Create interactive radar chart for skills"""
        categories = []
        values = []

        for category, skills in skills_data.items():
            avg_skill = sum(skills.values()) / len(skills)
            categories.append(category.replace('_', ' ').title())
            values.append(avg_skill)

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            fillcolor='rgba(46, 134, 171, 0.3)',
            line_color='#2E86AB',
            line_width=3,
            marker=dict(size=8, color='#2E86AB'),
            name='Skills Level'
        ))

        fig.update_layout(
            polar=dict(
                bgcolor='white',
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    gridcolor='rgba(108, 117, 125, 0.3)',
                    tickfont=dict(size=10, color='#6C757D')
                ),
                angularaxis=dict(
                    gridcolor='rgba(108, 117, 125, 0.3)',
                    tickfont=dict(size=12, color='#343A40', family='Segoe UI')
                )
            ),
            showlegend=False,
            title=dict(
                text='Technical Skills Overview',
                font=dict(size=18, color='#1E5A73', family='Segoe UI'),
                x=0.5
            ),
            width=500,
            height=500,
            margin=dict(l=80, r=80, t=80, b=80)
        )

        return fig

    @staticmethod
    @st.cache_data
    def create_experience_timeline(work_data: List[Dict]) -> go.Figure:
        """Create professional experience timeline"""
        positions = []
        companies = []
        start_dates = []
        end_dates = []

        for job in work_data:
            positions.append(job['position'])
            companies.append(job['company'])

            # Parse duration string (assuming format like "2022 - Present" or "2020 - 2022")
            duration = job['duration']
            if ' - ' in duration:
                start, end = duration.split(' - ')
                start_year = int(start) if start.isdigit() else 2020
                end_year = 2024 if end == 'Present' else int(end)

                start_dates.append(datetime(start_year, 1, 1))
                end_dates.append(datetime(end_year, 12, 31))

        fig = go.Figure()

        for i, (pos, comp, start, end) in enumerate(zip(positions, companies, start_dates, end_dates)):
            fig.add_trace(go.Scatter(
                x=[start, end],
                y=[i, i],
                mode='lines+markers',
                line=dict(width=8, color='#2E86AB'),
                marker=dict(size=12, color='#2E86AB'),
                name=f"{pos} at {comp}",
                hovertemplate=f"<b>{pos}</b><br>{comp}<br>%{{x}}<extra></extra>"
            ))

        fig.update_layout(
            title=dict(
                text='Professional Experience Timeline',
                font=dict(size=18, color='#1E5A73'),
                x=0.5
            ),
            xaxis=dict(
                title='Year',
                showgrid=True,
                gridcolor='rgba(108, 117, 125, 0.3)'
            ),
            yaxis=dict(
                title='Positions',
                tickmode='array',
                tickvals=list(range(len(positions))),
                ticktext=[f"{pos}<br><i>{comp}</i>" for pos, comp in zip(positions, companies)],
                showgrid=True,
                gridcolor='rgba(108, 117, 125, 0.3)'
            ),
            showlegend=False,
            height=400,
            margin=dict(l=200, r=50, t=80, b=50)
        )

        return fig

    @staticmethod
    @st.cache_data
    def create_project_impact_chart(projects_data: List[Dict]) -> go.Figure:
        """Create project impact visualization"""
        # Sample project impact data
        sample_projects = [
            {'name': 'AI Vision System', 'impact': 95, 'complexity': 90, 'type': 'Computer Vision'},
            {'name': 'NLP Chatbot', 'impact': 85, 'complexity': 80, 'type': 'NLP'},
            {'name': 'Recommendation Engine', 'impact': 90, 'complexity': 75, 'type': 'ML'},
            {'name': 'Fraud Detection', 'impact': 88, 'complexity': 85, 'type': 'ML'},
            {'name': 'Image Classification', 'impact': 82, 'complexity': 70, 'type': 'Computer Vision'}
        ]

        fig = px.scatter(
            sample_projects,
            x='complexity',
            y='impact', 
            color='type',
            size=[50] * len(sample_projects),
            hover_name='name',
            title='Project Impact vs Complexity',
            labels={'complexity': 'Technical Complexity', 'impact': 'Business Impact'},
            color_discrete_map={
                'Computer Vision': '#2E86AB',
                'NLP': '#F24236', 
                'ML': '#6C5CE7'
            }
        )

        fig.update_layout(
            width=600,
            height=400,
            showlegend=True,
            title_font=dict(size=18, color='#1E5A73'),
            margin=dict(l=50, r=50, t=80, b=50)
        )

        return fig

# Professional Contact & Lead Management
class ContactManager:
    """Professional contact form and lead management"""

    @staticmethod
    def create_contact_form():
        """Create professional contact form with validation"""
        st.markdown("### 📧 Get In Touch")
        st.markdown("Ready to collaborate? Let's discuss your next AI/ML project.")

        with st.form("professional_contact_form"):
            col1, col2 = st.columns(2)

            with col1:
                name = st.text_input("Full Name *", placeholder="John Doe")
                company = st.text_input("Company/Organization", placeholder="TechCorp Inc.")

            with col2:
                email = st.text_input("Email Address *", placeholder="john@example.com")
                phone = st.text_input("Phone Number", placeholder="+1 234 567 8900")

            project_type = st.selectbox(
                "Project Type *",
                ["", "AI/ML Consulting", "Deep Learning Project", "Computer Vision", 
                 "NLP Solution", "MLOps Implementation", "Data Science Project", "Other"]
            )

            budget_range = st.selectbox(
                "Budget Range",
                ["", "$5K - $15K", "$15K - $50K", "$50K - $100K", "$100K+", "Discuss Later"]
            )

            timeline = st.selectbox(
                "Project Timeline",
                ["", "1-2 months", "3-6 months", "6+ months", "Ongoing partnership"]
            )

            message = st.text_area(
                "Project Description *", 
                placeholder="Please describe your project requirements, goals, and any specific technical needs...",
                height=120
            )

            # Additional qualification questions
            st.markdown("### 📊 Additional Information")

            col3, col4 = st.columns(2)
            with col3:
                current_solution = st.text_input("Current Solution (if any)", placeholder="Manual process, Excel, etc.")

            with col4:
                team_size = st.selectbox("Technical Team Size", ["", "Just me", "2-5 people", "6-15 people", "15+ people"])

            # Privacy and terms
            privacy_agreed = st.checkbox("I agree to the privacy policy and terms of service")
            newsletter_signup = st.checkbox("Subscribe to AI/ML insights newsletter")

            submitted = st.form_submit_button("🚀 Send Message", use_container_width=True)

            if submitted:
                # Validation
                errors = []
                if not name.strip():
                    errors.append("Full name is required")
                if not email.strip() or "@" not in email:
                    errors.append("Valid email address is required")
                if not project_type:
                    errors.append("Project type is required")
                if not message.strip():
                    errors.append("Project description is required")
                if not privacy_agreed:
                    errors.append("You must agree to the privacy policy")

                if errors:
                    for error in errors:
                        st.error(f"❌ {error}")
                else:
                    # Simulate form processing
                    ContactManager.process_contact_submission({
                        'name': name,
                        'email': email,
                        'company': company,
                        'phone': phone,
                        'project_type': project_type,
                        'budget_range': budget_range,
                        'timeline': timeline,
                        'message': message,
                        'current_solution': current_solution,
                        'team_size': team_size,
                        'newsletter_signup': newsletter_signup,
                        'submission_time': datetime.now().isoformat()
                    })

    @staticmethod
    def process_contact_submission(form_data: Dict[str, str]):
        """Process contact form submission"""
        # In a real application, this would:
        # 1. Save to database
        # 2. Send email notifications
        # 3. Integrate with CRM
        # 4. Send auto-response

        st.success("✅ Message sent successfully!")
        st.info("🎯 You'll receive a response within 24 hours.")
        st.balloons()

        # Display confirmation details
        with st.expander("📋 Submission Details"):
            st.json(form_data)

# Professional Resume & CV Utils
class ResumeManager:
    """Professional resume and CV management utilities"""

    @staticmethod
    def generate_pdf_resume(personal_data: Dict) -> bytes:
        """Generate professional PDF resume"""
        # Placeholder for PDF generation
        # In a real implementation, you'd use libraries like:
        # - reportlab
        # - weasyprint
        # - jinja2 + wkhtmltopdf

        resume_content = f"""
        PROFESSIONAL RESUME

        {personal_data['personal_info']['name']}
        {personal_data['personal_info']['title']}

        Contact Information:
        Email: {personal_data['personal_info']['email']}
        Location: {personal_data['personal_info']['location']}
        LinkedIn: {personal_data['personal_info']['linkedin']}

        Professional Summary:
        - {personal_data['professional_summary']['experience_years']}+ years of experience
        - {personal_data['professional_summary']['projects_completed']}+ projects completed
        - {personal_data['professional_summary']['certifications']} professional certifications
        """

        return resume_content.encode('utf-8')

    @staticmethod
    def create_resume_download_button(personal_data: Dict):
        """Create professional resume download button"""
        pdf_content = ResumeManager.generate_pdf_resume(personal_data)

        st.download_button(
            label="📄 Download Professional Resume",
            data=pdf_content,
            file_name="Karim_Osman_Resume_2024.pdf",
            mime="application/pdf",
            use_container_width=True
        )

# SEO and Analytics Utils
class SEOManager:
    """SEO optimization and analytics utilities"""

    @staticmethod
    def add_structured_data(personal_data: Dict):
        """Add structured data for better SEO"""
        structured_data = {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": personal_data['personal_info']['name'],
            "jobTitle": personal_data['personal_info']['title'],
            "url": personal_data['personal_info']['website'],
            "sameAs": [
                personal_data['personal_info']['linkedin'],
                personal_data['personal_info']['github'],
                personal_data['personal_info']['twitter']
            ],
            "knowsAbout": personal_data['professional_summary']['specializations']
        }

        st.markdown(f"""
        <script type="application/ld+json">
        {json.dumps(structured_data, indent=2)}
        </script>
        """, unsafe_allow_html=True)

# Utility Functions
def get_professional_theme():
    """Get professional color theme"""
    return {
        'primary': '#2E86AB',
        'secondary': '#F24236', 
        'accent': '#6C5CE7',
        'neutral': '#6C757D',
        'success': '#28a745',
        'warning': '#ffc107',
        'error': '#dc3545'
    }

def format_currency(amount: float, currency: str = "USD") -> str:
    """Format currency professionally"""
    if currency == "USD":
        return f"${amount:,.0f}"
    return f"{amount:,.0f} {currency}"

def calculate_experience_years(start_date: str) -> int:
    """Calculate years of experience"""
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        return (datetime.now() - start).days // 365
    except:
        return 0

def generate_professional_id(name: str, email: str) -> str:
    """Generate professional ID hash"""
    return hashlib.md5(f"{name}-{email}".encode()).hexdigest()[:8].upper()

# Initialize global instances
data_manager = PortfolioDataManager()
analytics = PortfolioAnalytics()
contact_manager = ContactManager()
resume_manager = ResumeManager()
seo_manager = SEOManager()

# Export all utilities
__all__ = [
    'PortfolioDataManager',
    'PortfolioAnalytics', 
    'ContactManager',
    'ResumeManager',
    'SEOManager',
    'data_manager',
    'analytics',
    'contact_manager',
    'resume_manager',
    'seo_manager',
    'get_professional_theme',
    'format_currency',
    'calculate_experience_years',
    'generate_professional_id'
]
def get_browser_lang() -> str:
    """Detect browser language preference"""
    # In a real app, you would detect the browser language
    # This is a simplified version that always returns English
    return 'en'

def language_selector() -> None:
    """Render language selector UI component"""
    # This function would create a language selection UI
    # Since it's not implemented, we'll just create a placeholder
    with st.sidebar:
        st.markdown("---")
        st.markdown("**Language Settings**")
        st.radio("Language", ["English", "French", "German", "Swedish", "Dutch", "Japanese"], key='lang', index=0)
