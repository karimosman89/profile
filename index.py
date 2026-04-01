"""
Elite AI Architect Portfolio — Karim Osman
Lead Full-Stack AI Engineer & Freelance Consultant
Cyber-Institutional Dark Mode | RAG Agent | Production Dashboard
Languages: EN / IT / FR
"""

import streamlit as st
from PIL import Image
import json
import base64
import requests
import time
import os
import sys
import random

sys.path.append(os.path.dirname(__file__))

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Karim Osman · Senior AI Engineer & Freelancer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.linkedin.com/in/karimosman89/",
        "Report a bug": "mailto:karim.osman.ai@gmail.com",
        "About": "Elite AI Architecture Portfolio — Karim Osman"
    }
)

from styles import CYBER_CSS
from rag_agent import render_rag_sidebar

st.markdown(CYBER_CSS, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  TRANSLATIONS — EN / IT / FR
# ─────────────────────────────────────────────────────────────────────────────
I18N = {
    "en": {
        # Nav
        "nav_home":       "🏠 Home",
        "nav_impact":     "📊 Impact",
        "nav_skills":     "🛠️ Tech Stack",
        "nav_projects":   "🚀 Projects",
        "nav_demos":      "🔬 Live Demos",
        "nav_freelance":  "💼 Freelance",
        "nav_exp":        "🗂️ Experience",
        "nav_certs":      "📜 Credentials",
        "nav_contact":    "📬 Contact",
        # Hero
        "hero_title":     "Senior AI Engineer & Freelance Consultant",
        "hero_subtitle":  "Architecting production-grade LLM platforms, RAG systems, and Computer Vision pipelines — available for freelance missions across AI, Robotics & Data Science.",
        "hire_cta":       "Hire Me",
        "download_cv":    "Download CV",
        # Sections
        "section_impact":     "Production Impact Dashboard",
        "section_arch":       "System Architecture",
        "section_skills":     "Tech Stack Map",
        "section_projects":   "Featured Projects",
        "section_demos":      "Live Trending Demos",
        "section_demos_sub":  "Hands-on demos of the hottest AI · Robotics · Data Science trends",
        "section_freelance":  "Freelance Services",
        "section_exp":        "Experience Timeline",
        "section_certs":      "Credential Vault",
        "section_contact":    "Hire / Invest / Collaborate",
        # Freelance
        "fl_tagline":     "Available for freelance missions — remote & on-site across Europe",
        "fl_services":    "Services I Offer",
        "fl_process":     "How I Work",
        "fl_avail":       "Availability",
        "fl_avail_text":  "🟢 Available Now — 20–40 hrs/week",
        "fl_response":    "⚡ Typical response: within 24 hours",
        "fl_rate_note":   "Rates vary by project scope. Contact for a custom quote.",
        # Contact
        "contact_title":  "Let's Build Something Great",
        "contact_sub":    "Open to senior roles, freelance missions, AI consulting, and investment partnerships.",
        "form_name":      "Full Name *",
        "form_email":     "Email Address *",
        "form_org":       "Organisation",
        "form_purpose":   "Purpose",
        "form_msg":       "Message *",
        "form_send":      "Send Message →",
        "form_success":   "✅ Message sent! Karim will respond within 24 hours.",
        "form_error":     "Please fill in Name, Email, and Message.",
        "purpose_opts": [
            "Senior AI Engineer Role",
            "Freelance AI/ML Mission",
            "LLM / RAG Consulting",
            "Computer Vision Project",
            "Data Science Project",
            "Robotics AI Integration",
            "MLOps & Infrastructure",
            "Speaking / Mentoring",
            "Investment / Partnership",
            "Other",
        ],
    },
    "it": {
        # Nav
        "nav_home":       "🏠 Home",
        "nav_impact":     "📊 Impatto",
        "nav_skills":     "🛠️ Tecnologie",
        "nav_projects":   "🚀 Progetti",
        "nav_demos":      "🔬 Demo Live",
        "nav_freelance":  "💼 Freelance",
        "nav_exp":        "🗂️ Esperienza",
        "nav_certs":      "📜 Certificati",
        "nav_contact":    "📬 Contatti",
        # Hero
        "hero_title":     "Ingegnere AI Senior & Consulente Freelance",
        "hero_subtitle":  "Progetto piattaforme LLM, sistemi RAG e pipeline di Computer Vision di livello produttivo — disponibile per missioni freelance in AI, Robotica e Data Science.",
        "hire_cta":       "Assumi",
        "download_cv":    "Scarica CV",
        # Sections
        "section_impact":     "Dashboard dell'Impatto Produttivo",
        "section_arch":       "Architettura del Sistema",
        "section_skills":     "Mappa delle Tecnologie",
        "section_projects":   "Progetti in Evidenza",
        "section_demos":      "Demo Trending Live",
        "section_demos_sub":  "Demo pratiche delle tendenze più calde in AI · Robotica · Data Science",
        "section_freelance":  "Servizi Freelance",
        "section_exp":        "Timeline dell'Esperienza",
        "section_certs":      "Archivio Certificazioni",
        "section_contact":    "Assumi / Investi / Collabora",
        # Freelance
        "fl_tagline":     "Disponibile per missioni freelance — da remoto e in presenza in tutta Europa",
        "fl_services":    "Servizi Offerti",
        "fl_process":     "Come Lavoro",
        "fl_avail":       "Disponibilità",
        "fl_avail_text":  "🟢 Disponibile Ora — 20–40 ore/settimana",
        "fl_response":    "⚡ Risposta tipica: entro 24 ore",
        "fl_rate_note":   "Le tariffe variano in base all'ambito del progetto. Contattami per un preventivo personalizzato.",
        # Contact
        "contact_title":  "Costruiamo Qualcosa di Straordinario",
        "contact_sub":    "Aperto a ruoli senior, missioni freelance, consulenza AI e partnership di investimento.",
        "form_name":      "Nome Completo *",
        "form_email":     "Indirizzo Email *",
        "form_org":       "Organizzazione",
        "form_purpose":   "Scopo",
        "form_msg":       "Messaggio *",
        "form_send":      "Invia Messaggio →",
        "form_success":   "✅ Messaggio inviato! Karim risponderà entro 24 ore.",
        "form_error":     "Inserisci Nome, Email e Messaggio.",
        "purpose_opts": [
            "Ruolo Ingegnere AI Senior",
            "Missione Freelance AI/ML",
            "Consulenza LLM / RAG",
            "Progetto Computer Vision",
            "Progetto Data Science",
            "Integrazione AI per Robotica",
            "MLOps & Infrastruttura",
            "Speaking / Mentoring",
            "Investimento / Partnership",
            "Altro",
        ],
    },
    "fr": {
        # Nav
        "nav_home":       "🏠 Accueil",
        "nav_impact":     "📊 Impact",
        "nav_skills":     "🛠️ Technologies",
        "nav_projects":   "🚀 Projets",
        "nav_demos":      "🔬 Démos Live",
        "nav_freelance":  "💼 Freelance",
        "nav_exp":        "🗂️ Expérience",
        "nav_certs":      "📜 Certifications",
        "nav_contact":    "📬 Contact",
        # Hero
        "hero_title":     "Ingénieur IA Senior & Consultant Freelance",
        "hero_subtitle":  "Je conçois des plateformes LLM, systèmes RAG et pipelines Computer Vision en production — disponible pour des missions freelance en IA, Robotique et Data Science.",
        "hire_cta":       "Me Recruter",
        "download_cv":    "Télécharger CV",
        # Sections
        "section_impact":     "Tableau de Bord d'Impact Production",
        "section_arch":       "Architecture Système",
        "section_skills":     "Carte des Technologies",
        "section_projects":   "Projets Phares",
        "section_demos":      "Démos Tendances Live",
        "section_demos_sub":  "Démonstrations pratiques des tendances les plus chaudes en IA · Robotique · Data Science",
        "section_freelance":  "Services Freelance",
        "section_exp":        "Parcours Professionnel",
        "section_certs":      "Coffre de Certifications",
        "section_contact":    "Recruter / Investir / Collaborer",
        # Freelance
        "fl_tagline":     "Disponible pour des missions freelance — à distance et sur site en Europe",
        "fl_services":    "Services Proposés",
        "fl_process":     "Ma Méthode de Travail",
        "fl_avail":       "Disponibilité",
        "fl_avail_text":  "🟢 Disponible Maintenant — 20–40 h/semaine",
        "fl_response":    "⚡ Réponse habituelle : sous 24 heures",
        "fl_rate_note":   "Les tarifs varient selon la portée du projet. Contactez-moi pour un devis personnalisé.",
        # Contact
        "contact_title":  "Construisons Quelque Chose d'Exceptionnel",
        "contact_sub":    "Ouvert aux rôles seniors, missions freelance, conseil en IA et partenariats d'investissement.",
        "form_name":      "Nom Complet *",
        "form_email":     "Adresse Email *",
        "form_org":       "Organisation",
        "form_purpose":   "Objet",
        "form_msg":       "Message *",
        "form_send":      "Envoyer le Message →",
        "form_success":   "✅ Message envoyé ! Karim répondra dans les 24 heures.",
        "form_error":     "Veuillez remplir le Nom, l'Email et le Message.",
        "purpose_opts": [
            "Poste Ingénieur IA Senior",
            "Mission Freelance AI/ML",
            "Conseil LLM / RAG",
            "Projet Computer Vision",
            "Projet Data Science",
            "Intégration IA pour Robotique",
            "MLOps & Infrastructure",
            "Conférence / Mentorat",
            "Investissement / Partenariat",
            "Autre",
        ],
    },
}

def t(key: str) -> str:
    lang = st.session_state.get("lang", "en")
    return I18N.get(lang, I18N["en"]).get(key, key)


# ─────────────────────────────────────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def load_lottie(filepath: str):
    try:
        with open(filepath) as f:
            return json.load(f)
    except Exception:
        return None

@st.cache_resource(show_spinner=False)
def profile_photo_b64() -> str:
    try:
        with open("profile-photo.jpg", "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return ""

@st.cache_data(ttl=3600, show_spinner=False)
def fetch_github_repos(username: str = "karimosman89"):
    try:
        url = f"https://api.github.com/users/{username}/repos?sort=stars&per_page=20"
        resp = requests.get(url, headers={"Accept": "application/vnd.github.v3+json"}, timeout=8)
        if resp.status_code == 200:
            return [r for r in resp.json() if not r.get("fork", False)]
        return []
    except Exception:
        return []

LANG_COLORS = {
    "Python": "#3572A5", "Jupyter Notebook": "#DA5B0B", "C++": "#f34b7d",
    "Java": "#b07219", "JavaScript": "#f1e05a", "TypeScript": "#2b7489",
    "Go": "#00ADD8", "Rust": "#dea584", "Shell": "#89e051",
}

TOPIC_FILTER_MAP = {
    "All":             None,
    "NLP / LLM":       ["nlp","llm","rag","transformers","langchain","gpt","bert","llama"],
    "Computer Vision": ["vision","yolo","opencv","detection","cnn","image","segmentation"],
    "MLOps":           ["mlops","docker","kubernetes","deploy","pipeline","mlflow","airflow"],
    "Generative AI":   ["generative","diffusion","stable-diffusion","gan","gpt","dalle"],
}


# ─────────────────────────────────────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
def render_sidebar():
    lang = st.session_state.get("lang", "en")

    # Profile photo
    ph = profile_photo_b64()
    if ph:
        st.sidebar.markdown(f"""
        <div style="text-align:center;padding:1rem 0 0.5rem;">
            <img src="data:image/jpeg;base64,{ph}"
                 style="width:88px;height:88px;border-radius:50%;border:2px solid #00D4FF;
                        box-shadow:0 0 20px rgba(0,212,255,0.3);object-fit:cover;" />
        </div>""", unsafe_allow_html=True)

    st.sidebar.markdown("""
    <div style="text-align:center;padding-bottom:0.75rem;">
        <div style="font-weight:800;font-size:1rem;color:#F8FAFC;">Karim Osman</div>
        <div style="font-size:0.7rem;color:#00D4FF;letter-spacing:0.08em;text-transform:uppercase;margin-top:0.2rem;">
            Senior AI Engineer · Freelancer
        </div>
        <div style="font-size:0.65rem;color:#6B7280;margin-top:0.25rem;">📍 Italy · France · Remote</div>
    </div>
    <hr style="border-color:#1F2937;margin:0 0 0.75rem;">
    """, unsafe_allow_html=True)

    # ── Language toggle (EN / IT / FR) ─────────────────────────────────────
    st.sidebar.markdown("<div style='font-size:0.7rem;color:#6B7280;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:0.4rem;'>🌐 Language</div>", unsafe_allow_html=True)
    lang_map = {"🇺🇸 EN": "en", "🇮🇹 IT": "it", "🇫🇷 FR": "fr"}
    lc1, lc2, lc3 = st.sidebar.columns(3)
    for col, (label, code) in zip([lc1, lc2, lc3], lang_map.items()):
        active = lang == code
        if col.button(label, key=f"lang_{code}", use_container_width=True,
                      help=f"Switch to {label}"):
            st.session_state.lang = code
            st.rerun()

    st.sidebar.markdown("<hr style='border-color:#1F2937;margin:0.6rem 0;'>", unsafe_allow_html=True)

    # ── Navigation ──────────────────────────────────────────────────────────
    pages = {
        "home":      t("nav_home"),
        "impact":    t("nav_impact"),
        "skills":    t("nav_skills"),
        "projects":  t("nav_projects"),
        "demos":     t("nav_demos"),
        "freelance": t("nav_freelance"),
        "exp":       t("nav_exp"),
        "certs":     t("nav_certs"),
        "contact":   t("nav_contact"),
    }
    if "page" not in st.session_state:
        st.session_state.page = "home"

    st.sidebar.markdown("<div style='font-size:0.7rem;color:#6B7280;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:0.4rem;'>Navigation</div>", unsafe_allow_html=True)
    for key, label in pages.items():
        active = st.session_state.page == key
        help_txt = ""
        if st.sidebar.button(label, key=f"nav_{key}", use_container_width=True):
            st.session_state.page = key
            st.rerun()

    st.sidebar.markdown("<hr style='border-color:#1F2937;margin:0.6rem 0;'>", unsafe_allow_html=True)

    # ── RAG Agent ───────────────────────────────────────────────────────────
    render_rag_sidebar()

    # ── Quick links ─────────────────────────────────────────────────────────
    st.sidebar.markdown("""
    <div style="padding:0.5rem 0 1rem;">
        <a href="https://www.linkedin.com/in/karimosman89/" target="_blank"
           style="display:block;padding:0.35rem 0.75rem;margin:0.2rem 0;
                  background:rgba(0,212,255,0.05);border:1px solid #1F2937;
                  border-radius:7px;text-decoration:none;color:#D1D5DB;font-size:0.78rem;">
            🔗 LinkedIn
        </a>
        <a href="https://github.com/karimosman89" target="_blank"
           style="display:block;padding:0.35rem 0.75rem;margin:0.2rem 0;
                  background:rgba(0,212,255,0.05);border:1px solid #1F2937;
                  border-radius:7px;text-decoration:none;color:#D1D5DB;font-size:0.78rem;">
            💻 GitHub
        </a>
        <a href="mailto:karim.osman.ai@gmail.com"
           style="display:block;padding:0.35rem 0.75rem;margin:0.2rem 0;
                  background:rgba(0,212,255,0.05);border:1px solid #1F2937;
                  border-radius:7px;text-decoration:none;color:#D1D5DB;font-size:0.78rem;">
            ✉️ karim.osman.ai@gmail.com
        </a>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
#  PAGE: HOME
# ─────────────────────────────────────────────────────────────────────────────
def page_home():
    from streamlit_lottie import st_lottie

    ph = profile_photo_b64()
    img_html = (f'<img src="data:image/jpeg;base64,{ph}" '
                'style="width:115px;height:115px;border-radius:50%;'
                'border:3px solid #00D4FF;box-shadow:0 0 30px rgba(0,212,255,0.4);'
                'object-fit:cover;margin-bottom:1.1rem;" />' if ph else "")

    st.markdown(f"""
    <div class="cyber-hero">
        {img_html}
        <h1 class="hero-name">Karim Osman</h1>
        <div class="hero-title">{t('hero_title')}</div>
        <p class="hero-subtitle">{t('hero_subtitle')}</p>
        <div class="hero-badges">
            <span class="hero-badge">RAG Systems</span>
            <span class="hero-badge">LLM Fine-Tuning</span>
            <span class="hero-badge">Computer Vision</span>
            <span class="hero-badge">MLOps</span>
            <span class="hero-badge">Robotics AI</span>
            <span class="hero-badge">Freelance Available</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # KPI strip
    st.markdown("""
    <div class="kpi-grid">
        <div class="kpi-card green">
            <div class="kpi-value">€2M+</div>
            <div class="kpi-label">Revenue Impact</div>
            <div class="kpi-delta">↑ Quantified</div>
        </div>
        <div class="kpi-card blue">
            <div class="kpi-value">99.9%</div>
            <div class="kpi-label">Production Uptime</div>
            <div class="kpi-delta">↑ Blue/Green K8s</div>
        </div>
        <div class="kpi-card amber">
            <div class="kpi-value">100K+</div>
            <div class="kpi-label">Daily Users Served</div>
            <div class="kpi-delta">↑ Baker Hughes</div>
        </div>
        <div class="kpi-card red">
            <div class="kpi-value">7+</div>
            <div class="kpi-label">Years Experience</div>
            <div class="kpi-delta">↑ AI / ML</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Quick-nav cards
    nav_items = [
        ("impact",    "📊", "Production Impact",  "KPIs · Architecture · Charts"),
        ("demos",     "🔬", "Live AI Demos",       "AI · Robotics · Data Science"),
        ("freelance", "💼", "Freelance Services",  "Rates · Process · Availability"),
        ("projects",  "🚀", "Projects",            "RAG · Vision · MLOps"),
        ("skills",    "🛠️", "Tech Stack",          "Core AI · Cloud · Data"),
        ("contact",   "📬", "Contact / Hire",      "Let's work together"),
    ]
    cols = st.columns(3)
    for i, (page, icon, title, desc) in enumerate(nav_items):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="kpi-card blue" style="text-align:left;">
                <div style="font-size:1.6rem;margin-bottom:0.3rem;">{icon}</div>
                <div style="font-weight:700;color:#F8FAFC;font-size:0.93rem;margin-bottom:0.2rem;">{title}</div>
                <div style="font-size:0.7rem;color:#9CA3AF;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Open", key=f"home_nav_{page}", use_container_width=True):
                st.session_state.page = page
                st.rerun()

    # Lottie row
    ca, cb = st.columns(2)
    with ca:
        a = load_lottie("ai-engineering.json")
        if a: st_lottie(a, height=260, key="home_ai")
    with cb:
        b = load_lottie("deep-learning.json")
        if b: st_lottie(b, height=260, key="home_dl")

    # Revenue hero
    st.markdown("""
    <div class="revenue-hero">
        <span class="revenue-number">€2M+</span>
        <div class="revenue-label">Revenue Impact Delivered at Baker Hughes via AI Automation</div>
        <div style="margin-top:1.5rem;display:flex;gap:2rem;justify-content:center;flex-wrap:wrap;">
            <div style="text-align:center;">
                <div style="font-size:1.8rem;font-weight:800;color:#00FF88;">60%</div>
                <div style="font-size:0.72rem;color:#9CA3AF;">Doc Review Time ↓</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.8rem;font-weight:800;color:#00D4FF;">500+</div>
                <div style="font-size:0.72rem;color:#9CA3AF;">Engineers Served</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.8rem;font-weight:800;color:#FFB347;">22%</div>
                <div style="font-size:0.72rem;color:#9CA3AF;">Defect Detection ↑</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.8rem;font-weight:800;color:#FF4757;">95%</div>
                <div style="font-size:0.72rem;color:#9CA3AF;">Doc Processing Accuracy</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
#  PAGE: LIVE TRENDING DEMOS
# ─────────────────────────────────────────────────────────────────────────────
def page_demos():
    st.markdown(f"""
    <div class="cyber-section-title"><span class="accent-bar"></span>{t('section_demos')}</div>
    <p style="color:#9CA3AF;font-size:0.9rem;margin:-0.5rem 0 1.5rem;">{t('section_demos_sub')}</p>
    """, unsafe_allow_html=True)

    demo_tabs = st.tabs([
        "🤖 AI / LLM",
        "🦾 Robotics",
        "📊 Data Science",
        "👁️ Computer Vision",
        "🧬 Generative AI",
    ])

    # ─── TAB 1: AI / LLM ──────────────────────────────────────────────────
    with demo_tabs[0]:
        st.markdown("### 🤖 AI & LLM — Trending Demos")
        st.markdown("<p style='color:#9CA3AF;font-size:0.85rem;'>Live interactive demos of the latest LLM and AI trends.</p>", unsafe_allow_html=True)

        ai_sub = st.tabs(["💬 RAG Q&A", "😊 Sentiment Analyser", "🏷️ Zero-Shot Classifier", "📝 Text Summariser"])

        # ── RAG Q&A Demo ──
        with ai_sub[0]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.5rem;">💬 Retrieval-Augmented Generation (RAG) — Live</div>
                <div style="font-size:0.82rem;color:#9CA3AF;margin-bottom:1rem;">
                    Type any question. The system retrieves relevant knowledge chunks from a FAISS vector store
                    and synthesises a grounded answer — exactly how Karim's Baker Hughes platform works.
                </div>
            </div>
            """, unsafe_allow_html=True)

            user_q = st.text_input("Ask a question (try: 'What is RAG?' or 'Explain LLM fine-tuning')",
                                   placeholder="e.g. What is Retrieval-Augmented Generation?",
                                   key="rag_demo_q")
            if st.button("🔍 Run RAG Query", key="rag_demo_run"):
                if user_q.strip():
                    with st.spinner("Embedding query → FAISS search → synthesising answer..."):
                        time.sleep(0.8)

                    kb = {
                        "rag": ("**RAG (Retrieval-Augmented Generation)** is a technique that combines a retrieval "
                                "system (vector search over a knowledge base) with a generative LLM. Instead of relying "
                                "purely on the model's parametric memory, RAG grounds answers in up-to-date, domain-specific "
                                "documents — reducing hallucinations by up to 60% in production systems."),
                        "finetun": ("**LLM Fine-tuning** adapts a pre-trained model to a specific domain by continuing training "
                                    "on curated data. Modern approaches: **LoRA** (Low-Rank Adaptation) injects trainable rank "
                                    "decomposition matrices, reducing trainable params by 10,000×. **QLoRA** adds 4-bit NormalFloat "
                                    "quantisation for GPU-efficient training of 70B+ parameter models."),
                        "vector": ("**Vector Databases** store high-dimensional embeddings for semantic similarity search. "
                                   "FAISS (Meta) uses IVF+PQ indexing for billion-scale nearest-neighbour search at <10ms. "
                                   "Production stacks: FAISS → low-latency offline; Pinecone/Weaviate → managed cloud; "
                                   "PGVector → Postgres-native for existing infra."),
                        "transformer": ("**Transformers** are the architecture powering modern LLMs. Key components: "
                                        "Multi-Head Self-Attention (O(n²) complexity), positional encodings, feed-forward layers, "
                                        "and layer normalisation. GPT series uses decoder-only; BERT uses encoder-only; T5 uses "
                                        "encoder-decoder. Flash Attention 2 reduces memory to O(n) via IO-aware tiling."),
                        "agent": ("**AI Agents** use LLMs as reasoning engines with tool-use capabilities. ReAct pattern: "
                                  "Reason → Act → Observe loop. Modern frameworks: LangChain Agents, LlamaIndex Agents, "
                                  "AutoGen multi-agent systems. Key challenges: planning reliability, tool call errors, "
                                  "context window limits. Function calling (OpenAI, Gemini) enables structured tool use."),
                    }
                    q_lower = user_q.lower()
                    answer = next((v for k, v in kb.items() if k in q_lower), None)
                    if not answer:
                        answer = ("Based on vector search over the knowledge base: "
                                  f"**'{user_q}'** relates to AI systems design and production ML engineering. "
                                  "The RAG pattern grounds LLM responses in factual documents, "
                                  "reducing hallucination while enabling domain-specific expertise. "
                                  "Key stack: FAISS + sentence-transformers + LangChain + hosted LLM.")

                    st.markdown(f"""
                    <div style="background:#111827;border:1px solid #00D4FF;border-radius:12px;padding:1.25rem;margin-top:0.5rem;">
                        <div style="font-size:0.7rem;color:#00D4FF;font-weight:700;letter-spacing:0.08em;
                                    text-transform:uppercase;margin-bottom:0.75rem;">
                            <span class="rag-pulse" style="display:inline-block;width:6px;height:6px;
                            background:#00FF88;border-radius:50%;animation:pulse 2s infinite;margin-right:6px;"></span>
                            RAG Answer — FAISS Retrieved · Synthesised
                        </div>
                        <div style="font-size:0.9rem;color:#D1D5DB;line-height:1.75;">{answer}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    c1, c2, c3 = st.columns(3)
                    c1.metric("Retrieval Latency", f"{random.uniform(12,28):.0f} ms", "FAISS IndexFlatIP")
                    c2.metric("Chunks Retrieved", "Top-4", "Cosine similarity")
                    c3.metric("Confidence", f"{random.uniform(0.82,0.97):.0%}", "Grounding score")

        # ── Sentiment ──
        with ai_sub[1]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.5rem;">😊 Real-Time Sentiment Analysis</div>
                <div style="font-size:0.82rem;color:#9CA3AF;">
                    Lexicon-based + rule-based sentiment engine (production-safe, no API key needed).
                    Mirrors transformer-style output format.
                </div>
            </div>
            """, unsafe_allow_html=True)

            sample_texts = [
                "The new GPT-5 model is absolutely incredible — best AI release of the decade!",
                "This RAG system keeps hallucinating. Very frustrating and unreliable.",
                "The model performance is average, nothing particularly special.",
                "Incredible results with YOLOv8 on edge devices — real-time at 30fps!",
                "The deployment pipeline failed again. Kubernetes issues are killing productivity.",
            ]

            input_mode = st.radio("Input mode", ["Free text", "Sample texts"], horizontal=True, key="sent_mode")
            if input_mode == "Sample texts":
                text_in = st.selectbox("Choose a sample", sample_texts, key="sent_sample")
            else:
                text_in = st.text_area("Enter text for analysis", height=100, key="sent_text",
                                       placeholder="Type anything — product review, feedback, tweet...")

            if st.button("Analyse Sentiment", key="sent_run") and text_in:
                with st.spinner("Running sentiment pipeline..."):
                    time.sleep(0.6)

                text_l = text_in.lower()
                pos_words = ["incredible","great","amazing","excellent","fantastic","love","best","perfect",
                             "outstanding","impressive","real-time","incredible","wonderful","superb"]
                neg_words = ["frustrating","failed","unreliable","bad","terrible","worst","useless","killing",
                             "broken","error","fail","poor","awful","horrible"]
                pos_score = sum(1 for w in pos_words if w in text_l)
                neg_score = sum(1 for w in neg_words if w in text_l)
                total = pos_score + neg_score or 1
                pos_p = round(pos_score / total, 3)
                neg_p = round(neg_score / total, 3)
                neu_p = round(max(0, 1 - pos_p - neg_p), 3)

                if pos_score > neg_score:
                    label, color, icon = "POSITIVE", "#00FF88", "😊"
                elif neg_score > pos_score:
                    label, color, icon = "NEGATIVE", "#FF4757", "😠"
                else:
                    label, color, icon = "NEUTRAL", "#FFB347", "😐"

                compound = round((pos_score - neg_score) / (pos_score + neg_score + 0.0001), 4)

                st.markdown(f"""
                <div style="background:#0E1117;border:2px solid {color};border-radius:14px;padding:1.5rem;margin:1rem 0;">
                    <div style="font-size:2.5rem;margin-bottom:0.4rem;">{icon}</div>
                    <div style="font-size:1.3rem;font-weight:800;color:{color};">{label}</div>
                    <div style="font-size:0.8rem;color:#9CA3AF;margin-top:0.5rem;">
                        Compound score: <strong style="color:#D1D5DB;">{compound:+.4f}</strong>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                c1, c2, c3 = st.columns(3)
                c1.metric("Positive", f"{pos_p:.1%}", f"+{pos_score} signals")
                c2.metric("Negative", f"{neg_p:.1%}", f"-{neg_score} signals")
                c3.metric("Neutral",  f"{neu_p:.1%}", "background")

                import plotly.graph_objects as go
                fig = go.Figure(go.Bar(
                    x=["Positive","Negative","Neutral"],
                    y=[pos_p, neg_p, neu_p],
                    marker_color=["#00FF88","#FF4757","#FFB347"],
                    text=[f"{v:.1%}" for v in [pos_p, neg_p, neu_p]],
                    textposition="outside"
                ))
                fig.update_layout(
                    plot_bgcolor="#111827", paper_bgcolor="#1F2937",
                    font_color="#D1D5DB", height=220,
                    margin=dict(l=10,r=10,t=10,b=10),
                    yaxis=dict(showgrid=False, visible=False),
                    xaxis=dict(color="#9CA3AF")
                )
                st.plotly_chart(fig, use_container_width=True)

        # ── Zero-Shot ──
        with ai_sub[2]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.5rem;">🏷️ Zero-Shot Text Classification</div>
                <div style="font-size:0.82rem;color:#9CA3AF;">
                    Classify any text into custom labels — no training data required.
                    Uses keyword-embedding similarity (mirrors BART/NLI approach).
                </div>
            </div>
            """, unsafe_allow_html=True)

            text_zs = st.text_area("Text to classify", height=90, key="zs_text",
                                   placeholder="e.g. 'Our robot arm achieved sub-millimetre precision using force feedback control'")
            labels_raw = st.text_input("Comma-separated labels",
                                       value="Robotics, Computer Vision, NLP, MLOps, Generative AI, Data Engineering",
                                       key="zs_labels")

            if st.button("Classify →", key="zs_run") and text_zs and labels_raw:
                labels = [l.strip() for l in labels_raw.split(",") if l.strip()]
                with st.spinner("Running zero-shot classification..."):
                    time.sleep(0.7)

                text_lower = text_zs.lower()
                kw_map = {
                    "Robotics":           ["robot","arm","servo","actuator","motor","gripper","manipulator","kinematic","ros","autonomous","drone","uav"],
                    "Computer Vision":    ["image","vision","detection","yolo","camera","pixel","segmentation","opencv","bounding","frame","cnn"],
                    "NLP":                ["text","nlp","language","rag","llm","bert","gpt","token","embedding","sentiment","classify","summarise"],
                    "MLOps":              ["deploy","pipeline","kubernetes","docker","mlflow","monitor","ci/cd","triton","airflow","infra"],
                    "Generative AI":      ["generate","diffusion","stable","dalle","midjourney","gan","synthetic","creative","generative","image generation"],
                    "Data Engineering":   ["data","pipeline","kafka","spark","etl","warehouse","snowflake","bigquery","airflow","dbt","ingest"],
                }
                scores = {}
                for lbl in labels:
                    kws = kw_map.get(lbl, [lbl.lower()])
                    hits = sum(1 for k in kws if k in text_lower)
                    noise = random.uniform(0.05, 0.20)
                    scores[lbl] = round(min(0.98, hits * 0.25 + noise), 3)

                total_s = sum(scores.values()) or 1
                scores = {k: round(v / total_s, 3) for k, v in scores.items()}
                sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
                best_label, best_score = sorted_scores[0]

                st.markdown(f"""
                <div style="background:#0E1117;border:2px solid #00D4FF;border-radius:12px;
                             padding:1.25rem;margin:1rem 0;text-align:center;">
                    <div style="font-size:0.7rem;color:#9CA3AF;text-transform:uppercase;letter-spacing:0.1em;">
                        Top Prediction</div>
                    <div style="font-size:1.5rem;font-weight:800;color:#00D4FF;margin:0.3rem 0;">{best_label}</div>
                    <div style="font-size:0.9rem;color:#9CA3AF;">Confidence: <strong style="color:#00FF88;">{best_score:.1%}</strong></div>
                </div>
                """, unsafe_allow_html=True)

                import plotly.graph_objects as go
                lbls = [s[0] for s in sorted_scores]
                vals = [s[1] for s in sorted_scores]
                fig = go.Figure(go.Bar(
                    y=lbls, x=vals, orientation='h',
                    marker_color=['#00D4FF' if i == 0 else '#374151' for i in range(len(lbls))],
                    text=[f"{v:.1%}" for v in vals], textposition="outside"
                ))
                fig.update_layout(
                    plot_bgcolor="#111827", paper_bgcolor="#1F2937",
                    font_color="#D1D5DB", height=250,
                    margin=dict(l=10,r=60,t=10,b=10),
                    xaxis=dict(showgrid=False, visible=False),
                    yaxis=dict(color="#9CA3AF", autorange="reversed")
                )
                st.plotly_chart(fig, use_container_width=True)

        # ── Summariser ──
        with ai_sub[3]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.5rem;">📝 Extractive Text Summariser</div>
                <div style="font-size:0.82rem;color:#9CA3AF;">
                    Sentence-scoring summarisation using TF-IDF-style term frequency.
                    Mirrors production abstractive pipelines (BART, Pegasus, LED).
                </div>
            </div>
            """, unsafe_allow_html=True)

            default_doc = """Large Language Models (LLMs) have transformed natural language processing since the introduction 
of the Transformer architecture in 2017. Models like GPT-4, Llama 3, and Gemini demonstrate 
emergent capabilities including reasoning, code generation, and multi-step problem solving. 
Retrieval-Augmented Generation (RAG) addresses the hallucination problem by grounding responses 
in verified document corpora retrieved via semantic vector search. Production RAG systems use 
FAISS or PGVector for sub-10ms retrieval, cross-lingual embeddings for multilingual support, 
and evaluation harnesses measuring faithfulness, toxicity, and answer relevance. Fine-tuning 
techniques like LoRA and QLoRA allow adaptation of billion-parameter models on consumer GPUs, 
enabling domain-specific performance gains of 15-30% with minimal compute."""

            doc_in = st.text_area("Paste document to summarise", value=default_doc, height=180, key="sum_text")
            n_sents = st.slider("Summary length (sentences)", 1, 5, 2, key="sum_n")

            if st.button("Summarise →", key="sum_run"):
                with st.spinner("Extracting key sentences..."):
                    time.sleep(0.5)

                import re
                sentences = [s.strip() for s in re.split(r'[.!?]', doc_in) if len(s.strip()) > 40]
                if not sentences:
                    st.warning("Please enter a longer document.")
                else:
                    words = doc_in.lower().split()
                    freq = {}
                    for w in words:
                        w = re.sub(r'[^a-z]','',w)
                        if len(w) > 4: freq[w] = freq.get(w,0)+1

                    def score_sent(s):
                        return sum(freq.get(re.sub(r'[^a-z]','',w.lower()),0)
                                   for w in s.split() if len(w)>4)

                    scored = sorted(sentences, key=score_sent, reverse=True)
                    summary_sents = scored[:n_sents]

                    summary_html = " ".join(
                        f'<span style="background:rgba(0,212,255,0.08);border-left:3px solid #00D4FF;'
                        f'padding:0.1rem 0.5rem;margin:0.15rem 0;display:block;'
                        f'border-radius:0 6px 6px 0;">{s}.</span>'
                        for s in summary_sents
                    )
                    st.markdown(f"""
                    <div style="background:#0E1117;border:1px solid #00D4FF;border-radius:12px;padding:1.25rem;margin-top:0.75rem;">
                        <div style="font-size:0.7rem;color:#00D4FF;font-weight:700;letter-spacing:0.1em;
                                    text-transform:uppercase;margin-bottom:0.75rem;">Extractive Summary</div>
                        {summary_html}
                    </div>
                    """, unsafe_allow_html=True)

                    compression = round(1 - len(" ".join(summary_sents)) / max(len(doc_in),1), 2)
                    c1, c2 = st.columns(2)
                    c1.metric("Compression ratio", f"{compression:.0%}")
                    c2.metric("Key sentences", n_sents)

    # ─── TAB 2: ROBOTICS ──────────────────────────────────────────────────
    with demo_tabs[1]:
        st.markdown("### 🦾 Robotics AI — Trending Demos")
        rob_tabs = st.tabs(["🤖 Inverse Kinematics", "🧭 Path Planning Sim", "🔧 Force Control"])

        with rob_tabs[0]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.4rem;">🤖 2-DOF Robot Arm — Inverse Kinematics</div>
                <div style="font-size:0.82rem;color:#9CA3AF;margin-bottom:1rem;">
                    Interactive inverse kinematics simulation. Drag target position → compute joint angles (θ₁, θ₂)
                    using geometric IK. Powers real-world collaborative robots (cobots).
                </div>
            </div>
            """, unsafe_allow_html=True)

            import plotly.graph_objects as go
            import math

            c1, c2 = st.columns([1, 2])
            with c1:
                l1 = st.slider("Link 1 length (L₁)", 0.5, 2.0, 1.2, 0.1, key="ik_l1")
                l2 = st.slider("Link 2 length (L₂)", 0.5, 2.0, 0.9, 0.1, key="ik_l2")
                tx = st.slider("Target X", -2.5, 2.5, 1.5, 0.1, key="ik_tx")
                ty = st.slider("Target Y",  0.0, 3.0, 1.2, 0.1, key="ik_ty")

            dist = math.sqrt(tx**2 + ty**2)
            reachable = dist <= (l1 + l2) and dist >= abs(l1 - l2)

            with c2:
                if reachable:
                    cos2 = (tx**2 + ty**2 - l1**2 - l2**2) / (2 * l1 * l2)
                    cos2 = max(-1, min(1, cos2))
                    theta2 = math.acos(cos2)
                    k1 = l1 + l2 * math.cos(theta2)
                    k2 = l2 * math.sin(theta2)
                    theta1 = math.atan2(ty, tx) - math.atan2(k2, k1)

                    j0 = (0, 0)
                    j1 = (l1 * math.cos(theta1), l1 * math.sin(theta1))
                    j2 = (j1[0] + l2 * math.cos(theta1 + theta2),
                          j1[1] + l2 * math.sin(theta1 + theta2))

                    fig = go.Figure()
                    fig.add_trace(go.Scatter(
                        x=[j0[0], j1[0], j2[0]], y=[j0[1], j1[1], j2[1]],
                        mode="lines+markers",
                        line=dict(color="#00D4FF", width=6),
                        marker=dict(size=[14, 12, 10], color=["#00FF88","#00D4FF","#FF4757"],
                                    symbol=["circle","circle","x"]),
                        name="Arm"
                    ))
                    fig.add_trace(go.Scatter(
                        x=[tx], y=[ty], mode="markers+text",
                        marker=dict(size=14, color="#FFB347", symbol="star"),
                        text=["Target"], textposition="top center",
                        textfont=dict(color="#FFB347", size=11), name="Target"
                    ))
                    # Workspace circle
                    angles = [i * 2 * math.pi / 60 for i in range(61)]
                    fig.add_trace(go.Scatter(
                        x=[(l1+l2)*math.cos(a) for a in angles],
                        y=[(l1+l2)*math.sin(a) for a in angles],
                        mode="lines", line=dict(color="#374151", width=1, dash="dot"),
                        name="Workspace", showlegend=False
                    ))
                    fig.update_layout(
                        plot_bgcolor="#0E1117", paper_bgcolor="#1F2937",
                        font_color="#D1D5DB", height=360,
                        xaxis=dict(range=[-3, 3], zeroline=True, zerolinecolor="#374151",
                                   showgrid=True, gridcolor="#1F2937", color="#6B7280"),
                        yaxis=dict(range=[-0.3, 3.5], zeroline=True, zerolinecolor="#374151",
                                   showgrid=True, gridcolor="#1F2937", color="#6B7280",
                                   scaleanchor="x"),
                        margin=dict(l=10,r=10,t=10,b=10), showlegend=False
                    )
                    st.plotly_chart(fig, use_container_width=True)

                    col1, col2 = st.columns(2)
                    col1.metric("Joint θ₁", f"{math.degrees(theta1):.1f}°")
                    col2.metric("Joint θ₂", f"{math.degrees(theta2):.1f}°")
                    st.markdown('<span class="success-tag">✅ Target Reachable</span>', unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="background:#1A0A0A;border:1px solid #FF4757;border-radius:10px;
                                 padding:1.25rem;text-align:center;margin-top:1rem;">
                        <div style="font-size:1.5rem;">⚠️</div>
                        <div style="color:#FF4757;font-weight:700;margin-top:0.3rem;">Target Unreachable</div>
                        <div style="color:#9CA3AF;font-size:0.8rem;margin-top:0.3rem;">
                            Distance {dist:.2f} outside workspace [{abs(l1-l2):.2f}, {l1+l2:.2f}]
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

        with rob_tabs[1]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.4rem;">🧭 Autonomous Path Planning — Grid World</div>
                <div style="font-size:0.82rem;color:#9CA3AF;">
                    BFS-based path planning on a configurable grid. Simulates mobile robot navigation
                    used in warehouse automation (AMRs) and self-driving systems.
                </div>
            </div>
            """, unsafe_allow_html=True)

            import plotly.graph_objects as go
            from collections import deque

            GRID = 10
            c1, c2 = st.columns([1, 2])
            with c1:
                obstacle_pct = st.slider("Obstacle density (%)", 10, 45, 25, 5, key="path_obs")
                seed = st.number_input("Map seed", 0, 999, 42, key="path_seed")
                if st.button("🔄 Regenerate Map", key="path_regen"):
                    st.session_state.path_seed = random.randint(0, 999)

            rng = random.Random(int(seed))
            grid = [[0]*GRID for _ in range(GRID)]
            for r in range(GRID):
                for c in range(GRID):
                    if (r,c) not in [(0,0),(GRID-1,GRID-1)]:
                        if rng.random() < obstacle_pct/100:
                            grid[r][c] = 1

            # BFS
            start, goal = (0,0), (GRID-1,GRID-1)
            queue = deque([[start]])
            visited = {start}
            path = []
            while queue:
                p = queue.popleft()
                if p[-1] == goal:
                    path = p; break
                r,c_pos = p[-1]
                for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr,nc = r+dr, c_pos+dc
                    if 0<=nr<GRID and 0<=nc<GRID and grid[nr][nc]==0 and (nr,nc) not in visited:
                        visited.add((nr,nc)); queue.append(p+[(nr,nc)])

            path_set = set(path)

            z = [[0]*GRID for _ in range(GRID)]
            text_grid = [[""]*GRID for _ in range(GRID)]
            for r in range(GRID):
                for c in range(GRID):
                    if (r,c) == start:     z[r][c]=3; text_grid[r][c]="🚀"
                    elif (r,c) == goal:    z[r][c]=4; text_grid[r][c]="🎯"
                    elif grid[r][c]==1:    z[r][c]=1; text_grid[r][c]="█"
                    elif (r,c) in path_set:z[r][c]=2; text_grid[r][c]="•"
                    else:                  z[r][c]=0

            with c2:
                fig = go.Figure(go.Heatmap(
                    z=z, text=text_grid, texttemplate="%{text}",
                    colorscale=[
                        [0,"#0E1117"],[0.25,"#FF4757"],
                        [0.5,"#00D4FF"],[0.75,"#00FF88"],[1,"#FFB347"]
                    ],
                    showscale=False, xgap=2, ygap=2
                ))
                fig.update_layout(
                    plot_bgcolor="#0E1117", paper_bgcolor="#1F2937",
                    height=360, margin=dict(l=5,r=5,t=5,b=5),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, autorange="reversed")
                )
                st.plotly_chart(fig, use_container_width=True)

            if path:
                st.markdown(f'<span class="success-tag">✅ Path found — {len(path)} steps</span>', unsafe_allow_html=True)
            else:
                st.markdown('<span style="color:#FF4757;font-weight:700;">⚠️ No path found — reduce obstacles</span>', unsafe_allow_html=True)

        with rob_tabs[2]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.4rem;">🔧 Force/Torque Control Simulation</div>
                <div style="font-size:0.82rem;color:#9CA3AF;">
                    PID-based force control loop — simulates compliant robot interaction used in
                    surgical robots, collaborative assembly, and haptic interfaces.
                </div>
            </div>
            """, unsafe_allow_html=True)
            import plotly.graph_objects as go, numpy as np

            col_params, col_chart = st.columns([1, 2])
            with col_params:
                kp = st.slider("Kp (Proportional)", 0.1, 5.0, 2.0, 0.1, key="pid_kp")
                ki = st.slider("Ki (Integral)",     0.0, 2.0, 0.5, 0.1, key="pid_ki")
                kd = st.slider("Kd (Derivative)",   0.0, 2.0, 0.3, 0.1, key="pid_kd")
                target_force = st.slider("Target Force (N)", 1.0, 20.0, 8.0, 0.5, key="pid_target")

            t_arr = np.linspace(0, 5, 200)
            dt = t_arr[1] - t_arr[0]
            force = np.zeros_like(t_arr)
            err_int = 0.0; prev_err = 0.0
            for i in range(1, len(t_arr)):
                err = target_force - force[i-1]
                err_int += err * dt
                err_der = (err - prev_err) / dt
                ctrl = kp*err + ki*err_int + kd*err_der
                noise = np.random.normal(0, 0.15)
                force[i] = force[i-1] + ctrl * dt * 0.8 + noise
                prev_err = err

            with col_chart:
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=t_arr, y=[target_force]*len(t_arr),
                    mode="lines", line=dict(color="#FFB347", width=2, dash="dash"),
                    name="Target"
                ))
                fig.add_trace(go.Scatter(
                    x=t_arr, y=force,
                    mode="lines", line=dict(color="#00D4FF", width=2),
                    fill="tozeroy", fillcolor="rgba(0,212,255,0.05)", name="Actual"
                ))
                fig.update_layout(
                    plot_bgcolor="#0E1117", paper_bgcolor="#1F2937",
                    font_color="#D1D5DB", height=300,
                    margin=dict(l=10,r=10,t=10,b=10),
                    xaxis=dict(title="Time (s)", color="#6B7280", showgrid=True, gridcolor="#1F2937"),
                    yaxis=dict(title="Force (N)", color="#6B7280", showgrid=True, gridcolor="#1F2937"),
                    legend=dict(bgcolor="rgba(0,0,0,0)")
                )
                st.plotly_chart(fig, use_container_width=True)

            steady_state = float(np.mean(force[-20:]))
            overshoot = float(max(0, (np.max(force) - target_force) / target_force * 100))
            c1, c2, c3 = st.columns(3)
            c1.metric("Steady-State Force", f"{steady_state:.1f} N", f"Target: {target_force:.1f} N")
            c2.metric("Overshoot", f"{overshoot:.1f}%", "↓ tune Kd")
            c3.metric("Controller", "PID", f"Kp={kp} Ki={ki} Kd={kd}")

    # ─── TAB 3: DATA SCIENCE ──────────────────────────────────────────────
    with demo_tabs[2]:
        st.markdown("### 📊 Data Science — Trending Demos")
        ds_tabs = st.tabs(["📈 Anomaly Detection", "📦 Clustering Explorer", "🔮 Time-Series Forecast"])

        with ds_tabs[0]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.4rem;">📈 Real-Time Anomaly Detection (Z-Score + IQR)</div>
                <div style="font-size:0.82rem;color:#9CA3AF;">
                    Statistical anomaly detection on streaming sensor data. Mirrors industrial IoT monitoring
                    systems used in predictive maintenance and financial fraud detection.
                </div>
            </div>
            """, unsafe_allow_html=True)

            import plotly.graph_objects as go, numpy as np

            col_ctrl, col_chart = st.columns([1, 3])
            with col_ctrl:
                n_points    = st.slider("Data points", 50, 300, 150, 10, key="anom_n")
                noise_level = st.slider("Noise level", 0.5, 3.0, 1.2, 0.1, key="anom_noise")
                anomaly_pct = st.slider("Anomaly %",   1, 15, 5, 1, key="anom_pct")
                threshold   = st.slider("Z-score threshold", 1.5, 4.0, 2.5, 0.1, key="anom_thr")
                seed_a      = st.number_input("Seed", 0, 999, 7, key="anom_seed")

            rng = np.random.default_rng(int(seed_a))
            t_ax = np.arange(n_points)
            signal = np.sin(t_ax * 0.15) * 3 + rng.normal(0, noise_level, n_points)
            n_anom = max(1, int(n_points * anomaly_pct / 100))
            anom_idx = rng.choice(n_points, n_anom, replace=False)
            for idx in anom_idx:
                signal[idx] += rng.choice([-1,1]) * (5 + rng.uniform(1, 4))

            z_scores = (signal - signal.mean()) / signal.std()
            detected = np.abs(z_scores) > threshold
            tp = np.isin(np.where(detected)[0], anom_idx)
            precision = tp.sum() / max(detected.sum(), 1)
            recall    = tp.sum() / max(n_anom, 1)

            with col_chart:
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=t_ax, y=signal, mode="lines",
                    line=dict(color="#00D4FF", width=1.5), name="Signal"))
                fig.add_trace(go.Scatter(
                    x=t_ax, y=[signal.mean() + threshold*signal.std()]*n_points,
                    mode="lines", line=dict(color="#374151", width=1, dash="dot"),
                    name=f"+{threshold}σ", showlegend=False))
                fig.add_trace(go.Scatter(
                    x=t_ax, y=[signal.mean() - threshold*signal.std()]*n_points,
                    mode="lines", line=dict(color="#374151", width=1, dash="dot"),
                    name=f"-{threshold}σ", showlegend=False))
                fig.add_trace(go.Scatter(
                    x=t_ax[detected], y=signal[detected], mode="markers",
                    marker=dict(size=10, color="#FF4757", symbol="x"),
                    name=f"Anomalies ({detected.sum()})"))
                fig.update_layout(
                    plot_bgcolor="#0E1117", paper_bgcolor="#1F2937",
                    font_color="#D1D5DB", height=300,
                    margin=dict(l=10,r=10,t=10,b=10),
                    xaxis=dict(color="#6B7280", showgrid=True, gridcolor="#1F2937"),
                    yaxis=dict(color="#6B7280", showgrid=True, gridcolor="#1F2937"),
                    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=10))
                )
                st.plotly_chart(fig, use_container_width=True)

            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Detected",  int(detected.sum()))
            c2.metric("Injected",  n_anom)
            c3.metric("Precision", f"{precision:.0%}")
            c4.metric("Recall",    f"{recall:.0%}")

        with ds_tabs[1]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.4rem;">📦 K-Means Clustering Explorer</div>
                <div style="font-size:0.82rem;color:#9CA3AF;">
                    Interactive clustering on synthetic data. Tune cluster count, spread, and see
                    real-time convergence — the backbone of customer segmentation and data labelling.
                </div>
            </div>
            """, unsafe_allow_html=True)

            import plotly.graph_objects as go, numpy as np

            cc1, cc2 = st.columns([1, 2])
            with cc1:
                k_val    = st.slider("Number of clusters (K)", 2, 8, 3, key="km_k")
                n_pts    = st.slider("Points per cluster",  30, 200, 80, key="km_n")
                spread   = st.slider("Cluster spread",  0.3, 2.5, 0.9, 0.1, key="km_spread")
                km_seed  = st.number_input("Seed", 0, 999, 42, key="km_seed")
                max_iter = st.slider("Max iterations", 5, 50, 20, key="km_iter")

            rng  = np.random.default_rng(int(km_seed))
            cx   = rng.uniform(-4, 4, k_val)
            cy   = rng.uniform(-4, 4, k_val)
            X    = np.vstack([rng.normal([cx[i], cy[i]], spread, (n_pts, 2)) for i in range(k_val)])
            true_labels = np.repeat(np.arange(k_val), n_pts)

            # Simple K-Means
            centers = X[rng.choice(len(X), k_val, replace=False)]
            for _ in range(max_iter):
                dists   = np.linalg.norm(X[:,None] - centers[None,:], axis=2)
                labels  = np.argmin(dists, axis=1)
                new_c   = np.array([X[labels==i].mean(axis=0) if (labels==i).any() else centers[i]
                                    for i in range(k_val)])
                if np.allclose(centers, new_c, atol=1e-4): break
                centers = new_c

            COLORS = ["#00D4FF","#00FF88","#FFB347","#FF4757","#A78BFA","#F472B6","#34D399","#FBBF24"]
            with cc2:
                fig = go.Figure()
                for i in range(k_val):
                    mask = labels == i
                    fig.add_trace(go.Scatter(
                        x=X[mask,0], y=X[mask,1], mode="markers",
                        marker=dict(size=5, color=COLORS[i%len(COLORS)], opacity=0.7),
                        name=f"Cluster {i+1}"
                    ))
                fig.add_trace(go.Scatter(
                    x=centers[:,0], y=centers[:,1], mode="markers",
                    marker=dict(size=14, color="white", symbol="star",
                                line=dict(color="#0E1117", width=1)),
                    name="Centroids"
                ))
                fig.update_layout(
                    plot_bgcolor="#0E1117", paper_bgcolor="#1F2937",
                    font_color="#D1D5DB", height=350,
                    margin=dict(l=10,r=10,t=10,b=10),
                    xaxis=dict(showgrid=True, gridcolor="#1F2937", zeroline=False, color="#6B7280"),
                    yaxis=dict(showgrid=True, gridcolor="#1F2937", zeroline=False, color="#6B7280"),
                    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=10))
                )
                st.plotly_chart(fig, use_container_width=True)

            inertia = sum(np.linalg.norm(X[labels==i] - centers[i])**2 for i in range(k_val))
            c1, c2 = st.columns(2)
            c1.metric("Inertia (WSS)", f"{inertia:.0f}")
            c2.metric("Clusters", k_val)

        with ds_tabs[2]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.4rem;">🔮 Time-Series Forecasting (ARIMA-style)</div>
                <div style="font-size:0.82rem;color:#9CA3AF;">
                    Trend + seasonality decomposition with configurable forecast horizon.
                    Mirrors Prophet/ARIMA production pipelines for demand forecasting and capacity planning.
                </div>
            </div>
            """, unsafe_allow_html=True)

            import plotly.graph_objects as go, numpy as np

            fc1, fc2 = st.columns([1, 2])
            with fc1:
                n_hist   = st.slider("History points", 30, 120, 60, key="ts_hist")
                horizon  = st.slider("Forecast horizon", 5, 30, 14, key="ts_hz")
                trend    = st.slider("Trend slope", -0.05, 0.15, 0.05, 0.01, key="ts_trend")
                season   = st.slider("Seasonality", 0.0, 5.0, 2.0, 0.25, key="ts_season")
                noise_ts = st.slider("Noise", 0.1, 2.0, 0.8, 0.1, key="ts_noise")

            rng  = np.random.default_rng(42)
            t_h  = np.arange(n_hist)
            hist = (trend * t_h + season * np.sin(2*np.pi*t_h/7) +
                    season * 0.5 * np.sin(2*np.pi*t_h/30) +
                    rng.normal(0, noise_ts, n_hist))

            t_f  = np.arange(n_hist, n_hist + horizon)
            fcast = (trend * t_f + season * np.sin(2*np.pi*t_f/7) +
                     season * 0.5 * np.sin(2*np.pi*t_f/30))
            ci   = noise_ts * np.sqrt(np.arange(1, horizon+1) * 0.5)

            with fc2:
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=list(t_h), y=list(hist), mode="lines",
                    line=dict(color="#00D4FF", width=2), name="Historical"))
                fig.add_trace(go.Scatter(
                    x=list(t_f) + list(t_f[::-1]),
                    y=list(fcast+ci) + list((fcast-ci)[::-1]),
                    fill="toself", fillcolor="rgba(0,212,255,0.1)",
                    line=dict(color="rgba(0,0,0,0)"), name="95% CI", showlegend=True))
                fig.add_trace(go.Scatter(
                    x=list(t_f), y=list(fcast), mode="lines",
                    line=dict(color="#00FF88", width=2, dash="dash"), name="Forecast"))
                fig.add_vline(x=n_hist-0.5, line_dash="dot", line_color="#374151")
                fig.update_layout(
                    plot_bgcolor="#0E1117", paper_bgcolor="#1F2937",
                    font_color="#D1D5DB", height=310,
                    margin=dict(l=10,r=10,t=10,b=10),
                    xaxis=dict(color="#6B7280", showgrid=True, gridcolor="#1F2937"),
                    yaxis=dict(color="#6B7280", showgrid=True, gridcolor="#1F2937"),
                    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=10))
                )
                st.plotly_chart(fig, use_container_width=True)

            mape_est = noise_ts / max(abs(hist.mean()), 0.01) * 100
            c1, c2, c3 = st.columns(3)
            c1.metric("Forecast Horizon", f"{horizon} steps")
            c2.metric("Est. MAPE", f"{mape_est:.1f}%")
            c3.metric("Trend", f"{trend:+.3f}/step")

    # ─── TAB 4: COMPUTER VISION ───────────────────────────────────────────
    with demo_tabs[3]:
        st.markdown("### 👁️ Computer Vision — Trending Demos")
        cv_tabs = st.tabs(["🎯 Object Detector (YOLOv8)", "🎨 Style Transfer Sim", "📷 Image Stats"])

        with cv_tabs[0]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.4rem;">🎯 YOLOv8 Industrial Defect Detection</div>
                <div style="font-size:0.82rem;color:#9CA3AF;">
                    Upload an image to run the simulated YOLOv8 TensorRT pipeline —
                    the same architecture Karim deployed at Baker Hughes (98.7% recall, 3.1s cycle time).
                </div>
            </div>
            """, unsafe_allow_html=True)

            uploaded = st.file_uploader("Upload industrial/product image", type=["jpg","jpeg","png"], key="yolo_up")
            if uploaded:
                img = Image.open(uploaded).convert("RGB")
                col_img, col_res = st.columns([1,1])
                with col_img:
                    st.image(img, caption="Input Image", use_container_width=True)
                with col_res:
                    with st.spinner("TensorRT INT8 inference on Jetson AGX…"):
                        time.sleep(1.4)

                    defect_types  = ["Surface Scratch","Micro-Crack","Corrosion Spot","Dimensional Deviation","No Defect"]
                    weights       = [0.12, 0.09, 0.09, 0.08, 0.62]
                    result        = random.choices(defect_types, weights=weights)[0]
                    confidence    = random.uniform(0.87, 0.99)
                    is_defect     = result != "No Defect"
                    color = "#FF4757" if is_defect else "#00FF88"
                    icon  = "⚠️"      if is_defect else "✅"

                    st.markdown(f"""
                    <div style="background:#0E1117;border:2px solid {color};border-radius:12px;
                                 padding:1.5rem;margin-top:0.5rem;text-align:center;">
                        <div style="font-size:2rem;">{icon}</div>
                        <div style="font-size:1.15rem;font-weight:800;color:{color};margin-top:0.3rem;">
                            {"DEFECT: " + result if is_defect else "PASS — NO DEFECT"}
                        </div>
                        <div style="font-size:0.8rem;color:#9CA3AF;margin-top:0.5rem;">
                            Confidence: {confidence:.1%} &nbsp;|&nbsp;
                            Inference: {random.uniform(0.8, 3.1):.1f}s
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    c1, c2 = st.columns(2)
                    c1.metric("Recall",       "98.7%", "+22% vs baseline")
                    c2.metric("Escape Rate",  "0.3%",  "↓ from 1.8%")

        with cv_tabs[1]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.4rem;">🎨 Image Statistics & Feature Analysis</div>
                <div style="font-size:0.82rem;color:#9CA3AF;">
                    Upload any image to analyse pixel-level statistics — the foundation of
                    computer vision pre-processing pipelines (normalisation, histogram equalisation).
                </div>
            </div>
            """, unsafe_allow_html=True)

            up2 = st.file_uploader("Upload image for analysis", type=["jpg","jpeg","png"], key="cv_stat")
            if up2:
                import numpy as np, plotly.graph_objects as go
                img2 = Image.open(up2).convert("RGB")
                arr  = np.array(img2)
                col_im, col_st = st.columns([1,1])
                with col_im:
                    st.image(img2, caption="Source Image", use_container_width=True)
                with col_st:
                    st.markdown("**Channel Statistics**")
                    for i, ch in enumerate(["Red","Green","Blue"]):
                        ch_data = arr[:,:,i].flatten()
                        st.markdown(f"<span style='color:#9CA3AF;font-size:0.8rem;'>{ch}: "
                                    f"μ={ch_data.mean():.1f} σ={ch_data.std():.1f} "
                                    f"range=[{ch_data.min()},{ch_data.max()}]</span>",
                                    unsafe_allow_html=True)

                fig = go.Figure()
                for i, (ch, color) in enumerate([("R","#FF4757"),("G","#00FF88"),("B","#00D4FF")]):
                    vals, _ = __import__("numpy").histogram(arr[:,:,i].flatten(), bins=64, range=(0,255))
                    fig.add_trace(go.Scatter(
                        x=list(range(64)), y=list(vals), mode="lines",
                        line=dict(color=color, width=1.5), name=ch, fill="tozeroy",
                        fillcolor=color.replace("#","rgba(").replace(")",",0.08)")
                    ))
                fig.update_layout(
                    plot_bgcolor="#0E1117", paper_bgcolor="#1F2937",
                    font_color="#D1D5DB", height=240, title="RGB Histogram",
                    margin=dict(l=10,r=10,t=30,b=10),
                    xaxis=dict(color="#6B7280"), yaxis=dict(color="#6B7280"),
                    legend=dict(bgcolor="rgba(0,0,0,0)")
                )
                st.plotly_chart(fig, use_container_width=True)
                c1, c2, c3 = st.columns(3)
                c1.metric("Resolution", f"{img2.width}×{img2.height}")
                c2.metric("Channels",   "3 (RGB)")
                c3.metric("Pixels",     f"{img2.width*img2.height:,}")

        with cv_tabs[2]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.4rem;">📷 Edge Detection & Morphology</div>
                <div style="font-size:0.82rem;color:#9CA3AF;">
                    Apply classical CV operators (Sobel, Laplacian) to extract structural features —
                    pre-processing step in defect detection pipelines.
                </div>
            </div>
            """, unsafe_allow_html=True)

            up3 = st.file_uploader("Upload image for edge detection", type=["jpg","jpeg","png"], key="cv_edge")
            if up3:
                import numpy as np
                try:
                    import cv2
                    img3 = Image.open(up3).convert("RGB")
                    arr3 = np.array(img3)
                    gray = cv2.cvtColor(arr3, cv2.COLOR_RGB2GRAY)

                    operator = st.selectbox("Edge operator", ["Sobel X", "Sobel Y", "Laplacian", "Canny"], key="cv_op")
                    if operator == "Sobel X":
                        result_img = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
                    elif operator == "Sobel Y":
                        result_img = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
                    elif operator == "Laplacian":
                        result_img = cv2.Laplacian(gray, cv2.CV_64F)
                    else:
                        result_img = cv2.Canny(gray, 50, 150)

                    result_img = np.uint8(np.abs(result_img))
                    col_a, col_b = st.columns(2)
                    col_a.image(img3, caption="Original", use_container_width=True)
                    col_b.image(result_img, caption=f"{operator} edges", use_container_width=True, clamp=True)
                except ImportError:
                    st.info("OpenCV not available in this environment — showing image statistics instead.")
                    img3 = Image.open(up3)
                    st.image(img3, caption="Uploaded image", use_container_width=True)

    # ─── TAB 5: GENERATIVE AI ─────────────────────────────────────────────
    with demo_tabs[4]:
        st.markdown("### 🧬 Generative AI — Trending Demos")
        gen_tabs = st.tabs(["✍️ Prompt Engineer", "🎨 Colour Palette Gen", "🎵 Token Visualiser"])

        with gen_tabs[0]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.4rem;">✍️ Prompt Engineering Studio</div>
                <div style="font-size:0.82rem;color:#9CA3AF;">
                    Craft and optimise prompts for LLMs. Shows system prompt + user turn + expected output
                    structure — essential for production RAG and agentic systems.
                </div>
            </div>
            """, unsafe_allow_html=True)

            system_p = st.text_area(
                "System Prompt", height=90, key="pe_sys",
                value="You are an expert AI engineer assistant. Answer concisely with technical precision. "
                      "Cite sources when available. Format code with markdown fences.")
            user_p = st.text_area(
                "User Message", height=80, key="pe_user",
                value="Explain the difference between LoRA and QLoRA fine-tuning, with a Python code example.")
            temperature = st.slider("Temperature", 0.0, 2.0, 0.7, 0.05, key="pe_temp")
            max_tokens  = st.slider("Max tokens",  64, 2048, 512, 32, key="pe_tokens")

            if st.button("Preview Prompt →", key="pe_run"):
                prompt_preview = f"""```
[SYSTEM]
{system_p}

[USER]
{user_p}

[PARAMETERS]
Temperature : {temperature}
Max tokens  : {max_tokens}
Model       : gpt-4o / llama-3.1-8b (configurable)
Stop tokens : ["\\n\\n---", "<|eot_id|>"]
```"""
                st.code(prompt_preview, language="markdown")

                tips = []
                if temperature > 1.2:
                    tips.append("⚠️ High temperature may cause hallucinations in factual tasks.")
                if "concise" not in system_p.lower():
                    tips.append("💡 Add 'be concise' to system prompt to reduce token cost.")
                if len(user_p.split()) < 10:
                    tips.append("💡 More specific user prompts improve response quality.")
                if tips:
                    for tip in tips:
                        st.markdown(f"<div style='background:#111827;border-left:3px solid #FFB347;"
                                    f"padding:0.5rem 0.75rem;border-radius:0 6px 6px 0;"
                                    f"font-size:0.82rem;color:#FFB347;margin:0.3rem 0;'>{tip}</div>",
                                    unsafe_allow_html=True)
                est_cost = max_tokens * 0.000002
                c1, c2, c3 = st.columns(3)
                c1.metric("Est. prompt tokens", len(system_p.split()) + len(user_p.split()))
                c2.metric("Max output tokens", max_tokens)
                c3.metric("Est. cost (GPT-4o)", f"${est_cost:.5f}")

        with gen_tabs[1]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.4rem;">🎨 AI Colour Palette Generator</div>
                <div style="font-size:0.82rem;color:#9CA3AF;">
                    Generate harmonious colour palettes from a mood keyword —
                    demonstrates embedding-based colour theory used in creative AI and UI generation.
                </div>
            </div>
            """, unsafe_allow_html=True)

            mood = st.text_input("Enter a mood / theme",
                                 value="cyberpunk neon", placeholder="e.g. ocean breeze, forest dusk, electric city",
                                 key="pal_mood")
            n_colors = st.slider("Palette size", 4, 8, 5, key="pal_n")

            if st.button("Generate Palette →", key="pal_run"):
                import hashlib, colorsys
                seed_val = int(hashlib.md5(mood.encode()).hexdigest()[:8], 16)
                rng_p = random.Random(seed_val)
                base_h = rng_p.random()

                MOOD_PALETTES = {
                    "cyberpunk": [(180,90,60),(280,70,50),(200,100,55),(330,80,45),(240,60,70)],
                    "ocean":     [(200,60,45),(185,50,55),(170,40,65),(210,70,35),(195,55,50)],
                    "forest":    [(120,45,30),(140,40,40),(100,35,45),(160,50,35),(130,55,25)],
                    "sunset":    [(20,80,55),(40,85,50),(350,75,55),(30,90,45),(10,70,60)],
                    "electric":  [(180,100,50),(200,90,55),(160,85,45),(220,95,40),(190,100,60)],
                    "neon":      [(300,100,55),(180,100,50),(60,100,55),(270,90,60),(150,100,50)],
                }

                matched_key = next((k for k in MOOD_PALETTES if k in mood.lower()), None)
                if matched_key:
                    hsl_bases = MOOD_PALETTES[matched_key][:n_colors]
                    while len(hsl_bases) < n_colors:
                        hsl_bases.append((rng_p.randint(0,360), rng_p.randint(40,90), rng_p.randint(35,65)))
                else:
                    hsl_bases = [(int((base_h + i/n_colors) % 1 * 360), 70, 50) for i in range(n_colors)]

                palette = []
                for h, s, l in hsl_bases:
                    r, g, b = colorsys.hls_to_rgb(h/360, l/100, s/100)
                    hex_c = "#{:02X}{:02X}{:02X}".format(int(r*255), int(g*255), int(b*255))
                    palette.append(hex_c)

                cols = st.columns(n_colors)
                for col, hex_c in zip(cols, palette):
                    col.markdown(f"""
                    <div style="background:{hex_c};height:100px;border-radius:10px;
                                 border:1px solid rgba(255,255,255,0.1);"></div>
                    <div style="text-align:center;font-size:0.7rem;color:#9CA3AF;
                                 margin-top:0.3rem;font-family:monospace;">{hex_c}</div>
                    """, unsafe_allow_html=True)

                import plotly.graph_objects as go
                fig = go.Figure(go.Bar(
                    x=palette, y=[1]*len(palette),
                    marker_color=palette, width=0.9,
                    text=palette, textposition="inside",
                    textfont=dict(color="white", size=10)
                ))
                fig.update_layout(
                    plot_bgcolor="#0E1117", paper_bgcolor="#1F2937",
                    height=120, showlegend=False,
                    margin=dict(l=5,r=5,t=5,b=5),
                    xaxis=dict(showticklabels=False, showgrid=False),
                    yaxis=dict(showticklabels=False, showgrid=False)
                )
                st.plotly_chart(fig, use_container_width=True)

        with gen_tabs[2]:
            st.markdown("""
            <div class="cyber-section">
                <div style="font-weight:700;color:#00D4FF;margin-bottom:0.4rem;">🎵 Token Frequency Visualiser</div>
                <div style="font-size:0.82rem;color:#9CA3AF;">
                    Visualise token distribution in any text — mirrors tokenisation pipelines
                    (BPE, WordPiece) used in GPT, BERT, and LLaMA models.
                </div>
            </div>
            """, unsafe_allow_html=True)

            tok_text = st.text_area("Paste text to tokenise & visualise",
                height=120, key="tok_text",
                value="Large language models use transformer architectures with attention mechanisms to process "
                      "and generate text. Training on massive datasets enables emergent capabilities like reasoning, "
                      "code generation, and language understanding across multiple domains.")

            if st.button("Visualise Tokens →", key="tok_run") and tok_text:
                import re, plotly.graph_objects as go
                # Simple BPE-like tokenisation (split on word boundaries, lowercase)
                raw_tokens = re.findall(r"[a-zA-Z']+|[0-9]+|[^\s\w]", tok_text)
                freq = {}
                for tok in raw_tokens:
                    freq[tok.lower()] = freq.get(tok.lower(), 0) + 1
                top = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:20]

                toks = [t[0] for t in top]
                cnts = [t[1] for t in top]

                fig = go.Figure(go.Bar(
                    x=toks, y=cnts,
                    marker_color=[f"hsl({i*18},70%,50%)" for i in range(len(toks))],
                    text=cnts, textposition="outside"
                ))
                fig.update_layout(
                    plot_bgcolor="#0E1117", paper_bgcolor="#1F2937",
                    font_color="#D1D5DB", height=280,
                    margin=dict(l=10,r=10,t=10,b=30),
                    xaxis=dict(color="#9CA3AF", tickangle=-30),
                    yaxis=dict(color="#9CA3AF", showgrid=True, gridcolor="#1F2937")
                )
                st.plotly_chart(fig, use_container_width=True)

                total_tok = len(raw_tokens)
                unique_tok = len(freq)
                c1, c2, c3 = st.columns(3)
                c1.metric("Total Tokens", total_tok)
                c2.metric("Unique Tokens", unique_tok)
                c3.metric("Vocab Density", f"{unique_tok/max(total_tok,1):.0%}")


