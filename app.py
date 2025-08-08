"""
Enhanced Professional Portfolio - Main Entry Point
Karim Osman's AI & ML Engineering Portfolio
Advanced Streamlit application with professional design and modern features
"""

import streamlit as st
import sys
import os

# Add the current directory to Python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import all page modules and utilities
try:
    from styles import inject_custom_css, get_theme_colors
    from index import show_homepage
    from about import show_about_page
    from projects import show_projects_page
    from skills import show_skills_page
    from contact import show_contact_page
except ImportError as e:
    st.error(f"Import error: {e}")
    st.error("Please ensure all required files are in the same directory")
    st.stop()

# Professional page configuration
st.set_page_config(
    page_title="Karim Osman - AI/ML Engineer | Professional Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://linkedin.com/in/karim-osman',
        'Report a bug': 'mailto:karim.osman.ai@gmail.com',
        'About': """
        # Karim Osman - AI/ML Engineer

        **Professional Portfolio & Showcase**

        Showcasing cutting-edge AI/ML projects, innovative solutions, 
        and professional expertise in artificial intelligence, machine learning, 
        and software engineering.

        **Connect with me:**
        - 🌐 [LinkedIn](https://linkedin.com/in/karim-osman)
        - 💻 [GitHub](https://github.com/karimosman89)
        - ✉️ [Email](mailto:karim.osman.ai@gmail.com)
        - 🐦 [Twitter](https://twitter.com/karim_ai)

        ---
        *Transforming ideas into intelligent solutions*
        """
    }
)

# Professional metadata for SEO and social sharing
def add_professional_metadata():
    """Add comprehensive metadata for professional presentation"""
    st.markdown("""
    <meta name="description" content="Karim Osman - Senior AI/ML Engineer specializing in deep learning, computer vision, NLP, and intelligent systems. Professional portfolio showcasing innovative AI solutions and cutting-edge projects.">
    <meta name="keywords" content="AI Engineer, Machine Learning, Deep Learning, Computer Vision, NLP, Python, TensorFlow, PyTorch, Data Science, Software Engineering">
    <meta name="author" content="Karim Osman">
    <meta name="robots" content="index, follow">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="Karim Osman - AI/ML Engineer | Professional Portfolio">
    <meta property="og:description" content="Senior AI/ML Engineer specializing in cutting-edge artificial intelligence and machine learning solutions. Explore innovative projects and professional expertise.">
    <meta property="og:image" content="https://via.placeholder.com/1200x630/2E86AB/FFFFFF?text=Karim+Osman+AI/ML+Engineer">
    <meta property="og:url" content="https://kosman.streamlit.app">
    <meta property="og:site_name" content="Karim Osman Portfolio">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:title" content="Karim Osman - AI/ML Engineer | Professional Portfolio">
    <meta property="twitter:description" content="Senior AI/ML Engineer specializing in cutting-edge artificial intelligence and machine learning solutions.">
    <meta property="twitter:image" content="https://via.placeholder.com/1200x630/2E86AB/FFFFFF?text=Karim+Osman+AI/ML+Engineer">
    <meta property="twitter:creator" content="@karim_ai">

    <!-- Additional Professional Metadata -->
    <meta name="linkedin:owner" content="karim-osman">
    <meta name="theme-color" content="#2E86AB">
    <meta name="application-name" content="Karim Osman Portfolio">
    <meta name="msapplication-TileColor" content="#2E86AB">

    <!-- Structured Data for Rich Snippets -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "Karim Osman",
      "jobTitle": "Senior AI/ML Engineer",
      "description": "Expert AI/ML Engineer specializing in deep learning, computer vision, and intelligent systems",
      "url": "https://kosman.streamlit.app",
      "sameAs": [
        "https://linkedin.com/in/karim-osman",
        "https://github.com/karimosman89",
        "https://twitter.com/karim_ai"
      ],
      "knowsAbout": [
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning",
        "Computer Vision",
        "Natural Language Processing",
        "Python",
        "TensorFlow",
        "PyTorch",
        "Data Science"
      ],
      "alumniOf": "Alexandria University",
      "email": "karim.osman.ai@gmail.com"
    }
    </script>
    """, unsafe_allow_html=True)

