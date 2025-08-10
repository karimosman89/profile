import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
import base64
from app_utils  import tr

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
        
        .projects-hero {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 3rem;
            margin: 2rem 0;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            text-align: center;
        }
        
        .project-card {
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            border-left: 5px solid #667eea;
            position: relative;
            overflow: hidden;
        }
        
        .project-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
            border-left-color: #764ba2;
        }
        
        .project-card::before {
            content: \'\';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #667eea, #764ba2, #667eea);
            background-size: 200% 100%;
            animation: gradient-shift 3s ease-in-out infinite;
        }
        
        @keyframes gradient-shift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        .project-header {
            display: flex;
            align-items: center;
            margin-bottom: 1.5rem;
        }
        
        .project-icon {
            font-size: 3rem;
            margin-right: 1rem;
            background: linear-gradient(145deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .project-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #333;
            margin: 0;
        }
        
        .project-subtitle {
            font-size: 1rem;
            color: #667eea;
            font-weight: 500;
            margin: 0;
        }
        
        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin: 1rem 0;
        }
        
        .tech-tag {
            background: linear-gradient(145deg, #667eea, #764ba2);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 15px;
            font-size: 0.8rem;
            font-weight: 500;
        }
        
        .impact-metrics {
            background: linear-gradient(145deg, #e8f5e8, #c8e6c9);
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
            border-left: 4px solid #28a745;
        }
        
        .demo-section {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
            border: 2px dashed #667eea;
        }
        
        .field-category {
            background: linear-gradient(145deg, #fff3e0, #ffe0b2);
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            border-left: 5px solid #ff9800;
        }
        
        .field-category h2 {
            color: #e65100;
            margin-bottom: 1.5rem;
            text-align: center;
        }
        
        .project-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 10px;
            margin: 1rem 0;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .github-link {
            background: #333;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            display: inline-block;
            margin: 0.5rem 0;
            transition: all 0.3s ease;
        }
        
        .github-link:hover {
            background: #555;
            transform: translateY(-2px);
        }
        
        .live-demo-btn {
            background: linear-gradient(145deg, #28a745, #20c997);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            display: inline-block;
            margin: 0.5rem 0.5rem 0.5rem 0;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
        }
        
        .live-demo-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(40, 167, 69, 0.3);
        }
    </style>
    """, unsafe_allow_html=True)

set_style()

# Hero Section
st.markdown(f"""
<div class="projects-hero">
    <h1>🚀 AI Projects Portfolio</h1>
    <p style="font-size: 1.2rem; color: #555; margin-bottom: 1rem;">
        Comprehensive showcase of AI engineering across multiple domains
    </p>
    <p style="font-size: 1rem; color: #666;">
        From Computer Vision to Generative AI - Real-world applications with measurable impact
    </p>
</div>
""", unsafe_allow_html=True)

# Computer Vision Projects
st.markdown("""
<div class="field-category">
    <h2>👁️ Computer Vision & Image Processing</h2>
</div>
""", unsafe_allow_html=True)

cv_projects = [
    {
        "title": "Real-Time Object Detection System",
        "subtitle": "YOLO-based Multi-Object Recognition",
        "icon": "📹",
        "description": "Advanced real-time object detection system capable of identifying and tracking multiple objects simultaneously with 95% accuracy.",
        "tech_stack": ["Python", "YOLO v8", "OpenCV", "PyTorch", "CUDA", "Flask"],
        "impact": {
            "accuracy": "95.2%",
            "fps": "60 FPS",
            "objects": "80+ Classes",
            "deployment": "Production Ready"
        },
        "features": [
            "Real-time processing at 60 FPS",
            "Multi-object tracking with unique IDs",
            "Custom model training pipeline",
            "REST API for integration",
            "Mobile-optimized inference"
        ],
        "image": "assets/computer_vision_demo.png"
    },
    {
        "title": "Medical Image Analysis Platform",
        "subtitle": "AI-Powered Diagnostic Assistant",
        "icon": "🏥",
        "description": "Deep learning system for medical image analysis, specializing in X-ray and MRI scan interpretation with radiologist-level accuracy.",
        "tech_stack": ["TensorFlow", "Keras", "DICOM", "NumPy", "Streamlit", "Docker"],
        "impact": {
            "accuracy": "97.8%",
            "processing_time": "< 2 seconds",
            "cases_analyzed": "10,000+",
            "hospitals": "5 Deployed"
        },
        "features": [
            "Multi-modal medical image support",
            "Automated report generation",
            "HIPAA-compliant data handling",
            "Integration with hospital systems",
            "Continuous learning pipeline"
        ],
        "image": "assets/ai_brain_network.png"
    },
    {
        "title": "Facial Recognition & Emotion Detection",
        "subtitle": "Advanced Biometric Analysis",
        "icon": "😊",
        "description": "Comprehensive facial analysis system combining recognition, emotion detection, and demographic analysis for security and marketing applications.",
        "tech_stack": ["OpenCV", "dlib", "FaceNet", "TensorFlow", "Redis", "MongoDB"],
        "impact": {
            "recognition_accuracy": "99.1%",
            "emotion_accuracy": "94.5%",
            "processing_speed": "Real-time",
            "database_size": "1M+ faces"
        },
        "features": [
            "Multi-face detection and tracking",
            "7-emotion classification system",
            "Age and gender estimation",
            "Anti-spoofing mechanisms",
            "Privacy-preserving features"
        ]
    }
]

for project in cv_projects:
    st.markdown(f"""
    <div class="project-card">
        <div class="project-header">
            <div class="project-icon">{project['icon']}</div>
            <div>
                <h3 class="project-title">{project['title']}</h3>
                <p class="project-subtitle">{project['subtitle']}</p>
            </div>
        </div>
        
        <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 1.5rem;">
            {project['description']}
        </p>
        
        <div class="tech-stack">
            {' '.join([f'<span class="tech-tag">{tech}</span>' for tech in project['tech_stack']])}
        </div>
        
        <div class="impact-metrics">
            <h4 style="color: #2e7d32; margin-bottom: 1rem;">📊 Impact Metrics:</h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;">
                {' '.join([f'<div><strong>{key.replace("_", " ").title()}:</strong><br>{value}</div>' for key, value in project['impact'].items()])}
            </div>
       
        </div>
        
        <div style="margin: 1.5rem 0;">
            <h4>✨ Key Features:</h4>
            <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                {''.join([f'<li>{feature}</li>' for feature in project['features']])}
            </ul>
        </div>
        
        <div style="margin-top: 1.5rem;">
            <button class="live-demo-btn" onclick="alert(\'Live demo would be available in production deployment\')">
                🚀 Live Demo
            </button>
            <a href="#" class="github-link">
                📂 View Code
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add project image if available
    if 'image' in project:
        try:
            img = Image.open(project['image'])
            st.image(img, caption=f'{project["title"]} - Visual Demo', use_column_width=True)
        except:
            pass

# Natural Language Processing Projects
st.markdown("""
<div class="field-category">
    <h2>🗣️ Natural Language Processing & LLMs</h2>
</div>
""", unsafe_allow_html=True)

nlp_projects = [
    {
        "title": "Enterprise RAG System",
        "subtitle": "Retrieval-Augmented Generation Platform",
        "icon": "🧠",
        "description": "Scalable RAG system that transforms enterprise knowledge bases into intelligent Q&A systems, serving 10,000+ daily queries.",
        "tech_stack": ["LangChain", "OpenAI GPT-4", "Pinecone", "FastAPI", "Redis", "PostgreSQL"],
        "impact": {
            "daily_queries": "10,000+",
            "accuracy": "92.5%",
            "response_time": "< 3 seconds",
            "cost_reduction": "60%"
        },
        "features": [
            "Multi-document knowledge synthesis",
            "Real-time vector search optimization",
            "Context-aware response generation",
            "Multi-language support (12 languages)",
            "Enterprise security compliance"
        ],
        "image": "assets/nlp_processing.png"
    },
    {
        "title": "Multilingual Sentiment Analysis API",
        "subtitle": "Global Social Media Monitoring",
        "icon": "🌍",
        "description": "Advanced sentiment analysis system supporting 25+ languages with cultural context awareness for global brand monitoring.",
        "tech_stack": ["Transformers", "BERT", "XLM-R", "FastAPI", "Kafka", "Elasticsearch"],
        "impact": {
            "languages": "25+",
            "accuracy": "94.2%",
            "throughput": "1M tweets/hour",
            "clients": "50+ brands"
        },
        "features": [
            "Cross-lingual sentiment transfer",
            "Cultural context adaptation",
            "Real-time stream processing",
            "Aspect-based sentiment analysis",
            "Trend detection and alerting"
        ]
    },
    {
        "title": "AI-Powered Content Generator",
        "subtitle": "Creative Writing Assistant",
        "icon": "✍️",
        "description": "Intelligent content generation platform for marketing teams, creating personalized content at scale with brand voice consistency.",
        "tech_stack": ["GPT-3.5/4", "LangChain", "Streamlit", "MongoDB", "Celery", "AWS"],
        "impact": {
            "content_pieces": "100,000+",
            "time_saved": "80%",
            "engagement_boost": "45%",
            "active_users": "500+"
        },
        "features": [
            "Brand voice customization",
            "Multi-format content generation",
            "SEO optimization integration",
            "Plagiarism detection",
            "A/B testing capabilities"
        ]
    }
]

for project in nlp_projects:
    st.markdown(f"""
    <div class="project-card">
        <div class="project-header">
            <div class="project-icon">{project['icon']}</div>
            <div>
                <h3 class="project-title">{project[\'title\']}</h3>
                <p class="project-subtitle">{project[\'subtitle\]}</p>
            </div>
        </div>
        
        <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 1.5rem;">
            {project[\'description\]}
        </p>
        
        <div class="tech-stack">
            {\' \'.join([f\'<span class="tech-tag">{tech}</span>\' for tech in project[\'tech_stack\']])}
        </div>
        
        <div class="impact-metrics">
            <h4 style="color: #2e7d32; margin-bottom: 1rem;">📊 Impact Metrics:</h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;">
                {\' \'.join([f\'<div><strong>{key.replace("_", " ").title()}:</strong><br>{value}</div>\' for key, value in project[\'impact\'].items()])}
            </div>
        </div>
        
        <div style="margin: 1.5rem 0;">
            <h4>✨ Key Features:</h4>
            <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                {\' \'.join([f\'<li>{feature}</li>\' for feature in project[\'features\']])}
            </ul>
        </div>
        
        <div style="margin-top: 1.5rem;">
            <button class="live-demo-btn" onclick="alert(\'Live demo would be available in production deployment\')">
                🚀 Live Demo
            </button>
            <a href="#" class="github-link">
                📂 View Code
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add project image if available
    if \'image\' in project:
        try:
            img = Image.open(project[\'image\'])
            st.image(img, caption=f"{project[\'title\]} - Architecture Overview", use_column_width=True)
        except:
            pass

# Machine Learning & Data Science Projects
st.markdown("""
<div class="field-category">
    <h2>📊 Machine Learning & Predictive Analytics</h2>
</div>
""", unsafe_allow_html=True)

ml_projects = [
    {
        "title": "Predictive Maintenance System",
        "subtitle": "Industrial IoT Analytics",
        "icon": "🏭",
        "description": "ML-powered predictive maintenance system for manufacturing equipment, reducing downtime by 40% through early failure detection.",
        "tech_stack": ["Scikit-learn", "XGBoost", "Apache Spark", "Kafka", "InfluxDB", "Grafana"],
        "impact": {
            "downtime_reduction": "40%",
            "cost_savings": "$2.5M/year",
            "prediction_accuracy": "89.3%",
            "equipment_monitored": "500+ units"
        },
        "features": [
            "Real-time sensor data processing",
            "Anomaly detection algorithms",
            "Failure prediction with confidence intervals",
            "Maintenance scheduling optimization",
            "Interactive monitoring dashboards"
        ]
    },
    {
        "title": "Financial Risk Assessment AI",
        "subtitle": "Credit Scoring & Fraud Detection",
        "icon": "💰",
        "description": "Advanced ML system for financial risk assessment, combining credit scoring and fraud detection with explainable AI features.",
        "tech_stack": ["Python", "LightGBM", "SHAP", "MLflow", "Docker", "Kubernetes"],
        "impact": {
            "fraud_detection": "96.8%",
            "false_positives": "< 2%",
            "processing_speed": "< 100ms",
            "loans_processed": "1M+"
        },
        "features": [
            "Real-time fraud scoring",
            "Explainable AI decisions",
            "Regulatory compliance (GDPR, CCPA)",
            "A/B testing framework",
            "Continuous model monitoring"
        ]
    },
    {
        "title": "Customer Behavior Analytics",
        "subtitle": "E-commerce Personalization Engine",
        "icon": "🛒",
        "description": "Comprehensive customer analytics platform driving personalized shopping experiences and increasing conversion rates by 35%.",
        "tech_stack": ["TensorFlow", "Pandas", "Redis", "Apache Airflow", "BigQuery", "Tableau"],
        "impact": {
            "conversion_increase": "35%",
            "revenue_boost": "$5M+",
            "customers_analyzed": "2M+",
            "recommendations": "Real-time"
        },
        "features": [
            "Real-time recommendation engine",
            "Customer lifetime value prediction",
            "Churn prediction and prevention",
            "Dynamic pricing optimization",
            "Multi-channel attribution modeling"
        ]
    }
]

for project in ml_projects:
    st.markdown(f"""
    <div class="project-card">
        <div class="project-header">
            <div class="project-icon">{project[\'icon\']}</div>
            <div>
                <h3 class="project-title">{project[\'title\']}</h3>
                <p class="project-subtitle">{project[\'subtitle\]}</p>
            </div>
        </div>
        
        <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 1.5rem;">
            {project[\'description\]}
        </p>
        
        <div class="tech-stack">
            {\' \'.join([f\'<span class="tech-tag">{tech}</span>\' for tech in project[\'tech_stack\']])}
        </div>
        
        <div class="impact-metrics">
            <h4 style="color: #2e7d32; margin-bottom: 1rem;">📊 Impact Metrics:</h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;">
                {\' \'.join([f\'<div><strong>{key.replace("_", " ").title()}:</strong><br>{value}</div>\' for key, value in project[\'impact\'].items()])}
            </div>
        </div>
        
        <div style="margin: 1.5rem 0;">
            <h4>✨ Key Features:</h4>
            <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                {\' \'.join([f\'<li>{feature}</li>\' for feature in project[\'features\']])}
            </ul>
        </div>
        
        <div style="margin-top: 1.5rem;">
            <button class="live-demo-btn" onclick="alert(\'Live demo would be available in production deployment\')">
                🚀 Live Demo
            </button>
            <a href="#" class="github-link">
                📂 View Code
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Generative AI Projects
st.markdown("""
<div class="field-category">
    <h2>🎨 Generative AI & Creative Applications</h2>
</div>
""", unsafe_allow_html=True)

gen_ai_projects = [
    {
        "title": "AI Art Generation Platform",
        "subtitle": "Text-to-Image Creative Studio",
        "icon": "🎨",
        "description": "Advanced generative AI platform for creating custom artwork, logos, and designs from text descriptions with commercial licensing.",
        "tech_stack": ["Stable Diffusion", "DALL-E", "Midjourney API", "FastAPI", "React", "AWS S3"],
        "impact": {
            "images_generated": "500,000+",
            "active_artists": "10,000+",
            "revenue": "$100K+/month",
            "generation_time": "< 30 seconds"
        },
        "features": [
            "Multiple AI model integration",
            "Style transfer and customization",
            "Batch generation capabilities",
            "Commercial licensing management",
            "Community gallery and sharing"
        ],
        "image": "assets/generative_ai_art.png"
    },
    {
        "title": "AI Music Composition Assistant",
        "subtitle": "Intelligent Music Creation Tool",
        "icon": "🎵",
        "description": "AI-powered music composition platform helping musicians create original melodies, harmonies, and full arrangements across multiple genres.",
        "tech_stack": ["Magenta", "TensorFlow", "MIDI", "PyTorch", "Flask", "MongoDB"],
        "impact": {
            "compositions": "50,000+",
            "musicians": "5,000+",
            "genres": "20+",
            "avg_rating": "4.8/5"
        },
        "features": [
            "Multi-genre composition support",
            "Real-time collaboration tools",
            "MIDI export and integration",
            "Style adaptation algorithms",
            "Copyright-safe generation"
        ]
    },
    {
        "title": "Synthetic Data Generation Suite",
        "subtitle": "Privacy-Preserving Data Creation",
        "icon": "🔒",
        "description": "Enterprise-grade synthetic data generation platform creating realistic datasets while preserving privacy and regulatory compliance.",
        "tech_stack": ["GANs", "VAEs", "Differential Privacy", "PyTorch", "Kubernetes", "PostgreSQL"],
        "impact": {
            "datasets_created": "1,000+",
            "privacy_score": "99.9%",
            "enterprises": "50+",
            "data_points": "100M+"
        },
        "features": [
            "Multi-modal data synthesis",
            "Differential privacy guarantees",
            "Statistical fidelity preservation",
            "Regulatory compliance (GDPR, HIPAA)",
            "Custom model training"
        ]
    }
]

for project in gen_ai_projects:
    st.markdown(f"""
    <div class="project-card">
        <div class="project-header">
            <div class="project-icon">{project[\'icon\']}</div>
            <div>
                <h3 class="project-title">{project[\'title\']}</h3>
                <p class="project-subtitle">{project[\'subtitle\]}</p>
            </div>
        </div>
        
        <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 1.5rem;">
            {project[\'description\]}
        </p>
        
        <div class="tech-stack">
            {\' \'.join([f\'<span class="tech-tag">{tech}</span>\' for tech in project[\'tech_stack\']])}
        </div>
        
        <div class="impact-metrics">
            <h4 style="color: #2e7d32; margin-bottom: 1rem;">📊 Impact Metrics:</h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;">
                {\' \'.join([f\'<div><strong>{key.replace("_", " ").title()}:</strong><br>{value}</div>\' for key, value in project[\'impact\'].items()])}
            </div>
        </div>
        
        <div style="margin: 1.5rem 0;">
            <h4>✨ Key Features:</h4>
            <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                {\' \'.join([f\'<li>{feature}</li>\' for feature in project[\'features\']])}
            </ul>
        </div>
        
        <div style="margin-top: 1.5rem;">
            <button class="live-demo-btn" onclick="alert(\'Live demo would be available in production deployment\')">
                🚀 Live Demo
            </button>
            <a href="#" class="github-link">
                📂 View Code
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add project image if available
    if \'image\' in project:
        try:
            img = Image.open(project[\'image\'])
            st.image(img, caption=f"{project[\'title\]} - Creative Output", use_column_width=True)
        except:
            pass

# Portfolio Summary
st.markdown(f"""
<div class="projects-hero">
    <h2>🎯 Portfolio Impact Summary</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin: 2rem 0;">
        <div style="text-align: center;">
            <h3 style="color: #667eea; font-size: 2.5rem; margin: 0;">15+</h3>
            <p style="margin: 0; color: #666;">Major Projects</p>
        </div>
        <div style="text-align: center;">
            <h3 style="color: #667eea; font-size: 2.5rem; margin: 0;">$10M+</h3>
            <p style="margin: 0; color: #666;">Business Value</p>
        </div>
        <div style="text-align: center;">
            <h3 style="color: #667eea; font-size: 2.5rem; margin: 0;">95%+</h3>
            <p style="margin: 0; color: #666;">Avg. Accuracy</p>
        </div>
        <div style="text-align: center;">
            <h3 style="color: #667eea; font-size: 2.5rem; margin: 0;">100+</h3>
            <p style="margin: 0; color: #666;">Enterprise Clients</p>
        </div>
    </div>
    <p style="font-size: 1.1rem; color: #666; margin-top: 2rem;">
        Each project represents real-world AI applications with measurable business impact across diverse industries and use cases.
    </p>
</div>
""", unsafe_allow_html=True)

# Call to Action
st.markdown(f"""
<div class="projects-hero">
    <h2>🤝 Ready to Build the Future Together?</h2>
    <p style="font-size: 1.2rem; color: #555; margin-top: 2rem;">
        These projects showcase my ability to deliver AI solutions across the entire spectrum of artificial intelligence applications.
    </p>
    <p style="font-size: 1.1rem; color: #666; margin-top: 1rem;">
        Let\'s discuss how I can bring similar innovation and impact to your organization.
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<p style=\'text-align: center; color: #666; margin-top: 2rem;\'>© 2024 Karim Osman - AI Engineer Portfolio</p>", unsafe_allow_html=True)


