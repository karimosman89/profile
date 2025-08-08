import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import json
import numpy as np

def main():
    """Enhanced Projects page with comprehensive case studies"""

    # Page header
    st.markdown("""
    <div class="projects-hero">
        <h1>💼 Project Portfolio</h1>
        <p class="projects-tagline">AI Solutions That Drive Real Business Impact</p>
    </div>
    """, unsafe_allow_html=True)

    # Project statistics overview
    create_project_statistics()

    # Project filters and search
    st.markdown("## 🔍 Explore My Projects")

    filters_col1, filters_col2, filters_col3 = st.columns(3)

    with filters_col1:
        category_filter = st.selectbox(
            "Filter by Category",
            ["All Categories", "AI/ML", "Computer Vision", "NLP", "Data Engineering", "Web Development"],
            key="category_filter"
        )

    with filters_col2:
        tech_filter = st.selectbox(
            "Filter by Technology",
            ["All Technologies", "Python", "TensorFlow", "PyTorch", "AWS", "Docker", "React"],
            key="tech_filter"
        )

    with filters_col3:
        impact_filter = st.selectbox(
            "Sort by Impact",
            ["Most Recent", "Highest Impact", "Most Complex", "Client Favorites"],
            key="impact_filter"
        )

    # Search functionality
    search_query = st.text_input("🔍 Search projects...", placeholder="Enter keywords, technologies, or business domains")

    # Get filtered projects
    projects = get_filtered_projects(category_filter, tech_filter, impact_filter, search_query)

    # Display projects
    st.markdown(f"### Found {len(projects)} Projects")

    # Featured Projects Section
    st.markdown("## 🌟 Featured AI Solutions")
    display_featured_projects()

    # All Projects with Pagination
    st.markdown("## 📋 Complete Project Portfolio")
    display_all_projects(projects)

    # Project Impact Analysis
    st.markdown("## 📊 Project Impact Analysis")
    create_impact_analysis()

def create_project_statistics():
    """Create project statistics overview"""

    st.markdown("## 📈 Portfolio Overview")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Total Projects", "70+", delta="12 this year")

    with col2:
        st.metric("Success Rate", "98%", delta="2% vs industry")

    with col3:
        st.metric("Avg. ROI", "340%", delta="85% above target")

    with col4:
        st.metric("Client Satisfaction", "4.9/5", delta="0.3 vs benchmark")

    with col5:
        st.metric("Technologies", "25+", delta="8 new this year")

