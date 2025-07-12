import streamlit as st
import json
import os

def get_browser_lang():
    """Fallback language detection without JavaScript"""
    # Default to English
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
    display_options = [f"{lang_options[code]['flag']} {lang_options[code]['name']}" 
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
        "", 
        display_options,
        index=current_index
    )
    
    # Update session state with selected language
    selected_index = display_options.index(selected_display)
    st.session_state.lang = lang_keys[selected_index]
    
    st.sidebar.markdown(f"### 🚀 {tr('NAVIGATION')}")
    page = st.sidebar.radio("", [
        tr("NAV_HOME"),
        tr("NAV_ABOUT"),
        tr("NAV_PROJECTS"),
        tr("NAV_SKILLS"),
        tr("NAV_CONTACT"),
        tr("NAV_RESUME")
    ])
    return page
