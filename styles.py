"""
Elite AI Architect Portfolio — Cyber-Institutional Dark Theme
Complete CSS injection for Karim Osman's portfolio
"""

CYBER_CSS = """
<style>
/* ============================
   CYBER-INSTITUTIONAL THEME
   Primary: #0E1117 | Slate: #1F2937 | Electric Blue: #00D4FF
   ============================ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Lexend:wght@300;400;500;600;700;800&display=swap');

/* Root Variables */
:root {
    --deep-black:    #0E1117;
    --slate:         #1F2937;
    --slate-light:   #374151;
    --slate-border:  #2D3748;
    --electric-blue: #00D4FF;
    --blue-dim:      #0099BB;
    --blue-glow:     rgba(0, 212, 255, 0.15);
    --blue-glow-sm:  rgba(0, 212, 255, 0.08);
    --green-neon:    #00FF88;
    --amber:         #FFB347;
    --red-alert:     #FF4757;
    --white:         #F8FAFC;
    --text-muted:    #9CA3AF;
    --text-body:     #D1D5DB;
    --font-main:     'Inter', 'Lexend', sans-serif;
}

/* === GLOBAL RESET === */
html, body, [class*="css"] {
    font-family: var(--font-main) !important;
    background-color: var(--deep-black) !important;
    color: var(--text-body) !important;
}

.main .block-container {
    background-color: var(--deep-black) !important;
    padding: 1.5rem 2rem 3rem !important;
    max-width: 1400px !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0E1117 0%, #111827 50%, #0E1117 100%) !important;
    border-right: 1px solid var(--slate-border) !important;
}
[data-testid="stSidebar"] * {
    color: var(--text-body) !important;
}

/* Hide Streamlit default elements */
#MainMenu, footer, .stDeployButton { display: none !important; }
header[data-testid="stHeader"] {
    background: transparent !important;
    border-bottom: 1px solid var(--slate-border) !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--deep-black); }
::-webkit-scrollbar-thumb { background: var(--electric-blue); border-radius: 3px; }

/* === TYPOGRAPHY === */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Lexend', var(--font-main) !important;
    color: var(--white) !important;
    letter-spacing: -0.02em;
}

/* === HERO HEADER === */
.cyber-hero {
    background: linear-gradient(135deg, #0E1117 0%, #111827 40%, #0E1117 100%);
    border: 1px solid var(--slate-border);
    border-radius: 20px;
    padding: 3.5rem 3rem;
    margin: 0 0 2rem 0;
    position: relative;
    overflow: hidden;
    text-align: center;
}
.cyber-hero::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, transparent, var(--electric-blue), transparent);
    animation: scan-line 3s ease-in-out infinite;
}
.cyber-hero::after {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 80% 50% at 50% 0%, rgba(0,212,255,0.07), transparent);
    pointer-events: none;
}
@keyframes scan-line {
    0%,100% { background-position: -100% 0; }
    50% { background-position: 200% 0; }
}

.hero-name {
    font-size: clamp(2.2rem, 5vw, 4rem);
    font-weight: 900;
    font-family: 'Lexend', sans-serif !important;
    background: linear-gradient(135deg, #FFFFFF 0%, var(--electric-blue) 60%, #0099BB 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 0.5rem 0;
    line-height: 1.1;
}
.hero-title {
    font-size: 1.25rem;
    color: var(--electric-blue) !important;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.hero-subtitle {
    font-size: 1.05rem;
    color: var(--text-muted) !important;
    max-width: 640px;
    margin: 0 auto 2rem;
    line-height: 1.7;
}
.hero-badges {
    display: flex;
    gap: 0.75rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 2rem;
}
.hero-badge {
    background: var(--blue-glow);
    border: 1px solid var(--electric-blue);
    color: var(--electric-blue) !important;
    border-radius: 20px;
    padding: 0.3rem 1rem;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* === KPI METRIC CARDS === */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.25rem;
    margin: 1.5rem 0;
}
.kpi-card {
    background: var(--slate);
    border: 1px solid var(--slate-border);
    border-radius: 16px;
    padding: 1.5rem 1.25rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    cursor: default;
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    border-radius: 16px 16px 0 0;
}
.kpi-card.blue::before  { background: var(--electric-blue); }
.kpi-card.green::before { background: var(--green-neon); }
.kpi-card.amber::before { background: var(--amber); }
.kpi-card.red::before   { background: var(--red-alert); }

.kpi-card:hover {
    transform: translateY(-4px);
    border-color: var(--electric-blue);
    box-shadow: 0 8px 32px var(--blue-glow);
}
.kpi-value {
    font-family: 'Lexend', sans-serif;
    font-size: 2.4rem;
    font-weight: 800;
    line-height: 1;
    margin-bottom: 0.4rem;
}
.kpi-card.blue  .kpi-value { color: var(--electric-blue) !important; }
.kpi-card.green .kpi-value { color: var(--green-neon) !important; }
.kpi-card.amber .kpi-value { color: var(--amber) !important; }
.kpi-card.red   .kpi-value { color: var(--red-alert) !important; }
.kpi-label {
    font-size: 0.78rem;
    color: var(--text-muted) !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-weight: 600;
    line-height: 1.4;
}
.kpi-delta {
    font-size: 0.7rem;
    color: var(--green-neon) !important;
    margin-top: 0.4rem;
    font-weight: 600;
}

/* === SECTION CONTAINER === */
.cyber-section {
    background: var(--slate);
    border: 1px solid var(--slate-border);
    border-radius: 16px;
    padding: 2rem;
    margin: 1.5rem 0;
    position: relative;
    overflow: hidden;
}
.cyber-section-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--white) !important;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}
.cyber-section-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--electric-blue), transparent);
    margin-left: 0.5rem;
}
.accent-bar {
    display: inline-block;
    width: 4px; height: 1.4rem;
    background: var(--electric-blue);
    border-radius: 2px;
    margin-right: 0.5rem;
    vertical-align: middle;
}

/* === TECH SKILL PILLS === */
.skill-group { margin-bottom: 1.5rem; }
.skill-group-title {
    font-size: 0.7rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--electric-blue) !important;
    font-weight: 700;
    margin-bottom: 0.75rem;
}
.skill-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}
.skill-pill {
    background: var(--blue-glow-sm);
    border: 1px solid var(--slate-border);
    border-radius: 8px;
    padding: 0.3rem 0.75rem;
    font-size: 0.78rem;
    color: var(--text-body) !important;
    font-weight: 500;
    transition: all 0.2s ease;
}
.skill-pill:hover {
    border-color: var(--electric-blue);
    background: var(--blue-glow);
    color: var(--white) !important;
}
.skill-pill.core    { border-color: rgba(0,212,255,0.3);  }
.skill-pill.cloud   { border-color: rgba(255,179,71,0.3); color: #FFB347 !important; }
.skill-pill.data    { border-color: rgba(0,255,136,0.3);  color: #00FF88 !important; }

/* === TIMELINE / STEPPER === */
.timeline { position: relative; padding: 0; margin: 0; list-style: none; }
.timeline::before {
    content: '';
    position: absolute;
    left: 20px; top: 0; bottom: 0; width: 2px;
    background: linear-gradient(180deg, var(--electric-blue), var(--slate-border));
}
.timeline-item {
    position: relative;
    padding: 0 0 2rem 3.5rem;
}
.timeline-dot {
    position: absolute;
    left: 12px; top: 4px;
    width: 18px; height: 18px;
    border-radius: 50%;
    border: 2px solid var(--electric-blue);
    background: var(--deep-black);
    box-shadow: 0 0 12px var(--electric-blue);
}
.timeline-dot.active {
    background: var(--electric-blue);
    box-shadow: 0 0 20px var(--electric-blue);
}
.timeline-period {
    font-size: 0.72rem;
    color: var(--electric-blue) !important;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.25rem;
}
.timeline-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--white) !important;
    margin-bottom: 0.2rem;
}
.timeline-company {
    font-size: 0.9rem;
    color: var(--text-muted) !important;
    margin-bottom: 0.6rem;
}
.timeline-bullets { padding-left: 1rem; margin: 0; }
.timeline-bullets li {
    font-size: 0.85rem;
    color: var(--text-body) !important;
    line-height: 1.7;
    margin-bottom: 0.25rem;
    list-style: none;
    position: relative;
}
.timeline-bullets li::before {
    content: '▹';
    color: var(--electric-blue);
    position: absolute;
    left: -1rem;
}

/* === GITHUB REPO CARDS === */
.repo-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.25rem;
    margin-top: 1.5rem;
}
.repo-card {
    background: var(--slate);
    border: 1px solid var(--slate-border);
    border-radius: 14px;
    padding: 1.5rem;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    height: 100%;
}
.repo-card:hover {
    border-color: var(--electric-blue);
    box-shadow: 0 8px 32px var(--blue-glow);
    transform: translateY(-4px);
}
.repo-name {
    font-size: 1rem;
    font-weight: 700;
    color: var(--electric-blue) !important;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.repo-desc {
    font-size: 0.82rem;
    color: var(--text-muted) !important;
    line-height: 1.6;
    flex: 1;
    margin-bottom: 1rem;
}
.repo-meta {
    display: flex;
    gap: 1rem;
    align-items: center;
    flex-wrap: wrap;
}
.repo-lang {
    font-size: 0.72rem;
    font-weight: 600;
    padding: 0.2rem 0.6rem;
    border-radius: 6px;
    background: var(--blue-glow-sm);
    border: 1px solid var(--slate-border);
}
.repo-star { font-size: 0.75rem; color: var(--amber) !important; font-weight: 600; }
.repo-topic {
    font-size: 0.65rem;
    padding: 0.15rem 0.5rem;
    border-radius: 10px;
    border: 1px solid var(--slate-border);
    color: var(--text-muted) !important;
    background: transparent;
}

/* === CERTIFICATION VAULT === */
.cert-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
}
.cert-card {
    background: var(--slate);
    border: 1px solid var(--slate-border);
    border-radius: 12px;
    padding: 1.25rem;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
}
.cert-card:hover {
    border-color: var(--electric-blue);
    box-shadow: 0 4px 20px var(--blue-glow);
}
.cert-card.completed { border-left: 4px solid var(--green-neon); }
.cert-card.in-progress { border-left: 4px solid var(--amber); }
.cert-card.planned { border-left: 4px solid var(--slate-border); }
.cert-badge {
    display: inline-block;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.2rem 0.6rem;
    border-radius: 20px;
    margin-bottom: 0.6rem;
}
.cert-badge.completed  { background: rgba(0,255,136,0.1); color: var(--green-neon) !important; border: 1px solid rgba(0,255,136,0.3); }
.cert-badge.in-progress{ background: rgba(255,179,71,0.1); color: var(--amber) !important;     border: 1px solid rgba(255,179,71,0.3); }
.cert-badge.planned    { background: rgba(156,163,175,0.1); color: var(--text-muted) !important; border: 1px solid var(--slate-border); }
.cert-title { font-size: 0.92rem; font-weight: 700; color: var(--white) !important; margin-bottom: 0.3rem; }
.cert-issuer { font-size: 0.78rem; color: var(--text-muted) !important; }

/* === RAG ASSISTANT SIDEBAR === */
.rag-header {
    background: linear-gradient(135deg, var(--slate), #111827);
    border: 1px solid var(--electric-blue);
    border-radius: 12px;
    padding: 1rem;
    margin-bottom: 1rem;
    text-align: center;
}
.rag-title {
    color: var(--electric-blue) !important;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}
.rag-pulse {
    display: inline-block;
    width: 8px; height: 8px;
    background: var(--green-neon);
    border-radius: 50%;
    animation: pulse 2s infinite;
    margin-right: 6px;
}
@keyframes pulse {
    0%,100% { opacity: 1; transform: scale(1); }
    50%      { opacity: 0.5; transform: scale(0.8); }
}
.chat-bubble-user {
    background: var(--blue-glow);
    border: 1px solid var(--electric-blue);
    border-radius: 12px 12px 4px 12px;
    padding: 0.6rem 0.9rem;
    font-size: 0.82rem;
    color: var(--white) !important;
    margin-bottom: 0.5rem;
    max-width: 90%;
    margin-left: auto;
}
.chat-bubble-ai {
    background: var(--slate);
    border: 1px solid var(--slate-border);
    border-radius: 12px 12px 12px 4px;
    padding: 0.6rem 0.9rem;
    font-size: 0.82rem;
    color: var(--text-body) !important;
    margin-bottom: 0.5rem;
    max-width: 92%;
}

/* === MERMAID ARCHITECTURE === */
.arch-container {
    background: #0B0F1A;
    border: 1px solid var(--slate-border);
    border-radius: 16px;
    padding: 2rem;
    overflow-x: auto;
}
.arch-tab-active {
    background: var(--electric-blue) !important;
    color: #000 !important;
    font-weight: 700 !important;
}

/* === IMPACT REVENUE === */
.revenue-hero {
    background: linear-gradient(135deg, #0B1E0B 0%, #0E2A0E 50%, #0B1E0B 100%);
    border: 1px solid rgba(0,255,136,0.25);
    border-radius: 20px;
    padding: 3rem 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.revenue-hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 60% 60% at 50% 0%, rgba(0,255,136,0.08), transparent);
    pointer-events: none;
}
.revenue-number {
    font-family: 'Lexend', sans-serif;
    font-size: clamp(3rem, 8vw, 5.5rem);
    font-weight: 900;
    color: var(--green-neon) !important;
    line-height: 1;
    display: block;
    text-shadow: 0 0 40px rgba(0,255,136,0.4);
    animation: counter-glow 3s ease-in-out infinite;
}
@keyframes counter-glow {
    0%,100% { text-shadow: 0 0 40px rgba(0,255,136,0.3); }
    50%      { text-shadow: 0 0 80px rgba(0,255,136,0.6); }
}
.revenue-label {
    font-size: 1.1rem;
    color: var(--text-muted) !important;
    margin-top: 0.5rem;
    letter-spacing: 0.05em;
}

/* === LANGUAGE TOGGLE === */
.lang-toggle {
    display: flex;
    gap: 0.5rem;
    justify-content: center;
    margin-bottom: 1rem;
}
.lang-btn {
    background: transparent;
    border: 1px solid var(--slate-border);
    border-radius: 8px;
    padding: 0.35rem 0.75rem;
    font-size: 0.78rem;
    color: var(--text-muted) !important;
    cursor: pointer;
    transition: all 0.2s ease;
}
.lang-btn.active {
    background: var(--blue-glow);
    border-color: var(--electric-blue);
    color: var(--electric-blue) !important;
    font-weight: 600;
}

/* === CTA SECTION === */
.cta-section {
    background: linear-gradient(135deg, var(--slate) 0%, #111827 100%);
    border: 1px solid var(--electric-blue);
    border-radius: 20px;
    padding: 3rem 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin: 2rem 0;
}
.cta-section::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 70% 50% at 50% 0%, var(--blue-glow), transparent);
    pointer-events: none;
}
.cta-btn {
    display: inline-block;
    background: linear-gradient(135deg, var(--electric-blue), var(--blue-dim));
    color: #000 !important;
    font-weight: 800;
    font-size: 1rem;
    padding: 0.8rem 2.5rem;
    border-radius: 50px;
    text-decoration: none !important;
    letter-spacing: 0.02em;
    transition: all 0.3s ease;
    box-shadow: 0 8px 30px rgba(0,212,255,0.3);
    border: none;
    cursor: pointer;
}
.cta-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(0,212,255,0.5);
}
.cta-btn-secondary {
    display: inline-block;
    background: transparent;
    border: 2px solid var(--electric-blue);
    color: var(--electric-blue) !important;
    font-weight: 700;
    font-size: 0.9rem;
    padding: 0.75rem 2rem;
    border-radius: 50px;
    text-decoration: none !important;
    transition: all 0.3s ease;
}
.cta-btn-secondary:hover {
    background: var(--blue-glow);
    transform: translateY(-2px);
}

/* Streamlit button overrides */
.stButton > button {
    background: linear-gradient(135deg, var(--electric-blue), var(--blue-dim)) !important;
    color: #000 !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.5rem 1.25rem !important;
    transition: all 0.3s ease !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(0,212,255,0.35) !important;
}

/* Input fields */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: var(--slate) !important;
    border: 1px solid var(--slate-border) !important;
    color: var(--text-body) !important;
    border-radius: 8px !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--electric-blue) !important;
    box-shadow: 0 0 0 2px var(--blue-glow) !important;
}

/* Selectbox */
.stSelectbox > div > div {
    background: var(--slate) !important;
    border: 1px solid var(--slate-border) !important;
    border-radius: 8px !important;
    color: var(--text-body) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: var(--slate) !important;
    border-radius: 10px !important;
    padding: 4px !important;
    border: 1px solid var(--slate-border) !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: var(--text-muted) !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}
.stTabs [aria-selected="true"] {
    background: var(--blue-glow) !important;
    color: var(--electric-blue) !important;
    border: 1px solid var(--electric-blue) !important;
}

/* Metrics */
[data-testid="stMetric"] {
    background: var(--slate) !important;
    border: 1px solid var(--slate-border) !important;
    border-radius: 12px !important;
    padding: 1rem !important;
}
[data-testid="stMetricValue"] { color: var(--electric-blue) !important; font-weight: 800 !important; }
[data-testid="stMetricDelta"] { color: var(--green-neon) !important; }

/* Expander */
.streamlit-expanderHeader {
    background: var(--slate) !important;
    border: 1px solid var(--slate-border) !important;
    border-radius: 10px !important;
    color: var(--white) !important;
}
.streamlit-expanderContent {
    background: var(--slate) !important;
    border: 1px solid var(--slate-border) !important;
    border-top: none !important;
    border-radius: 0 0 10px 10px !important;
}

/* Multiselect */
.stMultiSelect > div {
    background: var(--slate) !important;
    border: 1px solid var(--slate-border) !important;
    border-radius: 8px !important;
}

/* Progress bar */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, var(--electric-blue), var(--blue-dim)) !important;
    border-radius: 4px !important;
}

/* Radio buttons */
.stRadio > div { gap: 0.5rem !important; }
.stRadio [role="radio"] { border-color: var(--slate-border) !important; }
.stRadio [aria-checked="true"] div { background: var(--electric-blue) !important; }

/* Divider */
hr { border-color: var(--slate-border) !important; margin: 1.5rem 0 !important; }

/* Mermaid overrides */
.mermaid { background: transparent !important; }
svg[id*="mermaid"] text { fill: var(--text-body) !important; }
svg[id*="mermaid"] .node rect,
svg[id*="mermaid"] .node circle {
    fill: var(--slate) !important;
    stroke: var(--electric-blue) !important;
}

/* Glow tag */
.glow-tag {
    display: inline-block;
    background: var(--blue-glow);
    border: 1px solid var(--electric-blue);
    color: var(--electric-blue) !important;
    border-radius: 6px;
    padding: 0.15rem 0.55rem;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.05em;
}
.success-tag {
    background: rgba(0,255,136,0.08);
    border: 1px solid rgba(0,255,136,0.3);
    color: var(--green-neon) !important;
    border-radius: 6px;
    padding: 0.15rem 0.55rem;
    font-size: 0.7rem;
    font-weight: 700;
    display: inline-block;
}

/* Responsive */
@media (max-width: 768px) {
    .main .block-container { padding: 1rem 0.75rem 2rem !important; }
    .cyber-hero { padding: 2rem 1.25rem; }
    .hero-name { font-size: 2rem; }
    .kpi-grid { grid-template-columns: repeat(2, 1fr); }
    .repo-grid { grid-template-columns: 1fr; }
}
@media (max-width: 480px) {
    .kpi-grid { grid-template-columns: 1fr 1fr; }
    .hero-badges { flex-wrap: wrap; gap: 0.5rem; }
}
</style>
"""
