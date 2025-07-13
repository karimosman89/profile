import os
import streamlit as st
from PIL import Image
import requests
import json
from utils import tr # Import the translation function
from datetime import datetime

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Function to fetch GitHub repositories
@st.cache_data(ttl=3600) # Cache for 1 hour
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
            st.error(f"{tr('GITHUB_FETCH_ERROR_CODE').format(code=response.status_code)}")
            return []
    except Exception as e:
        st.error(f"{tr('GITHUB_FETCH_ERROR_GENERIC').format(error=str(e))}")
        return []

# Enhanced Project Data with business impact and learning sections (fallback data)
featured_projects = [
    {
        "title_key": "PROJECT_NLP_TITLE", # Changed to key
        "description_key": "PROJECT_NLP_DESC", # Changed to key
        "link": "https://github.com/karimosman89/NLP-with-Transformers",
        "image": os.path.join(current_dir, "images", "background5.jpg"),
        "impact_key": "PROJECT_NLP_IMPACT", # Changed to key
        "learning_key": "PROJECT_NLP_LEARNING", # Changed to key
        "business_application_key": "PROJECT_NLP_BUSINESS_APP", # Changed to key
        "tech_stack": ["BERT", "Transformers", "PyTorch", "Hugging Face", "Python"],
        "metrics_keys": {"METRIC_ACCURACY": "94%", "METRIC_PROCESSING_SPEED": "2x faster", "METRIC_MODEL_SIZE": "50% smaller"} # Changed to keys
    },
    {
        "title_key": "PROJECT_TIME_SERIES_TITLE", # Changed to key
        "description_key": "PROJECT_TIME_SERIES_DESC", # Changed to key
        "link": "https://github.com/karimosman89/time-series",
        "image": os.path.join(current_dir, "images", "background9.jpg"),
        "impact_key": "PROJECT_TIME_SERIES_IMPACT", # Changed to key
        "learning_key": "PROJECT_TIME_SERIES_LEARNING", # Changed to key
        "business_application_key": "PROJECT_TIME_SERIES_BUSINESS_APP", # Changed to key
        "tech_stack": ["LSTM", "ARIMA", "Prophet", "TensorFlow", "Pandas", "Scikit-learn"],
        "metrics_keys": {"METRIC_PREDICTION_ACCURACY": "89%", "METRIC_MAPE": "8.5%", "METRIC_TRAINING_TIME": "60% faster"} # Changed to keys
    },
    {
        "title_key": "PROJECT_ML_PIPELINE_TITLE", # Changed to key
        "description_key": "PROJECT_ML_PIPELINE_DESC", # Changed to key
        "link": "https://github.com/karimosman89/ML-Pipeline-AWS",
        "image": os.path.join(current_dir, "images", "background10.jpg"),
        "impact_key": "PROJECT_ML_PIPELINE_IMPACT", # Changed to key
        "learning_key": "PROJECT_ML_PIPELINE_LEARNING", # Changed to key
        "business_application_key": "PROJECT_ML_PIPELINE_BUSINESS_APP", # Changed to key
        "tech_stack": ["AWS SageMaker", "Lambda", "S3", "CloudWatch", "Docker", "GitHub Actions"],
        "metrics_keys": {"METRIC_CHURN_REDUCTION": "23%", "METRIC_MODEL_ACCURACY": "92%", "METRIC_DEPLOYMENT_TIME": "75% faster"} # Changed to keys
    },
    {
        "title_key": "PROJECT_DATA_PIPELINE_TITLE", # Changed to key
        "description_key": "PROJECT_DATA_PIPELINE_DESC", # Changed to key
        "link": "https://github.com/karimosman89/Data-Pipeline",
        "image": os.path.join(current_dir, "images", "background15.jpg"),
        "impact_key": "PROJECT_DATA_PIPELINE_IMPACT", # Changed to key
        "learning_key": "PROJECT_DATA_PIPELINE_LEARNING", # Changed to key
        "business_application_key": "PROJECT_DATA_PIPELINE_BUSINESS_APP", # Changed to key
        "tech_stack": ["Apache Kafka", "Spark", "Elasticsearch", "Kibana", "Docker", "Kubernetes"],
        "metrics_keys": {"METRIC_THROUGHPUT": "10M events/hour", "METRIC_LATENCY": "<100ms", "METRIC_UPTIME": "99.9%"} # Changed to keys
    },
]

# Set page style (no changes needed here as it's CSS)
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


st.markdown(f"""
<div class="projects-header">
    <h1>{tr('PROJECTS_HERO_TITLE_NEW')}</h1>
    <p style="font-size: 1.2rem; margin-top: 1rem;">
        {tr('PROJECTS_HERO_SUBTITLE_NEW')}
    </p>
</div>
""", unsafe_allow_html=True)

# Create tabs for different project views
tab1, tab2 = st.tabs([tr("TAB_FEATURED_PROJECTS"), tr("TAB_GITHUB_REPOSITORIES")])