def get_filtered_projects(category, technology, impact, search):
    """Get filtered projects based on selection criteria"""

    # Project database
    all_projects = [
        {
            "id": 1,
            "title": "Enterprise RAG System for Legal Analysis",
            "category": "AI/ML",
            "description": "Developed a comprehensive Retrieval-Augmented Generation system for processing and analyzing legal documents with natural language queries.",
            "detailed_description": """This enterprise-grade RAG system revolutionized how legal professionals interact with vast document repositories. The system processes over 100,000 legal documents, enabling lawyers to quickly find relevant information through natural language queries.

Key innovations include:
• Hybrid search combining semantic and keyword matching
• Custom legal domain embeddings
• Multi-level summarization capabilities
• Real-time citation tracking and verification
• Compliance with data privacy regulations""",
            "technologies": ["Python", "LangChain", "FAISS", "HuggingFace", "AWS", "PostgreSQL", "Docker"],
            "duration": "6 months",
            "team_size": 4,
            "client": "International Law Firm",
            "industry": "Legal Services",
            "business_impact": {
                "cost_reduction": "85%",
                "time_savings": "12 hours/day per lawyer",
                "accuracy_improvement": "95%",
                "roi": "450%"
            },
            "technical_challenges": [
                "Processing documents in multiple languages",
                "Maintaining legal accuracy and citations",
                "Scaling to handle 100K+ documents",
                "Ensuring data security and compliance"
            ],
            "solutions": [
                "Implemented multilingual embeddings with legal domain fine-tuning",
                "Built custom citation extraction and verification pipeline",
                "Deployed distributed architecture on AWS with auto-scaling",
                "Integrated enterprise-grade security with audit trails"
            ],
            "metrics": {
                "documents_processed": 150000,
                "queries_per_day": 5000,
                "response_time": "< 2 seconds",
                "accuracy": "95%"
            },
            "demo_url": "https://legal-rag-demo.streamlit.app",
            "github_url": "https://github.com/karimosman89/legal-rag-system",
            "image_url": "https://via.placeholder.com/600x300/667eea/ffffff?text=Legal+RAG+System",
            "status": "Production",
            "date": "2024-11-01"
        },
        {
            "id": 2,
            "title": "Computer Vision Quality Control System",
            "category": "Computer Vision",
            "description": "Real-time defect detection system for manufacturing using advanced computer vision and deep learning techniques.",
            "detailed_description": """Developed an automated quality control system that revolutionized manufacturing inspection processes. The system uses state-of-the-art computer vision algorithms to detect defects in real-time with superhuman accuracy.

System capabilities:
• Real-time defect detection on production lines
• Multi-class defect classification and severity assessment
• Integration with existing manufacturing systems
• Automated reporting and analytics dashboard
• Edge deployment for minimal latency""",
            "technologies": ["PyTorch", "OpenCV", "YOLO", "TensorRT", "Docker", "Kubernetes", "MongoDB"],
            "duration": "4 months",
            "team_size": 3,
            "client": "Manufacturing Corporation",
            "industry": "Manufacturing",
            "business_impact": {
                "defect_detection": "98.7%",
                "false_positive_rate": "0.3%",
                "cost_savings": "$2M annually",
                "production_efficiency": "+15%"
            },
            "technical_challenges": [
                "Real-time processing requirements (30 FPS)",
                "Varying lighting and environmental conditions",
                "Integration with legacy manufacturing systems",
                "Edge deployment constraints"
            ],
            "solutions": [
                "Optimized YOLO architecture with TensorRT acceleration",
                "Implemented adaptive preprocessing for lighting variations",
                "Built REST API bridge for legacy system integration",
                "Deployed containerized edge computing solution"
            ],
            "metrics": {
                "processing_speed": "30 FPS",
                "accuracy": "98.7%",
                "uptime": "99.9%",
                "defects_detected": 25000
            },
            "demo_url": "https://cv-quality-demo.streamlit.app",
            "github_url": "https://github.com/karimosman89/cv-quality-control",
            "image_url": "https://via.placeholder.com/600x300/764ba2/ffffff?text=Computer+Vision+QC",
            "status": "Production",
            "date": "2024-09-15"
        },
        {
            "id": 3,
            "title": "Multilingual Sentiment Analysis Platform",
            "category": "NLP",
            "description": "Advanced sentiment analysis system supporting 12 languages with real-time processing and custom domain adaptation.",
            "detailed_description": """Built a comprehensive sentiment analysis platform that processes multilingual text data in real-time. The system serves multiple clients across different industries, providing accurate sentiment insights for business decision-making.

Platform features:
• Support for 12 languages including Arabic, English, Italian, French, German
• Real-time API with sub-second response times
• Custom domain adaptation for different industries
• Batch processing for large datasets
• Interactive dashboard for analytics and insights""",
            "technologies": ["Python", "Transformers", "FastAPI", "Redis", "PostgreSQL", "React", "Docker"],
            "duration": "3 months",
            "team_size": 2,
            "client": "Social Media Analytics Company",
            "industry": "Social Media",
            "business_impact": {
                "languages_supported": 12,
                "accuracy": "92%",
                "processing_speed": "10K texts/minute",
                "client_retention": "95%"
            },
            "technical_challenges": [
                "Handling multiple languages with varying characteristics",
                "Real-time processing at scale",
                "Domain adaptation across industries",
                "Model interpretability and bias detection"
            ],
            "solutions": [
                "Fine-tuned multilingual BERT models for each language",
                "Implemented Redis caching and load balancing",
                "Built modular pipeline for easy domain customization",
                "Added SHAP explanations for model interpretability"
            ],
            "metrics": {
                "texts_processed": 5000000,
                "avg_response_time": "0.8 seconds",
                "accuracy": "92%",
                "languages": 12
            },
            "demo_url": "https://sentiment-platform-demo.streamlit.app",
            "github_url": "https://github.com/karimosman89/multilingual-sentiment",
            "image_url": "https://via.placeholder.com/600x300/2196f3/ffffff?text=Sentiment+Analysis",
            "status": "Production",
            "date": "2024-08-01"
        },
        {
            "id": 4,
            "title": "Predictive Maintenance AI System",
            "category": "AI/ML",
            "description": "Machine learning system for predicting equipment failures in industrial settings with 88% accuracy.",
            "detailed_description": """Developed an AI-powered predictive maintenance system that transforms how industrial facilities manage equipment maintenance. The system analyzes sensor data to predict failures before they occur, significantly reducing downtime and maintenance costs.

System capabilities:
• Real-time sensor data processing
• Multi-modal failure prediction (mechanical, electrical, thermal)
• Maintenance scheduling optimization
• Cost-benefit analysis and ROI calculations
• Integration with existing CMMS systems""",
            "technologies": ["Python", "scikit-learn", "XGBoost", "TimeSeries", "InfluxDB", "Grafana", "Apache Kafka"],
            "duration": "5 months",
            "team_size": 3,
            "client": "Industrial Manufacturing",
            "industry": "Manufacturing",
            "business_impact": {
                "failure_prediction": "88%",
                "maintenance_cost_reduction": "30%",
                "unplanned_downtime": "-60%",
                "equipment_lifespan": "+25%"
            },
            "technical_challenges": [
                "Handling high-frequency sensor data streams",
                "Dealing with imbalanced failure datasets",
                "Integrating with legacy industrial systems",
                "Ensuring system reliability in harsh environments"
            ],
            "solutions": [
                "Implemented Apache Kafka for real-time data streaming",
                "Used SMOTE and ensemble methods for imbalanced data",
                "Built robust API layer with comprehensive error handling",
                "Deployed on-premise solution with edge computing capabilities"
            ],
            "metrics": {
                "sensors_monitored": 2500,
                "prediction_accuracy": "88%",
                "maintenance_savings": "$500K annually",
                "uptime_improvement": "15%"
            },
            "demo_url": "https://predictive-maintenance-demo.streamlit.app",
            "github_url": "https://github.com/karimosman89/predictive-maintenance",
            "image_url": "https://via.placeholder.com/600x300/4caf50/ffffff?text=Predictive+Maintenance",
            "status": "Production",
            "date": "2024-06-01"
        },
        {
            "id": 5,
            "title": "Financial Trading Algorithm with ML",
            "category": "AI/ML",
            "description": "Advanced algorithmic trading system using machine learning for portfolio optimization and risk management.",
            "detailed_description": """Created a sophisticated algorithmic trading system that combines machine learning with traditional financial analysis. The system manages portfolios autonomously while maintaining strict risk controls and regulatory compliance.

Key features:
• Multi-strategy portfolio optimization
• Real-time market sentiment analysis
• Risk management with dynamic position sizing
• Regulatory compliance and audit trails
• Backtesting framework with walk-forward analysis""",
            "technologies": ["Python", "scikit-learn", "pandas", "NumPy", "SQLAlchemy", "FastAPI", "React"],
            "duration": "8 months",
            "team_size": 2,
            "client": "Investment Management Firm",
            "industry": "Finance",
            "business_impact": {
                "portfolio_return": "18.5% annually",
                "sharpe_ratio": "1.8",
                "max_drawdown": "-8.2%",
                "assets_under_management": "$25M"
            },
            "technical_challenges": [
                "Handling high-frequency financial data",
                "Ensuring low-latency trade execution",
                "Managing portfolio risk in volatile markets",
                "Regulatory compliance and reporting"
            ],
            "solutions": [
                "Optimized data pipeline with in-memory processing",
                "Implemented direct market access (DMA) integration",
                "Built comprehensive risk management framework",
                "Created automated compliance reporting system"
            ],
            "metrics": {
                "trades_executed": 50000,
                "avg_execution_time": "50ms",
                "win_rate": "68%",
                "volatility": "12.5%"
            },
            "demo_url": "https://trading-algorithm-demo.streamlit.app",
            "github_url": "https://github.com/karimosman89/trading-algorithm",
            "image_url": "https://via.placeholder.com/600x300/ff9800/ffffff?text=Trading+Algorithm",
            "status": "Production",
            "date": "2024-03-01"
        }
    ]

    # Apply filters
    filtered_projects = all_projects

    if category != "All Categories":
        filtered_projects = [p for p in filtered_projects if p["category"] == category]

    if technology != "All Technologies":
        filtered_projects = [p for p in filtered_projects if technology in p["technologies"]]

    if search:
        search_lower = search.lower()
        filtered_projects = [p for p in filtered_projects 
                           if search_lower in p["title"].lower() 
                           or search_lower in p["description"].lower()
                           or any(search_lower in tech.lower() for tech in p["technologies"])]

    # Apply sorting
    if impact == "Most Recent":
        filtered_projects.sort(key=lambda x: x["date"], reverse=True)
    elif impact == "Highest Impact":
        filtered_projects.sort(key=lambda x: float(x["business_impact"]["roi"].rstrip("%")), reverse=True)

    return filtered_projects

