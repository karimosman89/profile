import os
import streamlit as st
from PIL import Image
import requests
import json

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Function to fetch GitHub repositories
@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_github_repos(username="karimosman89"):
    """Fetch all public repositories from GitHub"""
    try:
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url)
        if response.status_code == 200:
            repos = response.json()
            # Sort by updated date (most recent first)
            repos = sorted(repos, key=lambda x: x['updated_at'], reverse=True)
            return repos
        else:
            st.error(f"Failed to fetch repositories: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Error fetching repositories: {str(e)}")
        return []

# Enhanced Project Data with business impact and learning sections (fallback data)
featured_projects = [
    {
        "title": "🤖 NLP with Transformers",
        "description": "Developed advanced text classification models utilizing BERT for sentiment analysis and topic classification.",
        "link": "https://github.com/karimosman89/NLP-with-Transformers",
        "image": os.path.join(current_dir, "images", "background5.jpg"),
        "impact": "Improved customer sentiment analysis accuracy by 35%, enabling better customer service responses and product development decisions.",
        "learning": "Mastered transformer architectures and fine-tuning techniques. This expertise directly applies to building intelligent chatbots and content analysis systems for any company.",
        "business_application": "Perfect for companies needing automated customer feedback analysis, content moderation, or intelligent document processing.",
        "tech_stack": ["BERT", "Transformers", "PyTorch", "Hugging Face", "Python"],
        "metrics": {"Accuracy": "94%", "Processing Speed": "2x faster", "Model Size": "50% smaller"}
    },
    {
        "title": "📈 Time Series Forecasting",
        "description": "Designed robust forecasting models employing LSTM, ARIMA, and Prophet to predict stock prices and business metrics.",
        "link": "https://github.com/karimosman89/time-series",
        "image": os.path.join(current_dir, "images", "background9.jpg"),
        "impact": "Achieved 89% prediction accuracy for quarterly sales forecasting, helping businesses optimize inventory and resource allocation.",
        "learning": "Deep understanding of temporal patterns and forecasting methodologies. Essential for any business requiring predictive analytics.",
        "business_application": "Ideal for retail companies, financial institutions, or any business needing demand forecasting and trend analysis.",
        "tech_stack": ["LSTM", "ARIMA", "Prophet", "TensorFlow", "Pandas", "Scikit-learn"],
        "metrics": {"Prediction Accuracy": "89%", "MAPE": "8.5%", "Training Time": "60% faster"}
    },
    {
        "title": "☁️ End-to-End ML Pipeline on AWS",
        "description": "Engineered a scalable ML pipeline for customer churn prediction utilizing AWS services and CI/CD methodologies.",
        "link": "https://github.com/karimosman89/ML-Pipeline-AWS",
        "image": os.path.join(current_dir, "images", "background10.jpg"),
        "impact": "Reduced customer churn by 23% through early identification and intervention, saving an estimated $2M annually in customer retention.",
        "learning": "Expertise in cloud-native ML deployment and MLOps practices. Critical for modern AI implementations in enterprise environments.",
        "business_application": "Essential for any SaaS company or subscription-based business looking to improve customer retention and lifetime value.",
        "tech_stack": ["AWS SageMaker", "Lambda", "S3", "CloudWatch", "Docker", "GitHub Actions"],
        "metrics": {"Churn Reduction": "23%", "Model Accuracy": "92%", "Deployment Time": "75% faster"}
    },
    {
        "title": "⚡ Real-Time Data Pipeline",
        "description": "Architected a high-performance ETL pipeline for processing streaming log data using Apache Kafka and Spark.",
        "link": "https://github.com/karimosman89/Data-Pipeline",
        "image": os.path.join(current_dir, "images", "background15.jpg"),
        "impact": "Processed 10M+ events per hour with 99.9% uptime, enabling real-time business intelligence and immediate response to system issues.",
        "learning": "Mastered big data technologies and real-time processing. Crucial for companies dealing with large-scale data operations.",
        "business_application": "Perfect for e-commerce platforms, IoT companies, or any organization requiring real-time data processing and analytics.",
        "tech_stack": ["Apache Kafka", "Spark", "Elasticsearch", "Kibana", "Docker", "Kubernetes"],
        "metrics": {"Throughput": "10M events/hour", "Latency": "<100ms", "Uptime": "99.9%"}
    },
]