with tab1:
    st.markdown(f"### {tr('FEATURED_PROJECTS_HEADER')}")
    
    # Display Featured Projects with enhanced information
    for i, project in enumerate(featured_projects):
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{tr(project['title_key'])}</div>
            <div class="project-description">{tr(project['description_key'])}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Create columns for image and content
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Load and display the image (fixed deprecation warning)
            if os.path.exists(project["image"]):
                st.image(Image.open(project["image"]), use_container_width=True)
            
            # Tech stack badges
            st.markdown(f"**{tr('TECH_STACK_HEADER')}:**")
            tech_html = ""
            for tech in project["tech_stack"]:
                tech_html += f'<span class="tech-badge">{tech}</span> '
            st.markdown(tech_html, unsafe_allow_html=True)
        
        with col2:
            # Business Impact
            st.markdown(f"""
            <div class="impact-section">
                <h4>{tr('BUSINESS_IMPACT_TITLE')}</h4>
                <p>{tr(project['impact_key'])}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Learning & Expertise
            st.markdown(f"""
            <div class="learning-section">
                <h4>{tr('LEARNING_APPLIES_TITLE')}</h4>
                <p>{tr(project['learning_key'])}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Business Application
            st.markdown(f"""
            <div class="business-section">
                <h4>{tr('BUSINESS_APPLICATION_TITLE')}</h4>
                <p>{tr(project['business_application_key'])}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Metrics section
        st.markdown(f"### {tr('KPI_METRICS_HEADER')}")
        metric_cols = st.columns(len(project["metrics_keys"]))
        for j, (metric_key, value) in enumerate(project["metrics_keys"].items()):
            with metric_cols[j]:
                st.markdown(f"""
                <div class="metric-item">
                    <h4 style="margin: 0; color: #667eea;">{value}</h4>
                    <p style="margin: 0; font-size: 0.9em;">{tr(metric_key)}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Project link
        st.markdown(f"""
        <a href='{project['link']}' class='project-link' target='_blank'>
            {tr('EXPLORE_PROJECT_LINK_TEXT')}
        </a>
        """, unsafe_allow_html=True)
        
        # Separator
        st.markdown("---")

with tab2:
    st.markdown(f"### {tr('GITHUB_COLLECTION_HEADER')}")
    
    # Fetch GitHub repositories
    with st.spinner(tr("FETCHING_REPOS_SPINNER")):
        repos = fetch_github_repos()
    
    if repos:
        st.success(tr("REPOS_FOUND_MESSAGE").format(count=len(repos)))
        
        # Add search and filter options
        col1, col2, col3 = st.columns(3)
        
        with col1:
            search_term = st.text_input(tr("SEARCH_REPOS_LABEL"), placeholder=tr("SEARCH_REPOS_PLACEHOLDER"))
        
        with col2:
            language_filter = st.selectbox(
                tr("FILTER_LANGUAGE_LABEL"),
                [tr("FILTER_LANGUAGE_ALL")] + list(set([repo.get('language', 'Unknown') for repo in repos if repo.get('language')]))
            )
        
        with col3:
            sort_option = st.selectbox(
                tr("SORT_BY_LABEL"),
                [tr("SORT_LAST_UPDATED"), tr("SORT_STARS"), tr("SORT_NAME"), tr("SORT_SIZE")]
            )
        
        # Filter repositories
        filtered_repos = repos
        
        if search_term:
            filtered_repos = [
                repo for repo in filtered_repos
                if search_term.lower() in repo['name'].lower() or
                   search_term.lower() in (repo.get('description', '') or '').lower()
            ]
        
        if language_filter != tr("FILTER_LANGUAGE_ALL"):
            filtered_repos = [
                repo for repo in filtered_repos
                if repo.get('language') == language_filter
            ]
        
        # Sort repositories
        if sort_option == tr("SORT_STARS"):
            filtered_repos = sorted(filtered_repos, key=lambda x: x['stargazers_count'], reverse=True)
        elif sort_option == tr("SORT_NAME"):
            filtered_repos = sorted(filtered_repos, key=lambda x: x['name'].lower())
        elif sort_option == tr("SORT_SIZE"):
            filtered_repos = sorted(filtered_repos, key=lambda x: x['size'], reverse=True)
        # Default is already sorted by "Last Updated"
        
        st.markdown(f"**{tr('SHOWING_REPOS_COUNT').format(count=len(filtered_repos))}**")
        
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
                        {repo.get('description', tr('NO_DESCRIPTION_AVAILABLE')) or tr('NO_DESCRIPTION_AVAILABLE')}
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
                updated_date = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
                st.markdown(f"<small style='color: #888;'>{tr('LAST_UPDATED_LABEL')}: {updated_date.strftime('%B %d, %Y')}</small>", unsafe_allow_html=True)
                
                st.markdown("---")
    
    else:
        st.warning(tr('REPOS_FETCH_WARNING'))
        st.markdown(tr('REPOS_FETCH_ADVICE'))

# Call to Action
st.markdown(f"""
<div class="projects-header" style="margin-top: 3rem;">
    <h2>{tr('PROJECTS_CALL_TO_ACTION_TITLE')}</h2>
    <p style="font-size: 1.1rem;">
        {tr('PROJECTS_CALL_TO_ACTION_TEXT1')}
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown(f"<p style='text-align: center; color: #666; margin-top: 2rem;'>{tr('PROJECTS_FOOTER_TEXT')}</p>", unsafe_allow_html=True)