def display_featured_projects():
    """Display featured projects with enhanced visualization"""

    featured_ids = [1, 2, 3]  # Featured project IDs
    projects = get_filtered_projects("All Categories", "All Technologies", "Most Recent", "")
    featured_projects = [p for p in projects if p["id"] in featured_ids]

    for project in featured_projects:
        with st.container():
            st.markdown(f"""
            <div class="featured-project-card">
                <div class="project-header">
                    <h3>{project['title']}</h3>
                    <span class="project-status {project['status'].lower()}">{project['status']}</span>
                </div>
                <div class="project-meta">
                    <span class="project-category">{project['category']}</span>
                    <span class="project-duration">{project['duration']}</span>
                    <span class="project-team">Team of {project['team_size']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns([2, 1])

            with col1:
                st.markdown(project["detailed_description"])

                # Technical details
                with st.expander("🔧 Technical Implementation"):
                    st.markdown("**Technologies Used:**")
                    tech_cols = st.columns(4)
                    for i, tech in enumerate(project["technologies"]):
                        with tech_cols[i % 4]:
                            st.markdown(f"`{tech}`")

                    st.markdown("**Technical Challenges:**")
                    for challenge in project["technical_challenges"]:
                        st.markdown(f"• {challenge}")

                    st.markdown("**Solutions Implemented:**")
                    for solution in project["solutions"]:
                        st.markdown(f"✓ {solution}")

                # Business impact
                with st.expander("📈 Business Impact & Results"):
                    impact_cols = st.columns(2)
                    with impact_cols[0]:
                        for key, value in project["business_impact"].items():
                            st.metric(key.replace("_", " ").title(), value)

                    with impact_cols[1]:
                        st.markdown("**Key Metrics:**")
                        for key, value in project["metrics"].items():
                            st.markdown(f"• **{key.replace('_', ' ').title()}**: {value}")

            with col2:
                # Project image
                st.image(project["image_url"], caption=project["title"], use_container_width=True)

                # Action buttons
                btn_col1, btn_col2 = st.columns(2)
                with btn_col1:
                    if st.button(f"🔗 Live Demo", key=f"demo_{project['id']}"):
                        st.success(f"Opening demo for {project['title']}")
                        # In real implementation, this would open the demo URL

                with btn_col2:
                    if st.button(f"📝 GitHub", key=f"github_{project['id']}"):
                        st.success(f"Opening GitHub repository")
                        # In real implementation, this would open the GitHub URL

                # Project stats
                st.markdown("### 📊 Quick Stats")
                st.markdown(f"**Client:** {project['client']}")
                st.markdown(f"**Industry:** {project['industry']}")
                st.markdown(f"**Duration:** {project['duration']}")
                st.markdown(f"**Team Size:** {project['team_size']}")

            st.markdown("---")

def display_all_projects(projects):
    """Display all projects with pagination"""

    # Pagination
    projects_per_page = 5
    total_pages = (len(projects) - 1) // projects_per_page + 1

    if total_pages > 1:
        page = st.selectbox("Select Page", range(1, total_pages + 1), key="project_page")
        start_idx = (page - 1) * projects_per_page
        end_idx = start_idx + projects_per_page
        page_projects = projects[start_idx:end_idx]
    else:
        page_projects = projects

    # Display projects in cards
    for project in page_projects:
        with st.container():
            col1, col2, col3 = st.columns([2, 1, 1])

            with col1:
                st.markdown(f"### {project['title']}")
                st.markdown(project["description"])

                # Technology badges
                tech_html = ""
                for tech in project["technologies"][:5]:  # Show first 5 technologies
                    tech_html += f'<span class="tech-badge">{tech}</span> '
                if len(project["technologies"]) > 5:
                    tech_html += f'<span class="tech-badge">+{len(project["technologies"]) - 5} more</span>'

                st.markdown(f'<div class="tech-badges">{tech_html}</div>', unsafe_allow_html=True)

            with col2:
                st.markdown("**Business Impact**")
                impact_key = list(project["business_impact"].keys())[0]
                impact_value = project["business_impact"][impact_key]
                st.metric(impact_key.replace("_", " ").title(), impact_value)

            with col3:
                st.markdown("**Project Details**")
                st.markdown(f"**Category:** {project['category']}")
                st.markdown(f"**Status:** {project['status']}")
                st.markdown(f"**Duration:** {project['duration']}")

            # Expandable details
            with st.expander("View Full Details"):
                detail_col1, detail_col2 = st.columns([2, 1])

                with detail_col1:
                    st.markdown("**Detailed Description:**")
                    st.markdown(project["detailed_description"])

                    st.markdown("**Technologies:**")
                    tech_cols = st.columns(4)
                    for i, tech in enumerate(project["technologies"]):
                        with tech_cols[i % 4]:
                            st.markdown(f"`{tech}`")

                with detail_col2:
                    st.markdown("**Business Impact:**")
                    for key, value in project["business_impact"].items():
                        st.markdown(f"• **{key.replace('_', ' ').title()}**: {value}")

                    st.markdown("**Technical Metrics:**")
                    for key, value in project["metrics"].items():
                        st.markdown(f"• **{key.replace('_', ' ').title()}**: {value}")

            st.markdown("---")

def create_impact_analysis():
    """Create project impact analysis dashboard"""

    # Sample impact data
    impact_data = {
        'Project': ['Legal RAG System', 'CV Quality Control', 'Sentiment Analysis', 'Predictive Maintenance', 'Trading Algorithm'],
        'ROI (%)': [450, 280, 320, 380, 185],
        'Cost Savings ($K)': [850, 2000, 450, 500, 1250],
        'Time Savings (hrs/week)': [60, 40, 25, 35, 20],
        'Accuracy (%)': [95, 98.7, 92, 88, 68]
    }

    df = pd.DataFrame(impact_data)

    col1, col2 = st.columns(2)

    with col1:
        # ROI Chart
        fig_roi = px.bar(df, x='Project', y='ROI (%)', 
                        title='Return on Investment by Project',
                        color='ROI (%)', 
                        color_continuous_scale='viridis')
        fig_roi.update_xaxis(tickangle=45)
        st.plotly_chart(fig_roi, use_container_width=True)

    with col2:
        # Accuracy vs Cost Savings Scatter
        fig_scatter = px.scatter(df, x='Accuracy (%)', y='Cost Savings ($K)',
                               size='ROI (%)', hover_name='Project',
                               title='Accuracy vs Cost Savings',
                               color='ROI (%)', 
                               color_continuous_scale='plasma')
        st.plotly_chart(fig_scatter, use_container_width=True)

    # Technology usage analysis
    st.markdown("### 🛠️ Technology Stack Analysis")

    # Sample technology data
    tech_usage = {
        'Python': 5, 'PyTorch': 2, 'TensorFlow': 2, 'Docker': 4, 'AWS': 3,
        'FastAPI': 3, 'React': 2, 'PostgreSQL': 3, 'MongoDB': 1, 'Redis': 2
    }

    fig_tech = px.bar(x=list(tech_usage.keys()), y=list(tech_usage.values()),
                     title='Technology Usage Across Projects',
                     labels={'x': 'Technology', 'y': 'Number of Projects'})
    fig_tech.update_traces(marker_color='#667eea')
    st.plotly_chart(fig_tech, use_container_width=True)

if __name__ == "__main__":
    main()
