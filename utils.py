import streamlit as st
import json
import os

def get_browser_lang():
    """Fallback language detection without JavaScript"""
    # Default to English
    return "en"

def load_translations(lang):
    st.write(f"Attempting to load translations for: {lang}")
    try:
        with open(f"locales/{lang}/translation.json", "r", encoding='utf-8') as f:
            translations = json.load(f)
            st.write(f"Successfully loaded translations for {lang}")
            return translations
    except Exception as e:
        st.warning(f"Could not load translations for {lang}. Error: {e}. Falling back to English.")
        try:
            with open("locales/en/translation.json", "r", encoding='utf-8') as f:
                translations_en = json.load(f)
                st.write("Successfully loaded English fallback translations.")
                return translations_en
        except Exception as e_en:
            st.error(f"Could not load English fallback translations. Error: {e_en}. Returning empty dict.")
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
    # MODIFIED: Added a label and label_visibility="hidden"
    selected_display = st.sidebar.selectbox(
        "Select Language", # Provide a descriptive label
        display_options,
        index=current_index,
        label_visibility="hidden" # Hide the label if you don't want it visible
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
    # MODIFIED: Added a label and label_visibility="hidden"
    selected_label = st.sidebar.radio(
        "Navigate Pages", # Provide a descriptive label
        list(page_config.values()),
        index=list(page_config.keys()).index(st.session_state.page),
        label_visibility="hidden" # Hide the label if you don't want it visible
    )
    
    # Find the key for the selected label
    for key, label in page_config.items():
        if label == selected_label:
            st.session_state.page = key
            break
            
    return st.session_state.page