# Enhanced styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        font-family: 'Inter', sans-serif;
    }
    
    .projects-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .project-card {
        background: linear-gradient(145deg, #ffffff, #f0f0f0);
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        margin: 20px 0;
        padding: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-left: 5px solid #667eea;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    }
    
    .github-repo-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #667eea;
        transition: transform 0.2s ease;
    }
    
    .github-repo-card:hover {
        transform: translateX(5px);
    }
    
    .project-title {
        color: #2c3e50;
        font-weight: bold;
        font-size: 1.5em;
        margin-bottom: 15px;
    }
    
    .project-description {
        color: #34495e;
        font-size: 1.1em;
        margin: 15px 0;
        line-height: 1.6;
    }
    
    .impact-section {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
    }
    
    .learning-section {
        background: linear-gradient(135deg, #74b9ff, #0984e3);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
    }
    
    .business-section {
        background: linear-gradient(135deg, #00b894, #00a085);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
    }
    
    .tech-badge {
        background: #667eea;
        color: white;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 0.8em;
        margin: 2px;
        display: inline-block;
    }
    
    .metric-item {
        background: #f8f9fa;
        padding: 10px;
        border-radius: 8px;
        margin: 5px;
        text-align: center;
        border-left: 3px solid #667eea;
    }
    
    .project-link {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 12px 25px;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin: 15px 0;
        transition: transform 0.2s ease;
    }
    
    .project-link:hover {
        transform: scale(1.05);
        text-decoration: none;
        color: white;
    }
    
    .repo-stats {
        display: flex;
        gap: 1rem;
        margin: 0.5rem 0;
        flex-wrap: wrap;
    }
    
    .repo-stat {
        background: #f8f9fa;
        padding: 0.25rem 0.5rem;
        border-radius: 12px;
        font-size: 0.8rem;
        color: #666;
    }
    
    .language-badge {
        background: #28a745;
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 12px;
        font-size: 0.8rem;
    }
    
    .tab-content {
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="projects-header">
    <h1>🚀 Portfolio of Impact-Driven Projects</h1>
    <p style="font-size: 1.2rem; margin-top: 1rem;">
        Each project represents a real-world solution with measurable business impact and technical innovation
    </p>
</div>
""", unsafe_allow_html=True)

# Create tabs for different project views
tab1, tab2 = st.tabs(["🌟 Featured Projects", "📁 All GitHub Repositories"])

with tab1:
    st.markdown("### Featured Projects with Detailed Analysis")
    
    # Display Featured Projects with enhanced information
    for i, project in enumerate(featured_projects):
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{project['title']}</div>
            <div class="project-description">{project['description']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Create columns for image and content
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Load and display the image (fixed deprecation warning)
            if os.path.exists(project["image"]):
                st.image(Image.open(project["image"]), use_container_width=True)
            
            # Tech stack badges
            st.markdown("**🛠️ Tech Stack:**")
            tech_html = ""
            for tech in project["tech_stack"]:
                tech_html += f'<span class="tech-badge">{tech}</span> '
            st.markdown(tech_html, unsafe_allow_html=True)
        
        with col2:
            # Business Impact
            st.markdown(f"""
            <div class="impact-section">
                <h4>💼 Business Impact</h4>
                <p>{project['impact']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Learning & Expertise
            st.markdown(f"""
            <div class="learning-section">
                <h4>🎓 What I Learned & How It Applies</h4>
                <p>{project['learning']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Business Application
            st.markdown(f"""
            <div class="business-section">
                <h4>🎯 Perfect For Companies That Need</h4>
                <p>{project['business_application']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Metrics section
        st.markdown("### 📊 Key Performance Metrics")
        metric_cols = st.columns(len(project["metrics"]))
        for j, (metric, value) in enumerate(project["metrics"].items()):
            with metric_cols[j]:
                st.markdown(f"""
                <div class="metric-item">
                    <h4 style="margin: 0; color: #667eea;">{value}</h4>
                    <p style="margin: 0; font-size: 0.9em;">{metric}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Project link
        st.markdown(f"""
        <a href='{project['link']}' class='project-link' target='_blank'>
            🔗 Explore Project Details & Code
        </a>
        """, unsafe_allow_html=True)
        
        # Separator
        st.markdown("---")

with tab2:
    st.markdown("### Complete GitHub Repository Collection")
    
    # Fetch GitHub repositories
    with st.spinner("🔄 Fetching latest repositories from GitHub..."):
        repos = fetch_github_repos()
    
    if repos:
        st.success(f"✅ Found {len(repos)} repositories")
        
        # Add search and filter options
        col1, col2, col3 = st.columns(3)
        
        with col1:
            search_term = st.text_input("🔍 Search repositories", placeholder="Enter keywords...")
        
        with col2:
            language_filter = st.selectbox(
                "🔧 Filter by language", 
                ["All"] + list(set([repo.get('language', 'Unknown') for repo in repos if repo.get('language')]))
            )
        
        with col3:
            sort_option = st.selectbox(
                "📊 Sort by", 
                ["Last Updated", "Stars", "Name", "Size"]
            )
        
        # Filter repositories
        filtered_repos = repos
        
        if search_term:
            filtered_repos = [
                repo for repo in filtered_repos 
                if search_term.lower() in repo['name'].lower() or 
                   search_term.lower() in (repo.get('description', '') or '').lower()
            ]
        
        if language_filter != "All":
            filtered_repos = [
                repo for repo in filtered_repos 
                if repo.get('language') == language_filter
            ]
        
        # Sort repositories
        if sort_option == "Stars":
            filtered_repos = sorted(filtered_repos, key=lambda x: x['stargazers_count'], reverse=True)
        elif sort_option == "Name":
            filtered_repos = sorted(filtered_repos, key=lambda x: x['name'].lower())
        elif sort_option == "Size":
            filtered_repos = sorted(filtered_repos, key=lambda x: x['size'], reverse=True)
        # Default is already sorted by "Last Updated"
        
        st.markdown(f"**Showing {len(filtered_repos)} repositories**")
        
        # Display repositories in a grid
        cols = st.columns(2)
        
        for i, repo in enumerate(filtered_repos):
            col = cols[i % 2]
            
            with col:
                # Repository card
                st.markdown(f"""
                <div class="github-repo-card">
                    <h4 style="margin: 0 0 0.5rem 0; color: #2c3e50;">
                        <a href="{repo['html_url']}" target="_blank" style="text-decoration: none; color: inherit;">
                            📁 {repo['name']}
                        </a>
                    </h4>
                    <p style="margin: 0.5rem 0; color: #666; font-size: 0.9rem;">
                        {repo.get('description', 'No description available') or 'No description available'}
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                # Repository statistics
                stats_html = f"""
                <div class="repo-stats">
                    <span class="repo-stat">⭐ {repo['stargazers_count']}</span>
                    <span class="repo-stat">🍴 {repo['forks_count']}</span>
                    <span class="repo-stat">📊 {repo['size']} KB</span>
                """
                
                if repo.get('language'):
                    stats_html += f'<span class="language-badge">{repo["language"]}</span>'
                
                stats_html += "</div>"
                st.markdown(stats_html, unsafe_allow_html=True)
                
                # Last updated
                from datetime import datetime
                updated_date = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
                st.markdown(f"<small style='color: #888;'>Last updated: {updated_date.strftime('%B %d, %Y')}</small>", unsafe_allow_html=True)
                
                st.markdown("---")
    
    else:
        st.warning("⚠️ Unable to fetch repositories. Showing featured projects only.")
        st.markdown("Please check your internet connection or try again later.")

# Call to Action
st.markdown("""
<div class="projects-header" style="margin-top: 3rem;">
    <h2>🤝 Ready to Create Impact Together?</h2>
    <p style="font-size: 1.1rem;">
        These projects demonstrate my ability to deliver measurable results. 
        Let's discuss how I can bring similar value to your organization.
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: #666; margin-top: 2rem;'>© 2024 Karim Osman - Transforming Ideas into Intelligent Solutions</p>", unsafe_allow_html=True)