# Main application navigation and routing
def main():
    """Main application entry point with professional navigation"""

    # Inject professional styling and metadata
    inject_custom_css()
    add_professional_metadata()

    # Initialize session state for navigation
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Home'

    if 'page_history' not in st.session_state:
        st.session_state.page_history = ['Home']

    # Professional navigation sidebar
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 2rem 0;">
            <div style="width: 100px; height: 100px; border-radius: 50%; background: linear-gradient(135deg, #2E86AB, #6C5CE7); margin: 0 auto 1rem; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 2.5rem;">🚀</span>
            </div>
            <h2 style="margin: 0; color: #2E86AB;">Karim Osman</h2>
            <p style="margin: 0.5rem 0 0; color: #6C757D; font-size: 0.9rem;">AI/ML Engineer</p>
        </div>
        """, unsafe_allow_html=True)

        # Navigation menu
        pages = {
            '🏠 Home': 'Home',
            '👨‍💻 About Me': 'About',
            '🚀 Projects': 'Projects', 
            '🛠️ Skills': 'Skills',
            '📞 Contact': 'Contact'
        }

        selected_page = st.selectbox(
            "Navigate to:",
            list(pages.keys()),
            index=list(pages.values()).index(st.session_state.current_page),
            key="navigation_selectbox"
        )

        # Update current page
        if pages[selected_page] != st.session_state.current_page:
            st.session_state.current_page = pages[selected_page]
            if pages[selected_page] not in st.session_state.page_history[-3:]:
                st.session_state.page_history.append(pages[selected_page])

        # Professional quick actions
        st.markdown("---")
        st.markdown("### 🔗 Quick Actions")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("💼 LinkedIn", use_container_width=True):
                st.markdown('[Open LinkedIn](https://linkedin.com/in/karim-osman)', unsafe_allow_html=True)

            if st.button("✉️ Email", use_container_width=True):
                st.markdown('[Send Email](mailto:karim.osman.ai@gmail.com)', unsafe_allow_html=True)

        with col2:
            if st.button("💻 GitHub", use_container_width=True):
                st.markdown('[View GitHub](https://github.com/karimosman89)', unsafe_allow_html=True)

            if st.button("📄 Resume", use_container_width=True):
                st.markdown('[Download Resume](https://example.com/resume.pdf)', unsafe_allow_html=True)

        # Professional status indicator
        st.markdown("---")
        st.markdown("""
        <div style="padding: 1rem; background: linear-gradient(135deg, #d4edda, #c3e6cb); border-radius: 8px; text-align: center;">
            <div style="color: #155724; font-weight: 600; margin-bottom: 0.5rem;">🟢 Available for Work</div>
            <div style="color: #155724; font-size: 0.8rem;">Open to new opportunities</div>
        </div>
        """, unsafe_allow_html=True)

    # Main content area with professional routing
    try:
        if st.session_state.current_page == 'Home':
            show_homepage()
        elif st.session_state.current_page == 'About':
            show_about_page()
        elif st.session_state.current_page == 'Projects':
            show_projects_page()
        elif st.session_state.current_page == 'Skills':
            show_skills_page()
        elif st.session_state.current_page == 'Contact':
            show_contact_page()
        else:
            st.error("Page not found. Redirecting to homepage...")
            st.session_state.current_page = 'Home'
            st.rerun()

    except Exception as e:
        st.error(f"An error occurred while loading the page: {str(e)}")
        st.error("Please try refreshing the page or contact support.")

        # Error reporting for development
        with st.expander("🔧 Technical Details (Development)"):
            st.code(f"""
Error Details:
- Page: {st.session_state.current_page}
- Error: {str(e)}
- Type: {type(e).__name__}
            """)

    # Professional footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0; color: #6C757D;">
        <p style="margin: 0;">© 2024 Karim Osman. Crafted with ❤️ and cutting-edge technology.</p>
        <p style="margin: 0.5rem 0 0; font-size: 0.9rem;">Transforming ideas into intelligent solutions, one algorithm at a time.</p>
        <div style="margin-top: 1rem;">
            <a href="https://linkedin.com/in/karim-osman" style="margin: 0 0.5rem; color: #2E86AB; text-decoration: none;">LinkedIn</a> |
            <a href="https://github.com/karimosman89" style="margin: 0 0.5rem; color: #2E86AB; text-decoration: none;">GitHub</a> |
            <a href="mailto:karim.osman.ai@gmail.com" style="margin: 0 0.5rem; color: #2E86AB; text-decoration: none;">Email</a> |
            <a href="https://twitter.com/karim_ai" style="margin: 0 0.5rem; color: #2E86AB; text-decoration: none;">Twitter</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Application performance monitoring
@st.cache_data
def get_app_stats():
    """Get application statistics for monitoring"""
    import time
    return {
        'load_time': time.time(),
        'version': '2.0.0',
        'last_updated': '2024-12-19'
    }

# Entry point
if __name__ == "__main__":
    # Load application statistics
    app_stats = get_app_stats()

    # Run main application
    main()

    # Development mode indicator
    if os.getenv('STREAMLIT_ENV') == 'development':
        with st.sidebar:
            with st.expander("🔧 Development Info"):
                st.json(app_stats)