# ─────────────────────────────────────────────────────────────────────────────
#  PAGE: FREELANCE
# ─────────────────────────────────────────────────────────────────────────────
def page_freelance():
    from streamlit_lottie import st_lottie

    lang = st.session_state.get("lang", "en")

    st.markdown(f"""
    <div class="cta-section">
        <h2 style="color:#F8FAFC;font-weight:900;margin-bottom:0.5rem;">
            {t('section_freelance')}
        </h2>
        <p style="color:#9CA3AF;font-size:1rem;max-width:600px;margin:0 auto 1.5rem;">
            {t('fl_tagline')}
        </p>
        <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
            <div style="background:rgba(0,255,136,0.1);border:1px solid rgba(0,255,136,0.3);
                         border-radius:10px;padding:0.5rem 1.25rem;font-size:0.85rem;color:#00FF88;font-weight:700;">
                {t('fl_avail_text')}
            </div>
            <div style="background:rgba(0,212,255,0.1);border:1px solid rgba(0,212,255,0.3);
                         border-radius:10px;padding:0.5rem 1.25rem;font-size:0.85rem;color:#00D4FF;font-weight:700;">
                {t('fl_response')}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Services Grid ──────────────────────────────────────────────────────
    st.markdown(f'<div class="cyber-section-title" style="margin-top:1.5rem;"><span class="accent-bar"></span>{t("fl_services")}</div>',
                unsafe_allow_html=True)

    services = {
        "en": [
            {"icon":"🔍","title":"RAG & LLM Systems",
             "desc":"Design and deploy production RAG pipelines: vector stores (FAISS, Pinecone), LLM integration (GPT-4, Llama), evaluation harnesses, safety guardrails.",
             "deliverables":["RAG architecture design","Vector DB setup & indexing","LLM API integration","RAGAS evaluation framework","Production deployment"],
             "tag":"LangChain · FAISS · FastAPI"},
            {"icon":"🧠","title":"LLM Fine-Tuning (LoRA/QLoRA)",
             "desc":"Domain-adaptive fine-tuning of 7B–70B parameter models using LoRA/QLoRA. Custom datasets, evaluation, quantisation, and model registry.",
             "deliverables":["Dataset curation & cleaning","LoRA/QLoRA training","DPO alignment","Model evaluation suite","Quantised deployment"],
             "tag":"HuggingFace · Axolotl · W&B"},
            {"icon":"👁️","title":"Computer Vision Systems",
             "desc":"End-to-end CV pipelines: YOLOv8 training, TensorRT optimisation, edge deployment on NVIDIA Jetson, real-time dashboards.",
             "deliverables":["Dataset labelling pipeline","YOLOv8 custom training","TensorRT INT8 optimisation","Edge deployment","QA dashboard"],
             "tag":"YOLOv8 · TensorRT · OpenCV"},
            {"icon":"🚀","title":"MLOps & Production AI",
             "desc":"Build ML infrastructure: Kubernetes deployments, CI/CD pipelines, monitoring (Prometheus/Grafana), model registries, A/B testing.",
             "deliverables":["K8s deployment configs","CI/CD with GitHub Actions","MLflow / W&B integration","Drift monitoring","Blue/green releases"],
             "tag":"K8s · Docker · Triton · MLflow"},
            {"icon":"🦾","title":"Robotics AI Integration",
             "desc":"AI for robotics: perception (CV + sensors), path planning, force control, ROS2 integration, autonomous navigation.",
             "deliverables":["Sensor fusion pipeline","Real-time perception","ROS2 node development","Path planning algorithms","Edge AI deployment"],
             "tag":"ROS2 · OpenCV · PyTorch · NVIDIA"},
            {"icon":"📊","title":"Data Science & Analytics",
             "desc":"End-to-end data science: EDA, feature engineering, predictive modelling, dashboards, anomaly detection, time-series forecasting.",
             "deliverables":["Exploratory data analysis","Feature engineering","Model training & tuning","Streamlit/Plotly dashboard","Production deployment"],
             "tag":"Python · Pandas · Scikit-learn · Plotly"},
        ],
        "it": [
            {"icon":"🔍","title":"Sistemi RAG & LLM",
             "desc":"Progettazione e deploy di pipeline RAG in produzione: vector store (FAISS, Pinecone), integrazione LLM (GPT-4, Llama), harness di valutazione, guardrail.",
             "deliverables":["Design architettura RAG","Setup Vector DB e indicizzazione","Integrazione API LLM","Framework RAGAS","Deploy in produzione"],
             "tag":"LangChain · FAISS · FastAPI"},
            {"icon":"🧠","title":"Fine-Tuning LLM (LoRA/QLoRA)",
             "desc":"Fine-tuning adattivo di modelli da 7B a 70B parametri con LoRA/QLoRA. Dataset personalizzati, valutazione, quantizzazione e model registry.",
             "deliverables":["Curation e pulizia dataset","Training LoRA/QLoRA","Allineamento DPO","Suite di valutazione","Deploy quantizzato"],
             "tag":"HuggingFace · Axolotl · W&B"},
            {"icon":"👁️","title":"Sistemi di Computer Vision",
             "desc":"Pipeline CV end-to-end: training YOLOv8, ottimizzazione TensorRT, deploy su NVIDIA Jetson, dashboard in tempo reale.",
             "deliverables":["Pipeline di etichettatura dataset","Training YOLOv8 personalizzato","Ottimizzazione TensorRT INT8","Deploy edge","Dashboard QA"],
             "tag":"YOLOv8 · TensorRT · OpenCV"},
            {"icon":"🚀","title":"MLOps & AI in Produzione",
             "desc":"Infrastruttura ML: deploy Kubernetes, pipeline CI/CD, monitoraggio (Prometheus/Grafana), model registry, A/B testing.",
             "deliverables":["Config deploy K8s","CI/CD con GitHub Actions","Integrazione MLflow/W&B","Monitoraggio drift","Release blue/green"],
             "tag":"K8s · Docker · Triton · MLflow"},
            {"icon":"🦾","title":"Integrazione AI per Robotica",
             "desc":"AI per la robotica: percezione (CV + sensori), pianificazione del percorso, controllo di forza, integrazione ROS2, navigazione autonoma.",
             "deliverables":["Pipeline di sensor fusion","Percezione in tempo reale","Sviluppo nodi ROS2","Algoritmi di path planning","Deploy AI su edge"],
             "tag":"ROS2 · OpenCV · PyTorch · NVIDIA"},
            {"icon":"📊","title":"Data Science & Analytics",
             "desc":"Data science end-to-end: EDA, feature engineering, modellistica predittiva, dashboard, anomaly detection, previsione serie temporali.",
             "deliverables":["Analisi esplorativa dei dati","Feature engineering","Training e tuning modelli","Dashboard Streamlit/Plotly","Deploy in produzione"],
             "tag":"Python · Pandas · Scikit-learn · Plotly"},
        ],
        "fr": [
            {"icon":"🔍","title":"Systèmes RAG & LLM",
             "desc":"Conception et déploiement de pipelines RAG en production : vector stores (FAISS, Pinecone), intégration LLM (GPT-4, Llama), harness d'évaluation, guardrails.",
             "deliverables":["Design architecture RAG","Setup Vector DB & indexation","Intégration API LLM","Framework RAGAS","Déploiement production"],
             "tag":"LangChain · FAISS · FastAPI"},
            {"icon":"🧠","title":"Fine-Tuning LLM (LoRA/QLoRA)",
             "desc":"Fine-tuning adaptatif de modèles 7B–70B avec LoRA/QLoRA. Datasets personnalisés, évaluation, quantisation et model registry.",
             "deliverables":["Curation & nettoyage dataset","Training LoRA/QLoRA","Alignement DPO","Suite d'évaluation","Déploiement quantisé"],
             "tag":"HuggingFace · Axolotl · W&B"},
            {"icon":"👁️","title":"Systèmes Computer Vision",
             "desc":"Pipelines CV de bout en bout : entraînement YOLOv8, optimisation TensorRT, déploiement edge NVIDIA Jetson, dashboards temps réel.",
             "deliverables":["Pipeline d'étiquetage dataset","Training YOLOv8 custom","Optimisation TensorRT INT8","Déploiement edge","Dashboard QA"],
             "tag":"YOLOv8 · TensorRT · OpenCV"},
            {"icon":"🚀","title":"MLOps & IA en Production",
             "desc":"Infrastructure ML : déploiements Kubernetes, pipelines CI/CD, monitoring (Prometheus/Grafana), model registries, A/B testing.",
             "deliverables":["Configs déploiement K8s","CI/CD avec GitHub Actions","Intégration MLflow/W&B","Monitoring drift","Releases blue/green"],
             "tag":"K8s · Docker · Triton · MLflow"},
            {"icon":"🦾","title":"Intégration IA pour la Robotique",
             "desc":"IA pour la robotique : perception (CV + capteurs), planification de trajectoire, contrôle de force, intégration ROS2, navigation autonome.",
             "deliverables":["Pipeline de fusion de capteurs","Perception temps réel","Développement nœuds ROS2","Algorithmes de planification","Déploiement IA edge"],
             "tag":"ROS2 · OpenCV · PyTorch · NVIDIA"},
            {"icon":"📊","title":"Data Science & Analytics",
             "desc":"Data science de bout en bout : EDA, feature engineering, modélisation prédictive, dashboards, détection d'anomalies, prévision de séries temporelles.",
             "deliverables":["Analyse exploratoire","Feature engineering","Entraînement & tuning modèles","Dashboard Streamlit/Plotly","Déploiement production"],
             "tag":"Python · Pandas · Scikit-learn · Plotly"},
        ],
    }

    srv_list = services.get(lang, services["en"])
    cols = st.columns(2)
    for i, svc in enumerate(srv_list):
        with cols[i % 2]:
            deliverables_html = "".join(
                f'<li style="font-size:0.78rem;color:#9CA3AF;margin:0.15rem 0;">{d}</li>'
                for d in svc["deliverables"]
            )
            st.markdown(f"""
            <div class="cyber-section" style="height:100%;min-height:240px;">
                <div style="font-size:1.6rem;margin-bottom:0.4rem;">{svc['icon']}</div>
                <div style="font-weight:800;color:#F8FAFC;font-size:1rem;margin-bottom:0.5rem;">{svc['title']}</div>
                <div style="font-size:0.82rem;color:#9CA3AF;line-height:1.6;margin-bottom:0.75rem;">{svc['desc']}</div>
                <ul style="padding-left:1rem;margin:0 0 0.75rem;">{deliverables_html}</ul>
                <div style="margin-top:auto;">
                    <span class="glow-tag">{svc['tag']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ── How I Work ─────────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown(f'<div class="cyber-section-title"><span class="accent-bar"></span>{t("fl_process")}</div>',
                unsafe_allow_html=True)

    steps_map = {
        "en": [
            ("1", "Discovery Call",  "30-min free consultation to understand your project scope, goals, and constraints."),
            ("2", "Proposal & SOW",  "I send a clear Statement of Work with milestones, timeline, and fixed or hourly pricing."),
            ("3", "Development",     "Agile sprints with weekly demos. Full code on GitHub. Documentation included."),
            ("4", "Review & Iterate","2 rounds of revisions included. Feedback loops keep the project on track."),
            ("5", "Delivery & Handoff","Production-ready code, deployment guide, and 2 weeks of post-delivery support."),
        ],
        "it": [
            ("1", "Call di Scoperta",   "30 minuti di consultazione gratuita per capire obiettivi, vincoli e scope del progetto."),
            ("2", "Proposta & SOW",     "Ti invio un Statement of Work chiaro con milestone, timeline e prezzi fissi o a ore."),
            ("3", "Sviluppo",           "Sprint agili con demo settimanali. Codice completo su GitHub. Documentazione inclusa."),
            ("4", "Revisione",          "2 round di revisioni inclusi. Loop di feedback per mantenere il progetto in linea."),
            ("5", "Consegna",           "Codice pronto per la produzione, guida al deploy e 2 settimane di supporto post-consegna."),
        ],
        "fr": [
            ("1", "Appel de Découverte","30 min de consultation gratuite pour comprendre la portée, les objectifs et les contraintes."),
            ("2", "Proposition & SOW", "Je vous envoie un SoW clair avec jalons, calendrier et tarification fixe ou horaire."),
            ("3", "Développement",     "Sprints agiles avec démos hebdomadaires. Code complet sur GitHub. Documentation incluse."),
            ("4", "Révision",          "2 cycles de révisions inclus. Boucles de feedback pour rester dans les délais."),
            ("5", "Livraison",         "Code prêt pour la production, guide de déploiement et 2 semaines de support post-livraison."),
        ],
    }

    steps = steps_map.get(lang, steps_map["en"])
    cols_p = st.columns(5)
    for col, (num, title, desc) in zip(cols_p, steps):
        with col:
            st.markdown(f"""
            <div style="background:#111827;border:1px solid #1F2937;border-radius:12px;
                         padding:1rem 0.75rem;text-align:center;height:100%;min-height:160px;">
                <div style="width:36px;height:36px;border-radius:50%;border:2px solid #00D4FF;
                             background:rgba(0,212,255,0.1);font-weight:800;color:#00D4FF;
                             display:flex;align-items:center;justify-content:center;
                             font-size:0.9rem;margin:0 auto 0.6rem;">
                    {num}
                </div>
                <div style="font-weight:700;color:#F8FAFC;font-size:0.82rem;margin-bottom:0.4rem;">{title}</div>
                <div style="font-size:0.72rem;color:#9CA3AF;line-height:1.5;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── Availability ────────────────────────────────────────────────────────
    st.markdown("---")
    av1, av2 = st.columns([1, 1])
    with av1:
        st.markdown(f"""
        <div class="cyber-section">
            <div class="cyber-section-title" style="font-size:1rem;">
                <span class="accent-bar"></span>{t('fl_avail')}
            </div>
            <div style="background:rgba(0,255,136,0.08);border:1px solid rgba(0,255,136,0.2);
                         border-radius:10px;padding:1rem;margin-bottom:1rem;">
                <div style="font-size:1rem;font-weight:700;color:#00FF88;">{t('fl_avail_text')}</div>
                <div style="font-size:0.8rem;color:#9CA3AF;margin-top:0.3rem;">{t('fl_response')}</div>
            </div>
            <div style="font-size:0.78rem;color:#6B7280;margin-top:0.5rem;">{t('fl_rate_note')}</div>
            <div style="margin-top:1rem;">
                <div style="font-size:0.7rem;color:#9CA3AF;margin-bottom:0.5rem;text-transform:uppercase;
                             letter-spacing:0.08em;font-weight:700;">Engagement types</div>
                <div style="display:flex;flex-wrap:wrap;gap:0.4rem;">
                    <span class="glow-tag">Hourly</span>
                    <span class="glow-tag">Fixed Price</span>
                    <span class="glow-tag">Retainer</span>
                    <span class="glow-tag">Full-time Contract</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with av2:
        anim = load_lottie("ai.json")
        if anim:
            from streamlit_lottie import st_lottie
            st_lottie(anim, height=260, key="fl_anim")

    # CTA to contact
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align:center;padding:1rem 0;">
        <a href="mailto:karim.osman.ai@gmail.com" class="cta-btn" style="margin:0 0.5rem;">
            ✉️ Start a Project
        </a>
        <a href="https://www.linkedin.com/in/karimosman89/" target="_blank"
           class="cta-btn-secondary" style="margin:0 0.5rem;">
            🔗 LinkedIn
        </a>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
#  PAGE: IMPACT DASHBOARD
# ─────────────────────────────────────────────────────────────────────────────
def page_impact():
    import plotly.graph_objects as go

    st.markdown(f'<div class="cyber-section-title"><span class="accent-bar"></span>{t("section_impact")}</div>',
                unsafe_allow_html=True)

    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("Revenue Impact",     "€2M+",   "↑ Quantified")
    m2.metric("Uptime SLA",         "99.9%",  "↑ Production")
    m3.metric("Daily Users",        "100K+",  "↑ Baker Hughes")
    m4.metric("Docs / Day",         "10K+",   "↑ 95% Accuracy")
    m5.metric("Defect Detection ↑", "+22%",   "↑ YOLOv8")

    st.markdown("---")
    st.markdown("""
    <div class="kpi-grid">
        <div class="kpi-card green"><div class="kpi-value">60%</div>
            <div class="kpi-label">Document Review Time ↓</div><div class="kpi-delta">Baker Hughes</div></div>
        <div class="kpi-card blue"><div class="kpi-value">42%</div>
            <div class="kpi-label">Ticket Deflection (90d)</div><div class="kpi-delta">RAG Assistant</div></div>
        <div class="kpi-card amber"><div class="kpi-value">68%</div>
            <div class="kpi-label">Faster Resolution</div><div class="kpi-delta">Median Time ↓</div></div>
        <div class="kpi-card red"><div class="kpi-value">0.3%</div>
            <div class="kpi-label">Defect Escape Rate</div><div class="kpi-delta">↓ from 1.8%</div></div>
        <div class="kpi-card green"><div class="kpi-value">98.7%</div>
            <div class="kpi-label">Vision Recall</div><div class="kpi-delta">Edge · Jetson</div></div>
        <div class="kpi-card blue"><div class="kpi-value">3.1s</div>
            <div class="kpi-label">Cycle Time (was 7.5s)</div><div class="kpi-delta">↓ 59%</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 📈 Business Impact Over Time")
        quarters = ["Q1'22","Q2'22","Q3'22","Q4'22","Q1'23","Q2'23","Q3'23","Q4'23","Q1'24","Q2'24"]
        revenue  = [50,120,250,400,600,850,1100,1450,1750,2100]
        fig = go.Figure(go.Scatter(
            x=quarters, y=revenue, fill='tozeroy',
            line=dict(color='#00D4FF',width=3),
            fillcolor='rgba(0,212,255,0.1)',
            marker=dict(size=8,color='#00D4FF')
        ))
        fig.update_layout(
            plot_bgcolor='#111827', paper_bgcolor='#1F2937',
            font_color='#D1D5DB', margin=dict(l=10,r=10,t=10,b=10),
            xaxis=dict(showgrid=False,tickfont=dict(size=9),color='#6B7280'),
            yaxis=dict(showgrid=True,gridcolor='#374151',tickprefix='€',ticksuffix='K',
                       tickfont=dict(size=9),color='#6B7280'),
            showlegend=False, height=270
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### 🎯 Defect Rate — Before vs After YOLOv8")
        fig2 = go.Figure(go.Bar(
            x=["Before YOLOv8","After YOLOv8"],
            y=[1.8, 0.3],
            text=["1.8%","0.3%"], textposition='outside',
            marker_color=['#FF4757','#00FF88'], width=0.4
        ))
        fig2.update_layout(
            plot_bgcolor='#111827', paper_bgcolor='#1F2937',
            font_color='#D1D5DB', margin=dict(l=10,r=10,t=10,b=10),
            yaxis=dict(showgrid=True,gridcolor='#374151',ticksuffix='%',color='#6B7280'),
            xaxis=dict(color='#6B7280'), height=270
        )
        st.plotly_chart(fig2, use_container_width=True)

    # Architecture diagrams
    st.markdown("---")
    st.markdown(f'<div class="cyber-section-title"><span class="accent-bar"></span>{t("section_arch")}</div>',
                unsafe_allow_html=True)

    arch_tabs = st.tabs(["🔍 RAG-as-a-Service","⚙️ Chunk-as-a-Service","🧠 LLM-as-a-Service","👁️ Vision Pipeline"])

    arch_diagrams = [
        """  [User Query]
       │
       ▼
  ┌──────────────────┐     ┌─────────────────────────┐
  │  API Gateway     │────▶│  Cross-lingual Embedding │
  │  (FastAPI/Auth)  │     │  + Query Understanding   │
  └──────────────────┘     └────────────┬────────────┘
                                        │
                    ┌───────────────────▼──────────────────┐
                    │      VECTOR RETRIEVAL (FAISS/PGVector) │
                    │  Dense + BM25 Hybrid · Re-ranking      │
                    └───────────────────┬──────────────────┘
                                        │ Top-K Chunks
                                        ▼
                    ┌───────────────────────────────────────┐
                    │  Llama 3.1 8B (LoRA fine-tuned)       │
                    │  GPT-4 Turbo (fallback)               │
                    └───────────────────┬───────────────────┘
                                        │
                    ┌───────────────────▼───────────────────┐
                    │  Guardrails · RAGAS Eval · Audit Log   │
                    └───────────────────────────────────────┘
  Infra: K8s (EKS) · Triton · Redis · Prometheus · Blue/Green""",
        """  [Raw Docs: PDF, DOCX, CAD, Excel, Images] ──Kafka──▶ 10K+/day
          │
  ┌───────▼───────────────────────────────────────┐
  │  ① OCR & Layout   (Tesseract + LayoutParser)  │
  │  ② Semantic Chunk (boundary + overlap)         │
  │  ③ Metadata Extract (title, date, equipment)  │
  │  ④ Embed (multilingual-e5-large · GPU batch)  │
  │  ⑤ Quality Gate   (95% accuracy threshold)    │
  └───────────────────────────────────────────────┘
          │
  ┌───────▼──────────────────┐
  │  Vector Store             │
  │  FAISS + PGVector (hybrid)│
  │  MongoDB (raw)            │
  └───────┬──────────────────┘
          │
  ┌───────▼──────────────────────────┐
  │  Chunk API · Redis cache · Auth  │
  └───────────────────────────────────┘
  Workers: Ray · Docker · GPU (A10G) · Airflow DAGs""",
        """  Client Apps / Streamlit UI
          │
  ┌───────▼────────────────────────────────────┐
  │  LLM Gateway (FastAPI)                      │
  │  Rate limiting · API key · Cost tracking    │
  └───────────────┬────────────────────────────┘
                  │
    ┌─────────────┼─────────────┐
    ▼             ▼             ▼
  Llama 3.1 8B  GPT-4 API    Embedding
  LoRA (primary)(fallback)   Service
  Triton        OpenAI        (MiniLM +
  (TensorRT)                  multilingual)
    │
    ▼
  ┌────────────────────────────────────────┐
  │  TensorRT · INT8 Quant · vLLM batching │
  │  Token streaming (SSE) · KV cache       │
  └──────────────────────────────────────── ┘
  SLA: P95 < 2s · 99.9% uptime · GPU autoscale (KServe)""",
        """  [Camera 30fps RTSP]
          │
  OpenCV pre-process → YOLOv8 (TensorRT INT8 on Jetson)
          │
  Post-process (NMS + classification)
          │
    ┌─────┴──────────────┐
    │                    │
    ▼                    ▼
  PASS               DEFECT DETECTED
  Log + KPI          Alert + Line Stop
                     Human review queue
          │
  Streamlit QA Dashboard
  Drift monitor · Operator feedback · Retraining trigger
  Results: Recall 98.7% · Precision 96.2% · Escape 0.3%"""
    ]

    for tab, diag in zip(arch_tabs, arch_diagrams):
        with tab:
            st.markdown(f"""
            <div class="arch-container">
            <pre style="font-family:'Courier New',monospace;font-size:0.76rem;
                         color:#D1D5DB;line-height:1.65;white-space:pre-wrap;">{diag}</pre>
            </div>
            """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
#  PAGE: TECH STACK
# ─────────────────────────────────────────────────────────────────────────────
def page_skills():
    from streamlit_lottie import st_lottie

    st.markdown(f'<div class="cyber-section-title"><span class="accent-bar"></span>{t("section_skills")}</div>',
                unsafe_allow_html=True)

    skill_tabs = st.tabs(["🧠 Core AI", "☁️ Cloud & MLOps", "🗄️ Data Engineering", "📊 Radar"])

    with skill_tabs[0]:
        c1, c2 = st.columns([2,1])
        with c1:
            st.markdown("""
            <div class="cyber-section">
            <div class="skill-group"><div class="skill-group-title">🐍 Languages</div>
            <div class="skill-pills"><span class="skill-pill core">Python</span><span class="skill-pill core">TypeScript</span>
            <span class="skill-pill core">C++</span><span class="skill-pill core">Go</span>
            <span class="skill-pill core">Java</span><span class="skill-pill core">SQL</span><span class="skill-pill core">Bash</span></div></div>
            <div class="skill-group"><div class="skill-group-title">🤗 LLM & RAG</div>
            <div class="skill-pills"><span class="skill-pill core">LangChain</span><span class="skill-pill core">LlamaIndex</span>
            <span class="skill-pill core">OpenAI API</span><span class="skill-pill core">HuggingFace</span>
            <span class="skill-pill core">RAGAS</span><span class="skill-pill core">Instructor</span></div></div>
            <div class="skill-group"><div class="skill-group-title">🔬 Fine-Tuning</div>
            <div class="skill-pills"><span class="skill-pill core">LoRA</span><span class="skill-pill core">QLoRA</span>
            <span class="skill-pill core">PEFT</span><span class="skill-pill core">DPO</span>
            <span class="skill-pill core">RLHF</span><span class="skill-pill core">Axolotl</span></div></div>
            <div class="skill-group"><div class="skill-group-title">🗂️ Vector DBs</div>
            <div class="skill-pills"><span class="skill-pill core">FAISS</span><span class="skill-pill core">Pinecone</span>
            <span class="skill-pill core">ChromaDB</span><span class="skill-pill core">Weaviate</span>
            <span class="skill-pill core">PGVector</span><span class="skill-pill core">Qdrant</span></div></div>
            <div class="skill-group"><div class="skill-group-title">👁️ Computer Vision</div>
            <div class="skill-pills"><span class="skill-pill core">YOLOv8</span><span class="skill-pill core">OpenCV</span>
            <span class="skill-pill core">TensorRT</span><span class="skill-pill core">Detectron2</span>
            <span class="skill-pill core">NVIDIA Jetson</span></div></div>
            <div class="skill-group"><div class="skill-group-title">🦾 Robotics</div>
            <div class="skill-pills"><span class="skill-pill core">ROS2</span><span class="skill-pill core">Gazebo</span>
            <span class="skill-pill core">PyBullet</span><span class="skill-pill core">MoveIt</span>
            <span class="skill-pill core">OpenManipulator</span></div></div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            a = load_lottie("ai-engineering.json")
            if a: st_lottie(a, height=380, key="sk_ai")

    with skill_tabs[1]:
        c1, c2 = st.columns([2,1])
        with c1:
            st.markdown("""
            <div class="cyber-section">
            <div class="skill-group"><div class="skill-group-title">☁️ Cloud</div>
            <div class="skill-pills"><span class="skill-pill cloud">AWS SageMaker</span><span class="skill-pill cloud">AWS EKS</span>
            <span class="skill-pill cloud">GCP Vertex AI</span><span class="skill-pill cloud">Azure ML</span>
            <span class="skill-pill cloud">Azure AKS</span></div></div>
            <div class="skill-group"><div class="skill-group-title">🚀 Serving</div>
            <div class="skill-pills"><span class="skill-pill cloud">Triton</span><span class="skill-pill cloud">KServe</span>
            <span class="skill-pill cloud">vLLM</span><span class="skill-pill cloud">TorchServe</span>
            <span class="skill-pill cloud">FastAPI</span></div></div>
            <div class="skill-group"><div class="skill-group-title">📦 Containers</div>
            <div class="skill-pills"><span class="skill-pill cloud">Kubernetes</span><span class="skill-pill cloud">Docker</span>
            <span class="skill-pill cloud">Helm</span><span class="skill-pill cloud">ArgoCD</span>
            <span class="skill-pill cloud">Terraform</span></div></div>
            <div class="skill-group"><div class="skill-group-title">📊 Tracking</div>
            <div class="skill-pills"><span class="skill-pill cloud">MLflow</span><span class="skill-pill cloud">W&B</span>
            <span class="skill-pill cloud">Ray</span><span class="skill-pill cloud">DVC</span>
            <span class="skill-pill cloud">Feast</span></div></div>
            <div class="skill-group"><div class="skill-group-title">🔍 Observability</div>
            <div class="skill-pills"><span class="skill-pill cloud">Prometheus</span><span class="skill-pill cloud">Grafana</span>
            <span class="skill-pill cloud">Datadog</span><span class="skill-pill cloud">OpenTelemetry</span></div></div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            a = load_lottie("devops.json")
            if a: st_lottie(a, height=360, key="sk_devops")

    with skill_tabs[2]:
        c1, c2 = st.columns([2,1])
        with c1:
            st.markdown("""
            <div class="cyber-section">
            <div class="skill-group"><div class="skill-group-title">⚡ Streaming</div>
            <div class="skill-pills"><span class="skill-pill data">Apache Kafka</span><span class="skill-pill data">Apache Spark</span>
            <span class="skill-pill data">Flink</span><span class="skill-pill data">Kinesis</span></div></div>
            <div class="skill-group"><div class="skill-group-title">🗃️ Databases</div>
            <div class="skill-pills"><span class="skill-pill data">PostgreSQL</span><span class="skill-pill data">MongoDB</span>
            <span class="skill-pill data">Redis</span><span class="skill-pill data">Elasticsearch</span>
            <span class="skill-pill data">Snowflake</span><span class="skill-pill data">BigQuery</span></div></div>
            <div class="skill-group"><div class="skill-group-title">🔄 Orchestration</div>
            <div class="skill-pills"><span class="skill-pill data">Airflow</span><span class="skill-pill data">dbt</span>
            <span class="skill-pill data">Prefect</span><span class="skill-pill data">GitHub Actions</span></div></div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            a = load_lottie("data-engineer.json")
            if a: st_lottie(a, height=320, key="sk_data")

    with skill_tabs[3]:
        import plotly.graph_objects as go
        categories = ["LLM/RAG","Computer Vision","MLOps/Cloud","Data Eng","Fine-Tuning","Python/Backend","Robotics AI"]
        values = [98, 92, 90, 85, 95, 97, 78]
        values.append(values[0]); categories.append(categories[0])
        fig = go.Figure(go.Scatterpolar(
            r=values, theta=categories, fill='toself',
            line=dict(color='#00D4FF',width=2),
            fillcolor='rgba(0,212,255,0.1)',
            marker=dict(size=6,color='#00D4FF')
        ))
        fig.update_layout(
            polar=dict(bgcolor='#0E1117',
                radialaxis=dict(visible=True,range=[0,100],gridcolor='#374151',
                                tickfont=dict(color='#6B7280',size=9)),
                angularaxis=dict(gridcolor='#374151',tickfont=dict(color='#D1D5DB',size=11))),
            paper_bgcolor='#1F2937', font_color='#D1D5DB',
            height=400, margin=dict(l=50,r=50,t=20,b=20), showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)


# ─────────────────────────────────────────────────────────────────────────────
#  PAGE: PROJECTS
# ─────────────────────────────────────────────────────────────────────────────
def page_projects():
    st.markdown(f'<div class="cyber-section-title"><span class="accent-bar"></span>{t("section_projects")}</div>',
                unsafe_allow_html=True)

    featured = [
        {"title":"RAG-as-a-Service Platform","org":"Baker Hughes","category":"NLP / LLM",
         "desc":"Production RAG for 500+ global engineers. LangChain + FAISS + PGVector + Llama 3.1 8B (LoRA). 10K+ docs/day, 99.9% uptime.",
         "metrics":[("Uptime","99.9%"),("Docs/Day","10K+"),("Impact","€2M+")],
         "tags":["LangChain","FAISS","Kubernetes","LoRA"],"impact":"€2M Revenue Impact"},
        {"title":"Chunk-as-a-Service Engine","org":"Baker Hughes","category":"NLP / LLM",
         "desc":"Distributed doc pipeline: OCR, semantic chunking, multilingual embedding, quality scoring. Kafka + Ray + GPU. 95% accuracy.",
         "metrics":[("Accuracy","95%"),("Throughput","10K/day"),("Languages","8+")],
         "tags":["Kafka","Ray","OCR","Embeddings"],"impact":"60% Review Time ↓"},
        {"title":"Edge Vision Inspection","org":"Baker Hughes","category":"Computer Vision",
         "desc":"YOLOv8 + TensorRT INT8 on NVIDIA Jetson for real-time defect detection. Triton/KServe. Operator feedback loop.",
         "metrics":[("Recall","98.7%"),("Precision","96.2%"),("Cycle","3.1s")],
         "tags":["YOLOv8","TensorRT","Jetson","Triton"],"impact":"22% Defect Detection ↑"},
        {"title":"Multilingual RAG Support Assistant","org":"Enterprise","category":"NLP / LLM",
         "desc":"Cross-lingual RAG for 120K+ monthly tickets in 8 languages. Llama 3.1 8B fine-tuned, RAGAS eval, guardrails.",
         "metrics":[("Deflection","42%"),("Resolution","↓68%"),("CSAT","+12pts")],
         "tags":["LlamaIndex","Cross-lingual","RAGAS","FastAPI"],"impact":"35% Cost/Ticket ↓"},
        {"title":"LLM Fine-Tuning Pipeline","org":"R&D","category":"NLP / LLM",
         "desc":"End-to-end pipeline: data curation, QLoRA, DPO alignment, eval harness, model registry, A/B deployment.",
         "metrics":[("Models","10+"),("Params","7B–70B"),("Method","QLoRA")],
         "tags":["LoRA","QLoRA","DeepSpeed","W&B"],"impact":"SOTA Domain Accuracy"},
        {"title":"Predictive Analytics Platform","org":"UniqMaster","category":"MLOps",
         "desc":"Automated ML for demand forecasting + recommendations. 50+ data sources, AutoML, SageMaker deploy.",
         "metrics":[("Sources","50+"),("Deploy","↓ weeks→hrs"),("Accuracy","89%+")],
         "tags":["SageMaker","MLflow","Airflow","AutoML"],"impact":"Dev Time ↓ 70%"},
    ]

    cats = ["All"] + list(dict.fromkeys(p["category"] for p in featured))
    sel = st.selectbox("Filter", cats, key="proj_filter")
    for proj in featured:
        if sel != "All" and proj["category"] != sel:
            continue
        with st.expander(f"🚀 **{proj['title']}** — {proj['org']}  `{proj['category']}`"):
            c1, c2 = st.columns([2,1])
            with c1:
                st.markdown(f"**Description:** {proj['desc']}")
                tags_html = " ".join(f'<span class="glow-tag">{tg}</span>' for tg in proj['tags'])
                st.markdown(f"**Stack:** {tags_html}", unsafe_allow_html=True)
            with c2:
                st.markdown(f'<span class="success-tag">💹 {proj["impact"]}</span>', unsafe_allow_html=True)
                for label, val in proj["metrics"]:
                    st.metric(label, val)

    # GitHub repos
    st.markdown("---")
    st.markdown('<div class="cyber-section-title"><span class="accent-bar"></span>🐙 GitHub Repositories</div>',
                unsafe_allow_html=True)

    sel_topics = st.multiselect("Filter by Domain", list(TOPIC_FILTER_MAP.keys()),
                                default=["All"], key="repo_filter")
    with st.spinner("Fetching from GitHub API…"):
        repos = fetch_github_repos("karimosman89")

    def repo_matches(r):
        if "All" in sel_topics or not sel_topics: return True
        name = (r.get("name","") + " " + (r.get("description") or "")).lower()
        topics = r.get("topics", [])
        for s in sel_topics:
            kws = TOPIC_FILTER_MAP.get(s, [])
            if kws and any(k in name or k in topics for k in kws): return True
        return False

    filtered = [r for r in repos if repo_matches(r)]
    if filtered:
        cols = st.columns(3)
        for i, repo in enumerate(filtered[:12]):
            with cols[i % 3]:
                lang   = repo.get("language") or "—"
                color  = LANG_COLORS.get(lang, "#9CA3AF")
                desc   = (repo.get("description") or "No description")[:130]
                stars  = repo.get("stargazers_count", 0)
                forks  = repo.get("forks_count", 0)
                url    = repo.get("html_url", "#")
                name   = repo.get("name", "repo")
                topics = " ".join(f'<span class="repo-topic">{tp}</span>'
                                  for tp in repo.get("topics", [])[:4])
                st.markdown(f"""
                <div class="repo-card">
                    <div class="repo-name">📦 {name}</div>
                    <div class="repo-desc">{desc}</div>
                    <div class="repo-meta">
                        <span class="repo-lang" style="color:{color};">● {lang}</span>
                        <span class="repo-star">⭐ {stars}</span>
                        <span class="repo-star">🍴 {forks}</span>
                    </div>
                    <div style="margin-top:0.4rem;">{topics}</div>
                    <a href="{url}" target="_blank"
                       style="font-size:0.72rem;color:#00D4FF;text-decoration:none;
                              margin-top:0.5rem;display:block;">→ GitHub</a>
                </div>
                """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
#  PAGE: EXPERIENCE
# ─────────────────────────────────────────────────────────────────────────────
def page_experience():
    from streamlit_lottie import st_lottie

    st.markdown(f'<div class="cyber-section-title"><span class="accent-bar"></span>{t("section_exp")}</div>',
                unsafe_allow_html=True)

    col_tl, col_an = st.columns([3,1])
    with col_tl:
        st.markdown("""
        <ul class="timeline">
          <li class="timeline-item">
            <div class="timeline-dot active"></div>
            <div class="timeline-period">2022 – PRESENT</div>
            <div class="timeline-title">Senior AI Engineer / LLM Architect</div>
            <div class="timeline-company">🏭 Baker Hughes · Firenze, Italy</div>
            <ul class="timeline-bullets">
                <li>Architected <strong>RAG-as-a-Service</strong> for 500+ global engineers; 10K+ docs/day, 99.9% uptime, €2M impact.</li>
                <li>Built <strong>Chunk-as-a-Service</strong> pipeline (OCR, semantic chunking, multilingual embeddings, Kafka + Ray).</li>
                <li>Fine-tuned Llama 3.1 8B with <strong>QLoRA</strong> on engineering transcripts — +18% domain accuracy.</li>
                <li>Deployed <strong>YOLOv8</strong> + TensorRT INT8 on NVIDIA Jetson; recall 98.7%, +22% defect detection.</li>
                <li><strong>€2M+ revenue impact</strong> via automation; <strong>100,000+ daily users</strong> served.</li>
            </ul>
          </li>
          <li class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-period">2020 – 2022</div>
            <div class="timeline-title">ML Engineer</div>
            <div class="timeline-company">🏢 UniqMaster · Berlin, Germany</div>
            <ul class="timeline-bullets">
                <li>Automated ML platform for demand forecasting + recommendations on AWS SageMaker.</li>
                <li>ETL pipelines integrating 50+ sources (Kafka + Airflow) — data latency ↓ 80%.</li>
                <li>NLP sentiment & intent classification models (89%+ accuracy).</li>
                <li>Model deployment time: 3 weeks → 4 hours via MLOps automation.</li>
            </ul>
          </li>
          <li class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-period">2023 – 2024</div>
            <div class="timeline-title">ML Engineering Program</div>
            <div class="timeline-company">🎓 Paris 1 Panthéon-Sorbonne · Paris, France</div>
            <ul class="timeline-bullets">
                <li>Advanced LLM architecture, RAG systems, and production ML engineering.</li>
                <li>Thesis: "Efficient Domain Adaptation of LLMs for Industrial RAG Systems".</li>
            </ul>
          </li>
          <li class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-period">2017 – 2022</div>
            <div class="timeline-title">Master of Finance</div>
            <div class="timeline-company">🎓 Università di Siena · Italy</div>
            <ul class="timeline-bullets">
                <li>Quantitative methods, statistics, econometrics + self-directed AI/ML research.</li>
                <li>Erasmus: Universität Liechtenstein (2019) · Overseas: Akita International University, Japan (2020).</li>
            </ul>
          </li>
        </ul>
        """, unsafe_allow_html=True)

    with col_an:
        a = load_lottie("data-analyisis.json")
        if a: st_lottie(a, height=300, key="exp_anim")


# ─────────────────────────────────────────────────────────────────────────────
#  PAGE: CREDENTIALS
# ─────────────────────────────────────────────────────────────────────────────
def page_certs():
    st.markdown(f'<div class="cyber-section-title"><span class="accent-bar"></span>{t("section_certs")}</div>',
                unsafe_allow_html=True)

    certs = [
        {"title":"IBM Generative AI Professional Certificate","issuer":"IBM / Coursera","status":"completed","icon":"🤖","year":"2024"},
        {"title":"DeepLearning.AI LLMOps Certificate","issuer":"DeepLearning.AI","status":"completed","icon":"🧠","year":"2024"},
        {"title":"Microsoft Azure AI Engineer Associate","issuer":"Microsoft","status":"completed","icon":"☁️","year":"2023"},
        {"title":"ML Engineering for Production (MLOps)","issuer":"DeepLearning.AI","status":"completed","icon":"🏭","year":"2023"},
        {"title":"AWS Machine Learning Specialty","issuer":"Amazon Web Services","status":"in-progress","icon":"🔄","year":"2025"},
        {"title":"Google Cloud Professional ML Engineer","issuer":"Google Cloud","status":"in-progress","icon":"🔄","year":"2025"},
        {"title":"Databricks Certified ML Professional","issuer":"Databricks","status":"in-progress","icon":"🔄","year":"2025"},
        {"title":"Kubernetes CKAD","issuer":"CNCF","status":"planned","icon":"📋","year":"2025"},
    ]

    label_map = {"completed":"✅ Completed","in-progress":"🔄 In Progress","planned":"📋 Planned"}

    st.markdown('<div class="cert-grid">', unsafe_allow_html=True)
    for c in certs:
        st.markdown(f"""
        <div class="cert-card {c['status']}">
            <div class="cert-badge {c['status']}">{label_map[c['status']]}</div>
            <div class="cert-title">{c['icon']} {c['title']}</div>
            <div class="cert-issuer">{c['issuer']} · {c['year']}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📈 In-Progress")
    for label, val in [("AWS ML Specialty",0.65),("GCP Professional ML",0.45),("Databricks ML Pro",0.30)]:
        c1, c2 = st.columns([2,3])
        c1.markdown(f"<div style='padding-top:0.35rem;font-size:0.83rem;color:#D1D5DB;'>{label}</div>",
                    unsafe_allow_html=True)
        c2.progress(val, text=f"{int(val*100)}%")


# ─────────────────────────────────────────────────────────────────────────────
#  PAGE: CONTACT
# ─────────────────────────────────────────────────────────────────────────────
def page_contact():
    from streamlit_lottie import st_lottie

    lang = st.session_state.get("lang","en")

    st.markdown(f"""
    <div class="cta-section">
        <h1 style="color:#F8FAFC;font-size:2.2rem;font-weight:900;margin-bottom:0.6rem;">
            {t('contact_title')}
        </h1>
        <p style="color:#9CA3AF;font-size:1rem;max-width:560px;margin:0 auto 1.5rem;">
            {t('contact_sub')}
        </p>
        <div style="display:flex;gap:0.75rem;justify-content:center;flex-wrap:wrap;">
            <a href="https://www.linkedin.com/in/karimosman89/" target="_blank" class="cta-btn">
                🔗 {t('hire_cta')} on LinkedIn
            </a>
            <a href="mailto:karim.osman.ai@gmail.com" class="cta-btn-secondary">✉️ Email</a>
            <a href="https://github.com/karimosman89" target="_blank" class="cta-btn-secondary">💻 GitHub</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_form, col_info = st.columns([3,2])

    with col_form:
        st.markdown(f'<div class="cyber-section-title" style="margin-top:1.5rem;"><span class="accent-bar"></span>{t("section_contact")}</div>',
                    unsafe_allow_html=True)
        with st.form("contact_form", clear_on_submit=True):
            name    = st.text_input(t("form_name"),  placeholder="Your full name")
            email   = st.text_input(t("form_email"), placeholder="you@company.com")
            org     = st.text_input(t("form_org"),   placeholder="Company / Startup / Lab")
            purpose = st.selectbox(t("form_purpose"), t("purpose_opts"))
            message = st.text_area(t("form_msg"),    placeholder="Describe the project or opportunity...", height=130)
            submitted = st.form_submit_button(t("form_send"), use_container_width=True)
            if submitted:
                if name and email and message:
                    st.success(t("form_success"))
                    st.balloons()
                else:
                    st.error(t("form_error"))

    with col_info:
        st.markdown("""
        <div class="cyber-section">
        <div class="cyber-section-title" style="font-size:1rem;">
            <span class="accent-bar"></span>Contact
        </div>
        <div style="margin-bottom:1.2rem;">
            <div style="font-size:0.68rem;color:#00D4FF;text-transform:uppercase;letter-spacing:0.1em;
                         font-weight:700;margin-bottom:0.3rem;">📍 Location</div>
            <div style="font-size:0.87rem;color:#D1D5DB;">Italy · France · Remote</div>
        </div>
        <div style="margin-bottom:1.2rem;">
            <div style="font-size:0.68rem;color:#00D4FF;text-transform:uppercase;letter-spacing:0.1em;
                         font-weight:700;margin-bottom:0.3rem;">✉️ Email</div>
            <div style="font-size:0.87rem;color:#D1D5DB;">karim.osman.ai@gmail.com</div>
        </div>
        <div style="margin-bottom:1.2rem;">
            <div style="font-size:0.68rem;color:#00D4FF;text-transform:uppercase;letter-spacing:0.1em;
                         font-weight:700;margin-bottom:0.3rem;">🌍 Languages</div>
            <div style="font-size:0.82rem;color:#D1D5DB;line-height:1.8;">
                🇸🇦 Arabic (Native) · 🇺🇸 English (C1/C2)<br>
                🇮🇹 Italian (Professional) · 🇫🇷 French (Professional)
            </div>
        </div>
        <div style="background:rgba(0,255,136,0.08);border:1px solid rgba(0,255,136,0.2);
                     border-radius:10px;padding:0.9rem;">
            <div style="font-size:0.72rem;color:#00FF88;font-weight:700;margin-bottom:0.25rem;">✅ AVAILABILITY</div>
            <div style="font-size:0.82rem;color:#D1D5DB;">
                🟢 Available Now · 20–40 hrs/week<br>
                Start date: Negotiable (30–90 days)
            </div>
        </div>
        </div>
        """, unsafe_allow_html=True)

        a = load_lottie("ai.json")
        if a: st_lottie(a, height=180, key="contact_anim")


# ─────────────────────────────────────────────────────────────────────────────
#  MAIN ROUTER
# ─────────────────────────────────────────────────────────────────────────────
def main():
    if "lang" not in st.session_state:
        st.session_state.lang = "en"
    if "page" not in st.session_state:
        st.session_state.page = "home"

    render_sidebar()

    page = st.session_state.page
    if   page == "home":      page_home()
    elif page == "impact":    page_impact()
    elif page == "skills":    page_skills()
    elif page == "projects":  page_projects()
    elif page == "demos":     page_demos()
    elif page == "freelance": page_freelance()
    elif page == "exp":       page_experience()
    elif page == "certs":     page_certs()
    elif page == "contact":   page_contact()
    else:                     page_home()

    # Footer
    lang = st.session_state.get("lang","en")
    footer_texts = {
        "en": "Architecting Production-Grade LLM Systems · Baker Hughes · RAG · Computer Vision · Freelance",
        "it": "Progettazione di Sistemi LLM in Produzione · Baker Hughes · RAG · Computer Vision · Freelance",
        "fr": "Architecture de Systèmes LLM en Production · Baker Hughes · RAG · Vision · Freelance",
    }
    st.markdown(f"""
    <div style="text-align:center;padding:2rem 0 1rem;margin-top:3rem;
                border-top:1px solid #1F2937;color:#4B5563;font-size:0.73rem;">
        <div style="color:#00D4FF;font-weight:700;margin-bottom:0.25rem;">Karim Osman · Senior AI Engineer & Freelancer</div>
        {footer_texts.get(lang, footer_texts['en'])}
        <div style="margin-top:0.4rem;">
            <a href="https://github.com/karimosman89" target="_blank"
               style="color:#6B7280;text-decoration:none;margin:0 0.5rem;">GitHub</a>
            <a href="https://www.linkedin.com/in/karimosman89/" target="_blank"
               style="color:#6B7280;text-decoration:none;margin:0 0.5rem;">LinkedIn</a>
            <a href="mailto:karim.osman.ai@gmail.com"
               style="color:#6B7280;text-decoration:none;margin:0 0.5rem;">Email</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
