"""
Professional CSS Framework for Karim Osman's Portfolio
Advanced styling system with modern design patterns and responsive layouts
"""

import streamlit as st

def inject_custom_css():
    """Inject comprehensive professional CSS styling"""
    st.markdown("""
    <style>
    :root {
        --primary-blue: #2E86AB;
        --primary-blue-dark: #1E5A73;
        --secondary-orange: #F24236;
        --accent-purple: #6C5CE7;
        --white: #FFFFFF;
        --light-gray: #F8F9FA;
        --medium-gray: #6C757D;
        --dark-gray: #343A40;
        --gradient-primary: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
        --gradient-subtle: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        --space-sm: 0.5rem;
        --space-md: 1rem;
        --space-lg: 1.5rem;
        --space-xl: 2rem;
        --space-2xl: 3rem;
        --space-3xl: 4rem;
        --radius-md: 8px;
        --radius-lg: 12px;
        --radius-xl: 20px;
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        --transition-medium: 300ms ease-in-out;
    }

    .main {
        padding: 0 !important;
        max-width: none !important;
    }

    .block-container {
        padding: 2rem 1rem !important;
        max-width: 1200px !important;
        margin: 0 auto !important;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}

    .hero-section {
        text-align: center;
        padding: var(--space-3xl) 0;
        background: var(--gradient-subtle);
        border-radius: var(--radius-xl);
        margin-bottom: var(--space-3xl);
        position: relative;
        overflow: hidden;
    }

    .hero-title {
        font-size: 4rem;
        font-weight: 700;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: var(--space-lg);
    }

    .hero-subtitle {
        font-size: 1.5rem;
        color: var(--medium-gray);
        margin-bottom: var(--space-xl);
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }

    .professional-card {
        background: var(--white);
        border-radius: var(--radius-lg);
        padding: var(--space-xl);
        margin-bottom: var(--space-lg);
        box-shadow: var(--shadow-md);
        transition: all var(--transition-medium);
        border: 1px solid #e9ecef;
        position: relative;
        overflow: hidden;
    }

    .professional-card:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow-xl);
    }

    .professional-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: var(--gradient-primary);
    }

    .card-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--dark-gray);
        margin-bottom: var(--space-md);
    }

    .card-content {
        color: var(--medium-gray);
        line-height: 1.6;
    }

    .metrics-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: var(--space-lg);
        margin-bottom: var(--space-3xl);
    }

    .metric-card {
        background: var(--white);
        border-radius: var(--radius-lg);
        padding: var(--space-xl);
        text-align: center;
        box-shadow: var(--shadow-md);
        transition: all var(--transition-medium);
        border-left: 4px solid var(--primary-blue);
    }

    .metric-card:hover {
        transform: scale(1.05);
        box-shadow: var(--shadow-xl);
    }

    .metric-number {
        font-size: 2.5rem;
        font-weight: 700;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: var(--space-sm);
    }

    .metric-label {
        font-size: 1rem;
        color: var(--medium-gray);
        font-weight: 500;
    }

    .btn-primary {
        background: var(--gradient-primary);
        color: var(--white);
        border: none;
        padding: var(--space-md) var(--space-xl);
        border-radius: var(--radius-lg);
        font-weight: 600;
        font-size: 1rem;
        cursor: pointer;
        transition: all var(--transition-medium);
        text-decoration: none;
        display: inline-block;
        text-align: center;
        box-shadow: var(--shadow-md);
    }

    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-xl);
        filter: brightness(1.1);
    }

    .btn-secondary {
        background: var(--white);
        color: var(--primary-blue);
        border: 2px solid var(--primary-blue);
        padding: var(--space-md) var(--space-xl);
        border-radius: var(--radius-lg);
        font-weight: 600;
        font-size: 1rem;
        cursor: pointer;
        transition: all var(--transition-medium);
        text-decoration: none;
        display: inline-block;
        text-align: center;
    }

    .btn-secondary:hover {
        background: var(--primary-blue);
        color: var(--white);
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
    }

    .skill-item {
        margin-bottom: var(--space-lg);
    }

    .skill-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: var(--space-sm);
    }

    .skill-name {
        font-weight: 600;
        color: var(--dark-gray);
    }

    .skill-percentage {
        font-weight: 500;
        color: var(--primary-blue);
    }

    .skill-bar {
        height: 8px;
        background: var(--light-gray);
        border-radius: var(--radius-md);
        overflow: hidden;
        position: relative;
    }

    .skill-progress {
        height: 100%;
        background: var(--gradient-primary);
        border-radius: var(--radius-md);
        transition: width 1s ease-in-out;
        position: relative;
    }

    .stButton > button {
        background: var(--gradient-primary);
        color: var(--white);
        border: none;
        border-radius: var(--radius-lg);
        padding: var(--space-md) var(--space-xl);
        font-weight: 600;
        transition: all var(--transition-medium);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
        filter: brightness(1.1);
    }

    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        .block-container {
            padding: 1rem !important;
        }
        .metrics-container {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media (max-width: 480px) {
        .metrics-container {
            grid-template-columns: 1fr;
        }
        .hero-section {
            padding: var(--space-xl) var(--space-md);
        }
        .professional-card {
            padding: var(--space-lg);
        }
    }

    .fade-in {
        animation: fadeIn 0.6s ease-out;
    }

    .slide-up {
        animation: slideUp 0.6s ease-out;
    }

    .scale-in {
        animation: scaleIn 0.4s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes scaleIn {
        from { opacity: 0; transform: scale(0.9); }
        to { opacity: 1; transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)

def create_hero_section(name, title, description):
    """Create a professional hero section"""
    st.markdown(f"""
    <div class="hero-section fade-in">
        <div class="hero-content">
            <h1 class="hero-title">{name}</h1>
            <p class="hero-subtitle">{title}</p>
            <p class="subtitle">{description}</p>
            <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
                <a href="#contact" class="btn-primary">Get In Touch</a>
                <a href="#projects" class="btn-secondary">View Projects</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_metrics_dashboard(metrics):
    """Create a professional metrics dashboard"""
    st.markdown('<div class="metrics-container">', unsafe_allow_html=True)
    for metric in metrics:
        st.markdown(f"""
        <div class="metric-card scale-in">
            <div class="metric-number">{metric["value"]}</div>
            <div class="metric-label">{metric["label"]}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def create_professional_card(title, content, icon="📋"):
    """Create a professional card component"""
    st.markdown(f"""
    <div class="professional-card slide-up">
        <div class="card-title">{icon} {title}</div>
        <div class="card-content">{content}</div>
    </div>
    """, unsafe_allow_html=True)

def create_skill_bar(skill_name, percentage):
    """Create an animated skill bar"""
    st.markdown(f"""
    <div class="skill-item">
        <div class="skill-header">
            <span class="skill-name">{skill_name}</span>
            <span class="skill-percentage">{percentage}%</span>
        </div>
        <div class="skill-bar">
            <div class="skill-progress" style="width: {percentage}%"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def get_theme_colors():
    """Return the professional theme color palette"""
    return {
        'primary_blue': '#2E86AB',
        'primary_blue_dark': '#1E5A73',
        'secondary_orange': '#F24236',
        'accent_purple': '#6C5CE7',
        'white': '#FFFFFF',
        'light_gray': '#F8F9FA',
        'medium_gray': '#6C757D',
        'dark_gray': '#343A40'
    }
