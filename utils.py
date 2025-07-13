import streamlit as st
import json
import os
from streamlit_javascript import st_javascript

def get_browser_lang():
    try:
        lang = st_javascript("""const lang = navigator.language || navigator.userLanguage; 
        return lang.split('-')[0];""")
        return lang if lang else "en"
    except:
        return "en"

def load_translations(lang):
    try:
        with open(f"locales/{lang}/translation.json", "r", encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        # Fallback to English
        try:
            with open("locales/en/translation.json", "r", encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}

def tr(key):
    if 'lang' not in st.session_state:
        st.session_state.lang = get_browser_lang()
    
    if 'translations' not in st.session_state or st.session_state.translations.get('__lang__') != st.session_state.lang:
        st.session_state.translations = load_translations(st.session_state.lang)
        st.session_state.translations['__lang__'] = st.session_state.lang
    
    return st.session_state.translations.get(key, key)

def language_selector():
    st.sidebar.markdown(f"### 🌐 {tr('LANGUAGE')}")
    
    lang_options = {
        "en": "🇬🇧 English",
        "fr": "🇫🇷 Français",
        "de": "🇩🇪 Deutsch",
        "sv": "🇸🇪 Svenska",
        "no": "🇳🇴 Norsk",
        "nl": "🇳🇱 Nederlands",
        "da": "🇩🇰 Dansk",
        "ja": "🇯🇵 日本語"
    }
    
    selected_lang = st.sidebar.selectbox(
        "Select Language", # Added a label
        list(lang_options.values()),
        index=list(lang_options.keys()).index(st.session_state.lang),
        label_visibility="hidden" # Hidden the label for cleaner UI
    )
    st.session_state.lang = list(lang_options.keys())[list(lang_options.values()).index(selected_lang)]

    st.sidebar.markdown("---")
    
    # Navigation
    st.sidebar.markdown(f"### {tr('NAVIGATION')}")
    
    pages = {
        tr("NAV_HOME"): "🏠 Home",
        tr("NAV_ABOUT"): "👨‍💻 About",
        tr("NAV_PROJECTS"): "🚀 Projects",
        tr("NAV_SKILLS"): "⚡ Skills",
        tr("NAV_CONTACT"): "📞 Contact",
        tr("NAV_RESUME"): "📄 Resume"
    }

    # Set default page if not in session state
    if "page" not in st.session_state:
        st.session_state.page = tr("NAV_HOME")
    
    page = st.sidebar.radio(
        "Navigation", # Added a label
        list(pages.keys()),
        index=list(pages.keys()).index(st.session_state.page),
        label_visibility="hidden" # Hidden the label for cleaner UI
    )
    st.session_state.page = page

    return st.session_state.page
