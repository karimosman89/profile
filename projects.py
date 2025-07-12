import os
import streamlit as st
from PIL import Image
import requests
import json
from utils import tr 
from datetime import datetime 

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
            st.error(f"{tr('GITHUB_FETCH_ERROR_CODE').format(code=response.status_code)}")
            return []
    except Exception as e:
        st.error(f"{tr('GITHUB_FETCH_ERROR_GENERIC').format(error=str(e))}")
        return []

# Enhanced Project Data with business impact and learning sections (fallback data)
featured_projects = [
    {
        "title": tr('PROJECT_NLP_TITLE'),
        "description": tr('PROJECT_NLP_DESC'),
        "link": "https://github.com/karimosman89/NLP-with-Transformers",
        "image": os.path.join(current_dir, "images", "background5.jpg"),
        "impact": tr('PROJECT_NLP_IMPACT'),
        "learning": tr('PROJECT_NLP_LEARNING'),
        "technologies": ["Python", "Transformers", "PyTorch", "Hugging Face", "NLTK", "SpaCy"]
    },
    {
        "title": tr('PROJECT_COMPUTER_VISION_TITLE'),
        "description": tr('PROJECT_COMPUTER_VISION_DESC'),
        "link": "https://github.com/karimosman89/Real-time-Object-Detection",
        "image": os.path.join(current_dir, "images", "background3.jpg"),
        "impact": tr('PROJECT_COMPUTER_VISION_IMPACT'),
        "learning": tr('PROJECT_COMPUTER_VISION_LEARNING'),
        "technologies": ["Python", "OpenCV", "TensorFlow", "Keras", "YOLO"]
    },
    {
        "title": tr('PROJECT_RECOMMENDER_TITLE'),
        "description": tr('PROJECT_RECOMMENDER_DESC'),
        "link": "https://github.com/karimosman89/Personalized-Recommendation-System",
        "image": os.path.join(current_dir, "images", "background4.jpg"),
        "impact": tr('PROJECT_RECOMMENDER_IMPACT'),
        "learning": tr('PROJECT_RECOMMENDER_LEARNING'),
        "technologies": ["Python", "Pandas", "Scikit-learn", "Implicit", "Dash"]
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
        
        .projects-header {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 3rem;
            margin: 2rem 0;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
            text-align: center;
        }
        .projects-header h1 {
            color: #4a4a4a;
            margin-bottom: 1rem;
        }
        .projects-header p {
            color: #666;
            font-size: 1.15rem;
            line-height: 1.6;
        }

        .project-card {
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            border-left: 5px solid #667eea;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
            height: 100%; /* Ensure cards in columns have equal height */
        }
        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
        }
        .project-card h3 {
            color: #4a4a4a;
            margin-bottom: 1rem;
        }
        .project-card p {
            color: #666;
            font-size: 1.05rem;
            line-height: 1.6;
        }
        .project-card a {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
        }
        .project-card a:hover {
            text-decoration: underline;
        }
        .project-card img {
            max-width: 100%;
            border-radius: 10px;
            margin-bottom: 1rem;
        }
        .project-section-title {
            color: #5d3f6a;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
            border-bottom: 2px solid #eee;
            padding-bottom: 5px;
        }
        .tech-badge {
            display: inline-block;
            background-color: #e0e0e0;
            color: #555;
            padding: 5px 10px;
            border-radius: 8px;
            font-size: 0.85rem;
            margin-right: 8px;
            margin-bottom: 8px;
        }

        .github-repo-card {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
            border: 1px solid #ddd;
        }
        .github-repo-card h4 {
            color: #4a4a4a;
            margin-top: 0;
            margin-bottom: 0.5rem;
        }
        .github-repo-card p {
            color: #666;
            font-size: 0.95rem;
        }
        .repo-stats {
            display: flex;
            gap: 15px;
            margin-top: 1rem;
            flex-wrap: wrap;
        }
        .repo-stat {
            background-color: #f0f8ff;
            color: #337ab7;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 0.85rem;
        }
        .language-badge {
            background-color: #d4edda;
            color: #155724;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 0.85rem;
            font-weight: 500;
        }
    </style>
    """, unsafe_allow_html=True)

set_style()

# Hero Section
st.markdown(f"""
<div class="projects-header">
    <h1>{tr('PROJECTS_HERO_TITLE')}</h1>
    <p>{tr('PROJECTS_HERO_SUBTITLE')}</p>
</div>
""", unsafe_allow_html=True)

# Featured Projects Section
st.markdown(f"## {tr('PROJECTS_FEATURED_TITLE')}")

cols = st.columns(len(featured_projects))
for i, project in enumerate(featured_projects):
    with cols[i]:
        st.markdown(f"""
        <div class="project-card">
            <h3>{project['title']}</h3>
            {"<img src='data:image/jpeg;base64," + (Image.open(project['image']).tobytes().hex() if os.path.exists(project['image']) else '') + "' alt='Project Image'>" if os.path.exists(project['image']) else ''}
            <p>{project['description']}</p>
            <p><a href="{project['link']}" target="_blank">{tr('VIEW_PROJECT_BUTTON')}</a></p>
            
            <h4 class="project-section-title">{tr('BUSINESS_IMPACT_TITLE')}</h4>
            <p>{project['impact']}</p>
            
            <h4 class="project-section-title">{tr('KEY_LEARNINGS_TITLE')}</h4>
            <p>{project['learning']}</p>

            <h4 class="project-section-title">{tr('TECHNOLOGIES_USED_TITLE')}</h4>
            <div>
                {''.join([f'<span class="tech-badge">{tech}</span>' for tech in project['technologies']])}
            </div>
        </div>
        """, unsafe_allow_html=True)

# GitHub Repositories Section
st.markdown(f"## {tr('PROJECTS_GITHUB_TITLE')}")
st.markdown(f"<p>{tr('PROJECTS_GITHUB_SUBTITLE')}</p>", unsafe_allow_html=True)

repos = fetch_github_repos()

if repos:
    for repo in repos:
        if not repo['fork']: # Exclude forked repositories
            st.markdown(f"""
            <div class="github-repo-card">
                <h4><a href="{repo['html_url']}" target="_blank">{repo['name']}</a></h4>
                <p>{repo['description'] if repo['description'] else tr('NO_DESCRIPTION')}</p>
                <div class="repo-stats">
                    <span class="repo-stat">⭐ {repo['stargazers_count']}</span>
                    <span class="repo-stat">🍴 {repo['forks_count']}</span>
                    <span class="repo-stat">📊 {round(repo['size'] / 1024, 2) if repo['size'] else 0} MB</span>
                </div>
            """, unsafe_allow_html=True)
            
            if repo.get('language'):
                st.markdown(f'<span class="language-badge">{repo["language"]}</span></div>', unsafe_allow_html=True)
            else:
                st.markdown("</div>", unsafe_allow_html=True) # Close the div even if no language
            
            # Last updated
            updated_date = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
            st.markdown(f"<small style='color: #888;'>{tr('LAST_UPDATED')}: {updated_date.strftime('%B %d, %Y')}</small>", unsafe_allow_html=True)
            
            st.markdown("---")
else:
    st.warning(tr('GITHUB_FETCH_WARNING'))
    st.markdown(tr('GITHUB_FETCH_ADVICE'))

# Call to Action
st.markdown(f"""
<div class="projects-header" style="margin-top: 3rem;">
    <h2>{tr('PROJECTS_CALL_TITLE')}</h2>
    <p style="font-size: 1.1rem;">
        {tr('PROJECTS_CALL_TEXT1')}
    </p>
    <p style="font-size: 1.1rem;">
        {tr('PROJECTS_CALL_TEXT2')}
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown(f"<p style='text-align: center; color: #666; margin-top: 2rem;'>{tr('PROJECTS_FOOTER')}</p>", unsafe_allow_html=True)
