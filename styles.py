"""
Elite AI Architect Portfolio — Tech-Sector Dark Theme v3
Complete CSS: animated circuit background, JetBrains Mono + Inter fonts,
proper tech-sector aesthetics — no broken references.
"""

CYBER_CSS = """
<style>
/* ══════════════════════════════════════════════════════
   TECH-SECTOR DARK THEME  v3
   bg #080C14 | panel #0D1321 | accent #00D4FF | green #39FF14
   ══════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700;800&display=swap');

/* ── Root tokens ── */
:root {
  --bg:           #080C14;
  --bg2:          #0D1321;
  --bg3:          #111827;
  --panel:        #0F1923;
  --border:       #1E2D40;
  --border2:      #253347;
  --cyan:         #00D4FF;
  --cyan-dim:     rgba(0,212,255,0.12);
  --cyan-glow:    rgba(0,212,255,0.22);
  --green:        #39FF14;
  --green-dim:    rgba(57,255,20,0.10);
  --amber:        #F59E0B;
  --red:          #EF4444;
  --purple:       #8B5CF6;
  --white:        #F1F5F9;
  --muted:        #64748B;
  --body:         #CBD5E1;
  --mono:         'JetBrains Mono', 'Courier New', monospace;
  --sans:         'Space Grotesk', 'Inter', sans-serif;
  --ui:           'Inter', sans-serif;
}

/* ── Global reset ── */
html, body, [class*="css"] {
  font-family: var(--ui) !important;
  background-color: var(--bg) !important;
  color: var(--body) !important;
}

.main .block-container {
  background-color: var(--bg) !important;
  padding: 1.5rem 2rem 4rem !important;
  max-width: 1400px !important;
}

/* ── Animated circuit-board background ── */
.main::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image:
    linear-gradient(rgba(0,212,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,212,255,0.03) 1px, transparent 1px);
  background-size: 48px 48px;
  pointer-events: none;
  z-index: 0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #080C14 0%, #0D1321 60%, #080C14 100%) !important;
  border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--body) !important; }

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, .stDeployButton { display: none !important; }
header[data-testid="stHeader"] {
  background: transparent !important;
  border-bottom: 1px solid var(--border) !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--cyan); border-radius: 3px; }

/* ══ TYPOGRAPHY ══ */
h1, h2, h3 {
  font-family: var(--sans) !important;
  color: var(--white) !important;
  letter-spacing: -0.025em;
}
h4, h5, h6 {
  font-family: var(--ui) !important;
  color: var(--white) !important;
}
code, pre {
  font-family: var(--mono) !important;
  background: var(--bg3) !important;
  color: var(--cyan) !important;
  border-radius: 6px !important;
}

/* ══ HERO ══ */
.cyber-hero {
  background: linear-gradient(135deg, #080C14 0%, #0D1827 50%, #080C14 100%);
  border: 1px solid var(--border2);
  border-radius: 24px;
  padding: 4rem 3rem;
  margin: 0 0 2rem;
  position: relative;
  overflow: hidden;
  text-align: center;
}
.cyber-hero::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg,
    transparent 0%, var(--cyan) 30%, #8B5CF6 60%, var(--green) 80%, transparent 100%);
  animation: top-beam 4s linear infinite;
}
.cyber-hero::after {
  content: '';
  position: absolute; inset: 0;
  background:
    radial-gradient(ellipse 70% 40% at 50% 0%, rgba(0,212,255,0.08), transparent),
    radial-gradient(ellipse 40% 60% at 80% 80%, rgba(139,92,246,0.05), transparent);
  pointer-events: none;
}
@keyframes top-beam {
  0%   { background-position: -200% 0; }
  100% { background-position: 300% 0; }
}

.hero-name {
  font-size: clamp(2.4rem, 5vw, 4.2rem);
  font-weight: 800;
  font-family: var(--sans) !important;
  background: linear-gradient(135deg, #FFFFFF 0%, var(--cyan) 55%, var(--purple) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0 0 0.5rem;
  line-height: 1.05;
}
.hero-title {
  font-family: var(--mono) !important;
  font-size: 0.95rem;
  color: var(--cyan) !important;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin-bottom: 1.2rem;
}
.hero-subtitle {
  font-size: 1.05rem;
  color: var(--muted) !important;
  max-width: 660px;
  margin: 0 auto 2.2rem;
  line-height: 1.75;
}
.hero-badges {
  display: flex; gap: 0.6rem;
  justify-content: center; flex-wrap: wrap;
  margin-bottom: 2rem;
}
.hero-badge {
  background: rgba(0,212,255,0.08);
  border: 1px solid rgba(0,212,255,0.35);
  color: var(--cyan) !important;
  border-radius: 6px;
  padding: 0.25rem 0.85rem;
  font-size: 0.72rem; font-weight: 600;
  letter-spacing: 0.1em; text-transform: uppercase;
  font-family: var(--mono) !important;
}

/* ══ KPI CARDS ══ */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(185px, 1fr));
  gap: 1rem; margin: 1.5rem 0;
}
.kpi-card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 1.5rem 1.25rem;
  text-align: center;
  position: relative; overflow: hidden;
  transition: all 0.3s ease;
}
.kpi-card::before {
  content: ''; position: absolute;
  top: 0; left: 0; right: 0; height: 2px;
  border-radius: 16px 16px 0 0;
}
.kpi-card.blue::before   { background: linear-gradient(90deg, var(--cyan), var(--purple)); }
.kpi-card.green::before  { background: linear-gradient(90deg, var(--green), var(--cyan)); }
.kpi-card.amber::before  { background: linear-gradient(90deg, var(--amber), var(--red)); }
.kpi-card.red::before    { background: linear-gradient(90deg, var(--red), var(--amber)); }
.kpi-card.purple::before { background: linear-gradient(90deg, var(--purple), var(--cyan)); }
.kpi-card:hover {
  transform: translateY(-4px);
  border-color: var(--border2);
  box-shadow: 0 8px 32px rgba(0,212,255,0.12);
}
.kpi-value {
  font-family: var(--mono) !important;
  font-size: 2.2rem; font-weight: 700;
  line-height: 1; margin-bottom: 0.4rem;
}
.kpi-card.blue   .kpi-value { color: var(--cyan) !important; }
.kpi-card.green  .kpi-value { color: var(--green) !important; }
.kpi-card.amber  .kpi-value { color: var(--amber) !important; }
.kpi-card.red    .kpi-value { color: var(--red) !important; }
.kpi-card.purple .kpi-value { color: var(--purple) !important; }
.kpi-label {
  font-size: 0.72rem; color: var(--muted) !important;
  letter-spacing: 0.1em; text-transform: uppercase;
  font-weight: 600; line-height: 1.4;
}
.kpi-delta {
  font-size: 0.68rem; color: var(--green) !important;
  margin-top: 0.35rem; font-weight: 600;
  font-family: var(--mono) !important;
}

/* ══ SECTION TITLE ══ */
.cyber-section-title {
  font-size: 1.35rem; font-weight: 700;
  color: var(--white) !important;
  margin-bottom: 1.5rem;
  display: flex; align-items: center; gap: 0.75rem;
  font-family: var(--sans) !important;
}
.cyber-section-title::after {
  content: ''; flex: 1; height: 1px;
  background: linear-gradient(90deg, var(--border2), transparent);
  margin-left: 0.5rem;
}
.accent-bar {
  display: inline-block; width: 3px; height: 1.35rem;
  background: linear-gradient(180deg, var(--cyan), var(--purple));
  border-radius: 2px; margin-right: 0.4rem; vertical-align: middle;
}

/* ══ PANELS / CARDS ══ */
.cyber-section {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 1.75rem;
  margin: 1rem 0;
  position: relative;
}
.cyber-section:hover { border-color: var(--border2); }

/* ══ TECH ICON GRID ══ */
.tech-icon-grid {
  display: flex; flex-wrap: wrap; gap: 0.75rem;
  align-items: flex-start; margin: 0.75rem 0;
}
.tech-icon-item {
  display: flex; flex-direction: column;
  align-items: center; gap: 0.3rem;
  min-width: 56px; max-width: 64px;
}
.tech-icon-item img {
  width: 36px; height: 36px;
  border-radius: 8px;
  background: var(--bg3);
  padding: 5px;
  border: 1px solid var(--border);
  transition: all 0.2s ease;
}
.tech-icon-item img:hover {
  border-color: var(--cyan);
  box-shadow: 0 0 12px rgba(0,212,255,0.25);
  transform: translateY(-2px);
}
.tech-icon-item span {
  font-size: 0.58rem; color: var(--muted);
  text-align: center; font-family: var(--mono) !important;
  white-space: nowrap;
}

/* ══ SKILL PILLS ══ */
.skill-group { margin-bottom: 1.25rem; }
.skill-group-title {
  font-family: var(--mono) !important;
  font-size: 0.65rem; letter-spacing: 0.15em;
  text-transform: uppercase; color: var(--cyan) !important;
  font-weight: 600; margin-bottom: 0.6rem;
}
.skill-pills { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.skill-pill {
  background: rgba(0,212,255,0.06);
  border: 1px solid var(--border);
  border-radius: 6px; padding: 0.25rem 0.65rem;
  font-size: 0.76rem; color: var(--body) !important;
  font-weight: 500; transition: all 0.2s ease;
  font-family: var(--ui) !important;
}
.skill-pill:hover { border-color: var(--cyan); color: var(--cyan) !important; }
.skill-pill.core  { border-color: rgba(0,212,255,0.25); }
.skill-pill.cloud { border-color: rgba(245,158,11,0.25); color: var(--amber) !important; }
.skill-pill.data  { border-color: rgba(57,255,20,0.25);  color: var(--green) !important; }

/* ══ PROJECT CARDS ══ */
.proj-card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.3s ease;
  height: 100%;
}
.proj-card:hover {
  border-color: var(--border2);
  box-shadow: 0 10px 40px rgba(0,212,255,0.1);
  transform: translateY(-3px);
}
.proj-card-img {
  width: 100%; height: 160px;
  object-fit: cover; display: block;
  filter: brightness(0.7) saturate(1.3);
  transition: filter 0.3s ease;
}
.proj-card:hover .proj-card-img { filter: brightness(0.85) saturate(1.4); }
.proj-card-body { padding: 1.1rem; }
.proj-card-category {
  font-family: var(--mono) !important;
  font-size: 0.6rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.12em;
  color: var(--cyan) !important; margin-bottom: 0.4rem;
}
.proj-card-title {
  font-family: var(--sans) !important;
  font-size: 1rem; font-weight: 700;
  color: var(--white) !important; margin-bottom: 0.4rem;
  line-height: 1.3;
}
.proj-card-org {
  font-size: 0.72rem; color: var(--muted) !important;
  margin-bottom: 0.6rem;
}
.proj-card-desc {
  font-size: 0.8rem; color: var(--body) !important;
  line-height: 1.65; margin-bottom: 0.75rem;
}
.proj-impact {
  display: inline-flex; align-items: center; gap: 0.4rem;
  background: rgba(57,255,20,0.08);
  border: 1px solid rgba(57,255,20,0.25);
  border-radius: 8px; padding: 0.3rem 0.7rem;
  font-size: 0.72rem; font-weight: 700;
  color: var(--green) !important;
  font-family: var(--mono) !important;
}
.proj-metrics {
  display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.75rem;
}
.proj-metric {
  background: var(--bg3);
  border: 1px solid var(--border);
  border-radius: 8px; padding: 0.4rem 0.6rem;
  text-align: center; min-width: 72px;
}
.proj-metric-val {
  font-family: var(--mono) !important;
  font-size: 1rem; font-weight: 700; color: var(--cyan) !important;
}
.proj-metric-lbl {
  font-size: 0.6rem; color: var(--muted) !important;
  text-transform: uppercase; letter-spacing: 0.06em;
}

/* ══ GITHUB REPO CARDS ══ */
.repo-card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 14px;
  overflow: hidden;
  transition: all 0.3s ease;
}
.repo-card:hover {
  border-color: var(--border2);
  box-shadow: 0 8px 30px rgba(0,212,255,0.1);
  transform: translateY(-3px);
}
.repo-name {
  font-family: var(--mono) !important;
  font-size: 0.9rem; font-weight: 700;
  color: var(--cyan) !important; margin-bottom: 0.4rem;
}
.repo-desc {
  font-size: 0.8rem; color: var(--muted) !important;
  line-height: 1.6; flex: 1; margin-bottom: 0.75rem;
}
.repo-meta {
  display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;
}
.repo-lang {
  font-family: var(--mono) !important;
  font-size: 0.68rem; font-weight: 600;
  padding: 0.15rem 0.5rem; border-radius: 5px;
  background: var(--bg3); border: 1px solid var(--border);
  display: flex; align-items: center; gap: 4px;
}
.repo-star { font-size: 0.72rem; color: var(--amber) !important; font-weight: 600; }
.repo-topic {
  font-size: 0.62rem; padding: 0.12rem 0.45rem;
  border-radius: 10px; border: 1px solid var(--border);
  color: var(--muted) !important; background: transparent;
}

/* ══ ARCH DIAGRAM ══ */
.arch-container {
  background: #05080F;
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 2rem 2.5rem;
  overflow-x: auto;
  position: relative;
}
.arch-container::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, var(--cyan), var(--purple), var(--green));
  border-radius: 16px 16px 0 0;
}
.arch-container pre {
  font-family: var(--mono) !important;
  font-size: 0.78rem; color: #A8D8EA !important;
  line-height: 1.7; white-space: pre; margin: 0;
}

/* ══ DEMO CARDS (replacing YouTube) ══ */
.demo-card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 14px;
  overflow: hidden;
  transition: all 0.3s ease;
  position: relative;
}
.demo-card:hover {
  border-color: var(--border2);
  box-shadow: 0 8px 32px rgba(0,212,255,0.1);
}
.demo-card-visual {
  width: 100%; height: 155px;
  display: flex; align-items: center; justify-content: center;
  position: relative; overflow: hidden;
}
.demo-card-body { padding: 0.9rem 1rem 1rem; }
.demo-card-title {
  font-family: var(--sans) !important;
  font-size: 0.88rem; font-weight: 700;
  color: var(--white) !important; margin-bottom: 0.3rem;
}
.demo-card-desc {
  font-size: 0.74rem; color: var(--muted) !important; line-height: 1.55;
}

/* ══ TIMELINE ══ */
.timeline { position: relative; padding: 0; margin: 0; list-style: none; }
.timeline::before {
  content: ''; position: absolute;
  left: 20px; top: 0; bottom: 0; width: 2px;
  background: linear-gradient(180deg, var(--cyan) 0%, var(--purple) 60%, var(--border) 100%);
}
.timeline-item { position: relative; padding: 0 0 2.5rem 3.75rem; }
.timeline-dot {
  position: absolute; left: 12px; top: 4px;
  width: 18px; height: 18px; border-radius: 50%;
  border: 2px solid var(--cyan);
  background: var(--bg);
  box-shadow: 0 0 12px rgba(0,212,255,0.4);
}
.timeline-dot.active {
  background: var(--cyan);
  box-shadow: 0 0 20px rgba(0,212,255,0.7);
}
.timeline-period {
  font-family: var(--mono) !important;
  font-size: 0.68rem; color: var(--cyan) !important;
  font-weight: 600; letter-spacing: 0.1em;
  text-transform: uppercase; margin-bottom: 0.3rem;
}
.timeline-title {
  font-family: var(--sans) !important;
  font-size: 1.05rem; font-weight: 700;
  color: var(--white) !important; margin-bottom: 0.2rem;
}
.timeline-company {
  font-size: 0.88rem; color: var(--muted) !important; margin-bottom: 0.65rem;
}
.timeline-bullets { padding-left: 0; margin: 0; list-style: none; }
.timeline-bullets li {
  font-size: 0.83rem; color: var(--body) !important;
  line-height: 1.7; margin-bottom: 0.3rem;
  position: relative; padding-left: 1.1rem;
}
.timeline-bullets li::before {
  content: '›'; color: var(--cyan); position: absolute; left: 0;
  font-size: 1rem; line-height: 1.6;
}

/* ══ COMPANY LOGO STRIP ══ */
.company-strip {
  display: flex; gap: 2rem; align-items: center;
  flex-wrap: wrap; padding: 0.9rem 1.25rem;
  background: var(--panel); border-radius: 12px;
  border: 1px solid var(--border); margin-bottom: 1.75rem;
}
.company-logo-item {
  display: flex; align-items: center; gap: 0.6rem;
}
.company-logo-item span {
  font-size: 0.72rem; color: var(--muted);
  font-family: var(--mono) !important;
}

/* ══ CERTIFICATION VAULT ══ */
.cert-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1rem;
}
.cert-card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 14px; padding: 1.1rem;
  position: relative; overflow: hidden;
  transition: all 0.3s ease;
}
.cert-card:hover { border-color: var(--border2); }
.cert-card.completed  { border-left: 3px solid var(--green); }
.cert-card.in-progress{ border-left: 3px solid var(--amber); }
.cert-card.planned    { border-left: 3px solid var(--border2); }
.cert-badge {
  display: inline-block; font-family: var(--mono) !important;
  font-size: 0.6rem; font-weight: 700;
  letter-spacing: 0.1em; text-transform: uppercase;
  padding: 0.15rem 0.5rem; border-radius: 4px; margin-bottom: 0.5rem;
}
.cert-badge.completed  { background: rgba(57,255,20,0.08); color: var(--green) !important; border: 1px solid rgba(57,255,20,0.3); }
.cert-badge.in-progress{ background: rgba(245,158,11,0.08); color: var(--amber) !important; border: 1px solid rgba(245,158,11,0.3); }
.cert-badge.planned    { background: rgba(100,116,139,0.08); color: var(--muted) !important; border: 1px solid var(--border); }
.cert-title  { font-size: 0.88rem; font-weight: 700; color: var(--white) !important; margin-bottom: 0.25rem; line-height: 1.35; }
.cert-issuer { font-size: 0.72rem; color: var(--muted) !important; font-family: var(--mono) !important; }

/* ══ FREELANCE SERVICE CARDS ══ */
.service-card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 16px; overflow: hidden;
  transition: all 0.3s ease; height: 100%;
}
.service-card:hover {
  border-color: var(--border2);
  box-shadow: 0 10px 40px rgba(0,212,255,0.08);
  transform: translateY(-3px);
}
.service-card-img {
  width: 100%; height: 130px;
  object-fit: cover; display: block;
  filter: brightness(0.6) saturate(1.2);
}
.service-card-body { padding: 1rem 1.1rem 1.1rem; }
.service-icon {
  font-size: 1.8rem; margin-bottom: 0.4rem; display: block;
}
.service-title {
  font-family: var(--sans) !important;
  font-size: 0.97rem; font-weight: 700;
  color: var(--white) !important; margin-bottom: 0.4rem;
}
.service-desc {
  font-size: 0.78rem; color: var(--muted) !important;
  line-height: 1.6; margin-bottom: 0.6rem;
}
.service-deliverable {
  font-size: 0.74rem; color: var(--body) !important;
  padding: 0.1rem 0; display: flex; align-items: flex-start; gap: 0.4rem;
}
.service-deliverable::before { content: '✓'; color: var(--green); flex-shrink: 0; }

/* ══ TAGS ══ */
.glow-tag {
  display: inline-block;
  background: rgba(0,212,255,0.08);
  border: 1px solid rgba(0,212,255,0.3);
  color: var(--cyan) !important;
  border-radius: 6px; padding: 0.12rem 0.5rem;
  font-size: 0.68rem; font-weight: 600;
  letter-spacing: 0.05em;
  font-family: var(--mono) !important;
}
.success-tag {
  display: inline-block;
  background: rgba(57,255,20,0.08);
  border: 1px solid rgba(57,255,20,0.3);
  color: var(--green) !important;
  border-radius: 6px; padding: 0.12rem 0.5rem;
  font-size: 0.68rem; font-weight: 600;
  font-family: var(--mono) !important;
}

/* ══ RAG SIDEBAR ══ */
.rag-header {
  background: linear-gradient(135deg, var(--panel), var(--bg3));
  border: 1px solid var(--cyan); border-radius: 12px;
  padding: 0.9rem; margin-bottom: 0.75rem; text-align: center;
}
.rag-title {
  font-family: var(--mono) !important;
  color: var(--cyan) !important; font-weight: 700;
  font-size: 0.82rem; letter-spacing: 0.08em; text-transform: uppercase;
}
.rag-pulse {
  display: inline-block; width: 7px; height: 7px;
  background: var(--green); border-radius: 50%;
  animation: pulse 2s infinite; margin-right: 5px;
}
@keyframes pulse {
  0%,100% { opacity: 1; transform: scale(1); }
  50%      { opacity: 0.4; transform: scale(0.75); }
}
.chat-bubble-user {
  background: rgba(0,212,255,0.1);
  border: 1px solid rgba(0,212,255,0.3);
  border-radius: 12px 12px 4px 12px;
  padding: 0.55rem 0.85rem; font-size: 0.8rem;
  color: var(--white) !important; margin-bottom: 0.4rem;
  max-width: 90%; margin-left: auto;
}
.chat-bubble-ai {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 12px 12px 12px 4px;
  padding: 0.55rem 0.85rem; font-size: 0.8rem;
  color: var(--body) !important; margin-bottom: 0.4rem;
  max-width: 92%;
}

/* ══ REVENUE HERO ══ */
.revenue-hero {
  background: linear-gradient(135deg, #050E05 0%, #091509 50%, #050E05 100%);
  border: 1px solid rgba(57,255,20,0.2);
  border-radius: 20px; padding: 3rem 2rem;
  text-align: center; position: relative; overflow: hidden;
}
.revenue-hero::before {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(ellipse 60% 50% at 50% 0%, rgba(57,255,20,0.06), transparent);
  pointer-events: none;
}
.revenue-number {
  font-family: var(--mono) !important;
  font-size: clamp(3rem, 8vw, 5.5rem);
  font-weight: 700; color: var(--green) !important;
  line-height: 1; display: block;
  text-shadow: 0 0 40px rgba(57,255,20,0.35);
  animation: glow-pulse 3s ease-in-out infinite;
}
@keyframes glow-pulse {
  0%,100% { text-shadow: 0 0 30px rgba(57,255,20,0.3); }
  50%      { text-shadow: 0 0 70px rgba(57,255,20,0.6); }
}
.revenue-label {
  font-size: 1rem; color: var(--muted) !important; margin-top: 0.5rem;
}

/* ══ CTA ══ */
.cta-section {
  background: linear-gradient(135deg, var(--panel) 0%, #0D1827 100%);
  border: 1px solid var(--border2); border-radius: 20px;
  padding: 3rem 2rem; text-align: center;
  position: relative; overflow: hidden; margin: 2rem 0;
}
.cta-section::before {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(ellipse 70% 50% at 50% 0%, rgba(0,212,255,0.06), transparent);
  pointer-events: none;
}
.cta-btn {
  display: inline-block;
  background: linear-gradient(135deg, var(--cyan), #0099BB);
  color: #000 !important; font-weight: 800; font-size: 0.95rem;
  padding: 0.75rem 2.25rem; border-radius: 8px;
  text-decoration: none !important; letter-spacing: 0.02em;
  transition: all 0.3s ease; box-shadow: 0 6px 24px rgba(0,212,255,0.25);
  font-family: var(--sans) !important;
}
.cta-btn:hover { transform: translateY(-3px); box-shadow: 0 10px 36px rgba(0,212,255,0.45); }
.cta-btn-secondary {
  display: inline-block; background: transparent;
  border: 2px solid var(--cyan); color: var(--cyan) !important;
  font-weight: 700; font-size: 0.9rem;
  padding: 0.7rem 2rem; border-radius: 8px;
  text-decoration: none !important; transition: all 0.3s ease;
  font-family: var(--sans) !important;
}
.cta-btn-secondary:hover { background: rgba(0,212,255,0.1); transform: translateY(-2px); }

/* ══ STREAMLIT OVERRIDES ══ */
.stButton > button {
  background: linear-gradient(135deg, var(--cyan), #0099BB) !important;
  color: #000 !important; font-weight: 700 !important;
  border: none !important; border-radius: 8px !important;
  padding: 0.45rem 1.1rem !important;
  font-family: var(--sans) !important;
  transition: all 0.25s ease !important;
}
.stButton > button:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 20px rgba(0,212,255,0.3) !important;
}
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
  background: var(--panel) !important; border: 1px solid var(--border) !important;
  color: var(--body) !important; border-radius: 8px !important;
  font-family: var(--ui) !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
  border-color: var(--cyan) !important;
  box-shadow: 0 0 0 2px rgba(0,212,255,0.15) !important;
}
.stSelectbox > div > div, .stMultiSelect > div {
  background: var(--panel) !important; border: 1px solid var(--border) !important;
  border-radius: 8px !important; color: var(--body) !important;
}
.stTabs [data-baseweb="tab-list"] {
  background: var(--panel) !important; border-radius: 10px !important;
  padding: 4px !important; border: 1px solid var(--border) !important;
}
.stTabs [data-baseweb="tab"] {
  background: transparent !important; color: var(--muted) !important;
  border-radius: 7px !important; font-weight: 600 !important;
  font-family: var(--ui) !important;
}
.stTabs [aria-selected="true"] {
  background: rgba(0,212,255,0.1) !important;
  color: var(--cyan) !important;
  border: 1px solid rgba(0,212,255,0.35) !important;
}
[data-testid="stMetric"] {
  background: var(--panel) !important; border: 1px solid var(--border) !important;
  border-radius: 12px !important; padding: 0.9rem !important;
}
[data-testid="stMetricValue"] {
  color: var(--cyan) !important; font-weight: 800 !important;
  font-family: var(--mono) !important;
}
[data-testid="stMetricDelta"] { color: var(--green) !important; }
.streamlit-expanderHeader {
  background: var(--panel) !important; border: 1px solid var(--border) !important;
  border-radius: 10px !important; color: var(--white) !important;
  font-family: var(--sans) !important;
}
.streamlit-expanderContent {
  background: var(--panel) !important; border: 1px solid var(--border) !important;
  border-top: none !important; border-radius: 0 0 10px 10px !important;
}
.stProgress > div > div > div > div {
  background: linear-gradient(90deg, var(--cyan), var(--purple)) !important;
  border-radius: 4px !important;
}
hr { border-color: var(--border) !important; margin: 1.5rem 0 !important; }

/* ══ STEP CARDS ══ */
.step-card {
  background: var(--panel); border: 1px solid var(--border);
  border-radius: 12px; padding: 1rem 0.9rem;
  text-align: center; height: 100%; min-height: 155px;
  transition: border-color 0.2s;
}
.step-card:hover { border-color: var(--border2); }
.step-num {
  width: 34px; height: 34px; border-radius: 50%;
  border: 2px solid var(--cyan); background: rgba(0,212,255,0.1);
  font-family: var(--mono) !important; font-weight: 700;
  color: var(--cyan) !important; font-size: 0.85rem;
  display: flex; align-items: center; justify-content: center;
  margin: 0 auto 0.6rem;
}

/* ══ RESPONSIVE ══ */
@media (max-width: 768px) {
  .main .block-container { padding: 1rem 0.75rem 2rem !important; }
  .cyber-hero { padding: 2rem 1.25rem; }
  .hero-name { font-size: 2.2rem; }
  .kpi-grid  { grid-template-columns: repeat(2, 1fr); }
  .cert-grid { grid-template-columns: 1fr; }
}
@media (max-width: 480px) {
  .kpi-grid { grid-template-columns: 1fr 1fr; }
  .hero-badges { flex-wrap: wrap; gap: 0.4rem; }
}

/* ══ NAV CARDS (Home Page) ══ */
.nav-card {
  position: relative; border-radius: 14px;
  overflow: hidden; border: 1px solid var(--border);
  transition: all 0.3s ease; background: var(--panel);
  cursor: pointer;
}
.nav-card:hover {
  border-color: var(--border2);
  box-shadow: 0 10px 40px rgba(0,212,255,0.14);
  transform: translateY(-4px);
}
.nav-card-bg {
  height: 90px; width: 100%;
  object-fit: cover; display: block;
  filter: brightness(0.45) saturate(1.3);
  transition: filter 0.3s ease;
}
.nav-card:hover .nav-card-bg { filter: brightness(0.6) saturate(1.5); }
.nav-card-body { padding: 0.75rem 0.9rem 0.65rem; }
.nav-card-icon { font-size: 1.35rem; margin-bottom: 0.2rem; display: block; }
.nav-card-title {
  font-family: var(--sans) !important;
  font-size: 0.9rem; font-weight: 700;
  color: var(--white) !important; margin-bottom: 0.12rem;
}
.nav-card-desc { font-size: 0.67rem; color: var(--muted) !important; }

/* ══ DEMO VISUAL CARDS ══ */
.demo-visual-card {
  border-radius: 12px; overflow: hidden;
  border: 1px solid var(--border); position: relative;
  margin: 0.5rem 0;
}
.demo-visual-card img {
  width: 100%; height: 200px;
  object-fit: cover; display: block;
  filter: brightness(0.7) saturate(1.2);
}
.demo-visual-overlay {
  position: absolute; bottom: 0; left: 0; right: 0;
  background: linear-gradient(transparent, rgba(8,12,20,0.92));
  padding: 0.5rem 0.85rem 0.6rem;
}
.demo-visual-caption {
  font-family: var(--mono) !important;
  font-size: 0.68rem; color: #A8D8EA;
}

/* ══ FLOATING DOT ANIMATION ══ */
.dot-pattern {
  position: fixed; inset: 0; pointer-events: none; z-index: -1;
  background-image: radial-gradient(rgba(0,212,255,0.04) 1px, transparent 1px);
  background-size: 32px 32px;
  animation: bg-drift 60s linear infinite;
}
@keyframes bg-drift {
  0%   { background-position: 0 0; }
  100% { background-position: 320px 320px; }
}

/* ══ IMPACT BANNER ══ */
.impact-banner {
  border-radius: 16px; overflow: hidden;
  border: 1px solid var(--border); position: relative;
  margin-bottom: 1.5rem;
}
.impact-banner img {
  width: 100%; height: 200px;
  object-fit: cover; display: block;
  filter: brightness(0.55) saturate(1.3);
}
.impact-banner-overlay {
  position: absolute; bottom: 0; left: 0; right: 0;
  background: linear-gradient(transparent, rgba(8,12,20,0.9));
  padding: 1rem 1.5rem 1rem;
  display: flex; align-items: center; gap: 1rem;
}
.impact-banner-title {
  font-family: var(--mono) !important;
  font-size: 0.75rem; color: var(--cyan);
  text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}

/* ══ PAGE SECTION HERO STRIPS ══ */
.page-hero-strip {
  width: 100%; height: 120px; border-radius: 14px;
  overflow: hidden; position: relative; margin-bottom: 1.5rem;
  border: 1px solid var(--border);
}
.page-hero-strip img {
  width: 100%; height: 120px;
  object-fit: cover; display: block;
  filter: brightness(0.45) saturate(1.3);
}
.page-hero-strip-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(90deg, rgba(8,12,20,0.85) 0%, transparent 60%);
  display: flex; flex-direction: column; justify-content: center;
  padding: 0 1.75rem;
}
.page-hero-strip-title {
  font-family: var(--sans) !important;
  font-size: 1.2rem; font-weight: 700; color: var(--white);
  margin-bottom: 0.2rem;
}
.page-hero-strip-sub {
  font-family: var(--mono) !important;
  font-size: 0.68rem; color: var(--cyan);
  text-transform: uppercase; letter-spacing: 0.12em;
}
</style>
"""
