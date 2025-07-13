import streamlit as st
import json
import os

def get_browser_lang():
    """Improved browser language detection"""
    try:
        # Get browser language from Streamlit headers
        headers = st.experimental_get_headers()
        accept_language = headers.get("Accept-Language", "en").split(",")[0].split("-")[0].lower()
        
        # Map Norwegian variants to 'no'
        if accept_language in ["nb", "nn", "no"]:
            return "no"
        return accept_language if accept_language in ["en", "fr", "de", "sv", "nl", "da", "ja"] else "en"
    except:
        return "en"

def load_translations(lang):
    """Handle case sensitivity and Norwegian variants with absolute paths"""
    try:
        # Normalize language code
        lang = lang.lower()
        
        # Handle Norwegian variants
        if lang in ["nb", "nn"]:
            lang = "no"
            
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct absolute path to translation file
        base_path = os.path.join(script_dir, "locales", lang, "translation.json")
        alt_path = os.path.join(script_dir, "locales", lang.upper(), "translation.json")
        
        # Try paths in order
        for path in [base_path, alt_path]:
            if os.path.exists(path):
                with open(path, "r", encoding='utf-8') as f:
                    return json.load(f)
        
        # If no file found, raise error
        raise FileNotFoundError(f"No translation file found for {lang}")
        
    except Exception as e:
        print(f"Translation error: {e}")
        # Fallback to English
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            en_path = os.path.join(script_dir, "locales", "en", "translation.json")
            with open(en_path, "r", encoding='utf-8') as f:
                return json.load(f)
        except Exception as e2:
            print(f"English fallback failed: {e2}")
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
    
    # Language options with flags and full names
    lang_options = {
        "en": {"flag": "🇬🇧"},
        "fr": {"flag": "🇫🇷"},
        "de": {"flag": "🇩🇪"},
        "sv": {"flag": "🇸🇪"},
        "no": {"flag": "🇳🇴"},
        "nl": {"flag": "🇳🇱"},
        "da": {"flag": "🇩🇰"},
        "ja": {"flag": "🇯🇵"}
    }
    
    # Create display names with flags
    display_options = [f"{lang_options[code]['flag']}" 
                      for code in lang_options.keys()]
    
    # Get current language index
    current_lang = st.session_state.lang
    lang_keys = list(lang_options.keys())
    
    try:
        current_index = lang_keys.index(current_lang)
    except ValueError:
        current_index = 0
    
    # Create language selector
    selected_display = st.sidebar.selectbox(
        "Language Selector",  
        display_options,
        index=current_index,
        label_visibility="collapsed"  
    )
    
    # Update session state with selected language
    selected_index = display_options.index(selected_display)
    st.session_state.lang = lang_keys[selected_index]
    
    # Page navigation with keys
    st.sidebar.markdown(f"### 🚀 {tr('NAVIGATION')}")
    
    # Page configuration with keys
    page_config = {
        "home": tr("NAV_HOME"),
        "about": tr("NAV_ABOUT"),
        "projects": tr("NAV_PROJECTS"),
        "skills": tr("NAV_SKILLS"),
        "contact": tr("NAV_CONTACT"),
        "resume": tr("NAV_RESUME")
    }
    
    # Initialize selected page
    if "page" not in st.session_state:
        st.session_state.page = "home"
    
    # Create radio buttons with translated labels
    selected_label = st.sidebar.radio(
        "Navigation Menu",  
        list(page_config.values()),
        index=list(page_config.keys()).index(st.session_state.page),
        label_visibility="collapsed"  
    )
    
    # Find the key for the selected label
    for key, label in page_config.items():
        if label == selected_label:
            st.session_state.page = key
            break
            
    return st.session_state.page
