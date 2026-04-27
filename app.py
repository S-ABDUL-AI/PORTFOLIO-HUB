"""
Portfolio Hub — Sherriff Abdul-Hamid
Government Digital Services & Decision Science Portfolio
"""

import streamlit as st

st.set_page_config(
    page_title="Sherriff Abdul-Hamid — Portfolio",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── PALETTE ───────────────────────────────────────────────────
NAVY     = "#0A1F44"
NAVY_MID = "#152B5C"
GOLD     = "#C9A84C"
GOLD_LT  = "#E8C97A"
INK      = "#1A1A1A"
BODY     = "#2C3E50"
MUTED    = "#6B7280"
RULE     = "#E2E6EC"
RED      = "#C8382A"
AMBER    = "#B8560A"
GREEN    = "#1A7A2E"
OFF_WHITE= "#F8F5EE"

# ── CSS ───────────────────────────────────────────────────────
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400;700&display=swap');

    #MainMenu{{visibility:hidden;}} header{{visibility:hidden;}} footer{{visibility:hidden;}}
    .main .block-container{{padding:0!important;max-width:100%!important;}}
    body{{background:{OFF_WHITE};}}

    /* ── HERO ── */
    .hero{{
        background:linear-gradient(135deg,{NAVY} 0%,{NAVY_MID} 60%,#1A3A6E 100%);
        border-left:8px solid {GOLD};
        padding:56px 64px 48px;
        margin-bottom:0;
        position:relative;
        overflow:hidden;
    }}
    .hero::after{{
        content:'';
        position:absolute;
        top:-60px; right:-60px;
        width:320px; height:320px;
        background:{GOLD};
        opacity:0.04;
        border-radius:50%;
    }}
    .hero::before{{
        content:'';
        position:absolute;
        bottom:-80px; right:80px;
        width:200px; height:200px;
        background:{GOLD};
        opacity:0.06;
        border-radius:50%;
    }}
    .hero-eye{{
        color:{GOLD};
        font-family:'Lato',sans-serif;
        font-size:10px;
        font-weight:700;
        letter-spacing:3px;
        text-transform:uppercase;
        margin-bottom:14px;
    }}
    .hero-name{{
        color:white;
        font-family:'Playfair Display',Georgia,serif;
        font-size:44px;
        font-weight:700;
        line-height:1.1;
        margin-bottom:8px;
    }}
    .hero-title{{
        color:{GOLD_LT};
        font-family:'Lato',sans-serif;
        font-size:17px;
        font-weight:300;
        letter-spacing:0.5px;
        margin-bottom:20px;
    }}
    .hero-bio{{
        color:#CADCFC;
        font-family:'Lato',sans-serif;
        font-size:14px;
        line-height:1.7;
        max-width:720px;
        margin-bottom:28px;
    }}
    .hero-creds{{
        display:flex;
        flex-wrap:wrap;
        gap:10px;
        margin-top:4px;
    }}
    .cred-pill{{
        background:rgba(201,168,76,0.15);
        border:1px solid rgba(201,168,76,0.35);
        color:{GOLD_LT};
        font-family:'Lato',sans-serif;
        font-size:11px;
        font-weight:700;
        letter-spacing:0.8px;
        padding:5px 12px;
        border-radius:2px;
        text-transform:uppercase;
    }}

    /* ── SECTION ── */
    .section-wrap{{
        padding:48px 64px;
        background:{OFF_WHITE};
    }}
    .section-eye{{
        color:{MUTED};
        font-family:'Lato',sans-serif;
        font-size:10px;
        font-weight:700;
        letter-spacing:2.5px;
        text-transform:uppercase;
        margin-bottom:6px;
    }}
    .section-title{{
        color:{INK};
        font-family:'Playfair Display',Georgia,serif;
        font-size:28px;
        font-weight:700;
        margin-bottom:6px;
        line-height:1.2;
    }}
    .section-sub{{
        color:{MUTED};
        font-family:'Lato',sans-serif;
        font-size:13.5px;
        margin-bottom:32px;
        max-width:680px;
        line-height:1.6;
    }}
    .divider{{
        border:none;
        border-top:1px solid {RULE};
        margin:0 64px;
    }}

    /* ── FEATURED CARDS ── */
    .feat-card{{
        background:white;
        border:1px solid {RULE};
        border-top:4px solid {NAVY};
        border-radius:4px;
        padding:24px 22px 20px;
        box-shadow:0 2px 8px rgba(0,0,0,0.05);
        height:100%;
        transition:box-shadow 0.2s;
        position:relative;
    }}
    .feat-card:hover{{box-shadow:0 6px 20px rgba(0,0,0,0.10);}}
    .feat-number{{
        color:{GOLD};
        font-family:'Playfair Display',Georgia,serif;
        font-size:36px;
        font-weight:700;
        line-height:1;
        margin-bottom:10px;
        opacity:0.6;
    }}
    .feat-tag{{
        display:inline-block;
        background:{NAVY};
        color:white;
        font-family:'Lato',sans-serif;
        font-size:9px;
        font-weight:700;
        letter-spacing:1.5px;
        text-transform:uppercase;
        padding:3px 8px;
        border-radius:2px;
        margin-bottom:10px;
    }}
    .feat-title{{
        color:{INK};
        font-family:'Playfair Display',Georgia,serif;
        font-size:17px;
        font-weight:700;
        line-height:1.25;
        margin-bottom:8px;
    }}
    .feat-desc{{
        color:{MUTED};
        font-family:'Lato',sans-serif;
        font-size:12.5px;
        line-height:1.6;
        margin-bottom:16px;
    }}
    .feat-users{{
        color:{BODY};
        font-family:'Lato',sans-serif;
        font-size:11px;
        font-weight:700;
        letter-spacing:0.5px;
        margin-bottom:16px;
    }}
    .feat-link{{
        display:inline-block;
        background:{NAVY};
        color:white!important;
        font-family:'Lato',sans-serif;
        font-size:11px;
        font-weight:700;
        letter-spacing:1px;
        text-transform:uppercase;
        padding:8px 16px;
        border-radius:2px;
        text-decoration:none!important;
    }}
    .feat-link:hover{{background:{GOLD};color:{INK}!important;}}

    /* ── OTHER TOOLS ── */
    .other-section{{
        padding:40px 64px;
        background:white;
    }}
    .tool-row{{
        background:{OFF_WHITE};
        border:1px solid {RULE};
        border-left:4px solid {GOLD};
        border-radius:3px;
        padding:14px 18px;
        margin-bottom:10px;
        display:flex;
        align-items:center;
        justify-content:space-between;
    }}
    .tool-name{{
        color:{INK};
        font-family:'Lato',sans-serif;
        font-size:13.5px;
        font-weight:700;
    }}
    .tool-desc{{
        color:{MUTED};
        font-family:'Lato',sans-serif;
        font-size:12px;
        margin-top:2px;
    }}
    .tool-link{{
        color:{NAVY}!important;
        font-family:'Lato',sans-serif;
        font-size:11px;
        font-weight:700;
        letter-spacing:0.8px;
        text-transform:uppercase;
        text-decoration:none!important;
        white-space:nowrap;
        margin-left:16px;
    }}

    /* ── ABOUT STRIP ── */
    .about-strip{{
        background:{NAVY};
        border-left:8px solid {GOLD};
        padding:40px 64px;
    }}
    .about-strip-title{{
        color:white;
        font-family:'Playfair Display',Georgia,serif;
        font-size:22px;
        font-weight:700;
        margin-bottom:12px;
    }}
    .about-strip-body{{
        color:#CADCFC;
        font-family:'Lato',sans-serif;
        font-size:13.5px;
        line-height:1.7;
        max-width:760px;
        margin-bottom:20px;
    }}
    .award-row{{
        display:flex;
        flex-wrap:wrap;
        gap:8px;
        margin-top:4px;
    }}
    .award-pill{{
        background:rgba(201,168,76,0.12);
        border:1px solid rgba(201,168,76,0.3);
        color:{GOLD_LT};
        font-family:'Lato',sans-serif;
        font-size:11px;
        padding:4px 11px;
        border-radius:2px;
    }}

    /* ── CONNECT ── */
    .connect-row{{
        padding:32px 64px;
        background:{OFF_WHITE};
        border-top:1px solid {RULE};
        display:flex;
        align-items:center;
        justify-content:space-between;
        flex-wrap:wrap;
        gap:16px;
    }}
    .connect-left{{
        color:{MUTED};
        font-family:'Lato',sans-serif;
        font-size:12px;
    }}
    .connect-links{{display:flex;gap:16px;flex-wrap:wrap;}}
    .connect-link{{
        color:{NAVY}!important;
        font-family:'Lato',sans-serif;
        font-size:12px;
        font-weight:700;
        letter-spacing:0.8px;
        text-transform:uppercase;
        text-decoration:none!important;
        border-bottom:2px solid {GOLD};
        padding-bottom:2px;
    }}
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
    <div class="hero-eye">Portfolio · Government Digital Services & Decision Science</div>
    <div class="hero-name">Sherriff Abdul-Hamid</div>
    <div class="hero-title">Product Leader · Global Health Economist · Decision Scientist</div>
    <div class="hero-bio">
    I build decision-support tools that help governments, funders, and program officers
    allocate scarce resources more fairly — particularly when evidence is incomplete
    and the people affected have the least power to influence the decision.
    Over 10 years directing $200M+ in resource allocation decisions for USAID, UNDP,
    and UKAID across West Africa and the United States.
    </div>
    <div class="hero-creds">
        <span class="cred-pill">EB1-A Extraordinary Ability</span>
        <span class="cred-pill">Obama Foundation Leaders Award</span>
        <span class="cred-pill">U.S. Dept of State Fellow</span>
        <span class="cred-pill">Harvard Business School</span>
        <span class="cred-pill">USAID · UNDP · UKAID</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── FEATURED TOOLS ─────────────────────────────────────────────
st.markdown(f"""
<div class="section-wrap">
    <div class="section-eye">Featured Work</div>
    <div class="section-title">Four Tools. One Mission.</div>
    <div class="section-sub">
    Production-ready decision-support tools for SNAP program officers,
    Medicaid administrators, and global health funders.
    Each generates a downloadable McKinsey-style PDF policy report.
    </div>
</div>
""", unsafe_allow_html=True)

FEATURED = [
    {
        "n": "01",
        "tag": "Medicaid · Healthcare",
        "title": "Medicaid & Healthcare Access Risk Monitor",
        "desc": "State-level coverage risk scoring for all 50 US states. Identifies where Medicaid access pressure is highest across insurance gaps, cost burden, income, and rural reach.",
        "users": "For: State Medicaid program officers · Federal policy teams",
        "url": "https://medicaid-healthcare-access-risk-monitor-state-level-coverage-p.streamlit.app/",
        "border": RED,
    },
    {
        "n": "02",
        "tag": "SNAP · Food Security",
        "title": "Safety Net Risk Monitor",
        "desc": "Proactive SNAP and food security vulnerability targeting. Identifies communities at highest risk before they reach crisis point — with structured policy briefs and recommended actions.",
        "users": "For: SNAP outreach coordinators · State food security teams",
        "url": "https://povertyearlywarningsystem-7rrmkktbi7bwha2nna8gk7.streamlit.app/",
        "border": AMBER,
    },
    {
        "n": "03",
        "tag": "Budget · Allocation",
        "title": "Public Budget Allocation Tool",
        "desc": "Need-based government budget distribution across regions. Generates a ministerial-grade decision brief with risk flags, implication analysis, and immediate action steps.",
        "users": "For: Government program directors · Budget administrators",
        "url": "https://smart-resource-allocation-dashboard-eudzw5r2f9pbu4qyw3psez.streamlit.app/",
        "border": NAVY,
    },
    {
        "n": "04",
        "tag": "Global Health · CEA",
        "title": "GovFund Allocation Engine",
        "desc": "Cost-effectiveness decision tool for global health funders. Models cost-per-life-saved across malaria, nutrition, and social protection interventions with sensitivity analysis.",
        "users": "For: Global health funders · USAID · Gates Foundation program officers",
        "url": "https://impact-allocation-engine-ahxxrbgwmvyapwmifahk2b.streamlit.app/",
        "border": GREEN,
    },
]

cols = st.columns(4, gap="medium")
for col, app in zip(cols, FEATURED):
    with col:
        st.markdown(f"""
        <div class="feat-card" style="border-top-color:{app['border']};">
            <div class="feat-number">{app['n']}</div>
            <div class="feat-tag">{app['tag']}</div>
            <div class="feat-title">{app['title']}</div>
            <div class="feat-desc">{app['desc']}</div>
            <div class="feat-users">{app['users']}</div>
            <a href="{app['url']}" target="_blank" class="feat-link">Open Tool →</a>
        </div>
        """, unsafe_allow_html=True)

# ── DIVIDER ────────────────────────────────────────────────────
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── OTHER TOOLS ────────────────────────────────────────────────
st.markdown(f"""
<div class="other-section">
    <div class="section-eye">Additional Tools</div>
    <div class="section-title">More from the Portfolio</div>
    <div class="section-sub">Supporting tools covering global health data pipelines and supply chain optimisation.</div>
""", unsafe_allow_html=True)

OTHER_TOOLS = [
    {
        "name": "Global Vaccination Coverage Explorer",
        "desc": "WHO vaccination data across 190+ countries — automated ETL pipeline for public health program managers and researchers.",
        "url": "https://global-vaccination-coverage-explorer-6xop7p8cklrs2j3zp2ny7b.streamlit.app/",
    },
    {
        "name": "Humanitarian Procurement Optimiser",
        "desc": "Linear programming tool for logistics cost minimisation across field program supply chains.",
        "url": "https://appuctionplanningoptimizationlinearprogramming-6wd4sg3wmwesrxp.streamlit.app/",
    },
]

for tool in OTHER_TOOLS:
    st.markdown(f"""
    <div class="tool-row">
        <div>
            <div class="tool-name">{tool['name']}</div>
            <div class="tool-desc">{tool['desc']}</div>
        </div>
        <a href="{tool['url']}" target="_blank" class="tool-link">Open →</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── ABOUT STRIP ────────────────────────────────────────────────
st.markdown(f"""
<div class="about-strip">
    <div class="about-strip-title">About the Work</div>
    <div class="about-strip-body">
    Every tool in this portfolio was built to answer one question:
    <em>what do you do when evidence is incomplete, resources are limited,
    and a decision still has to be made?</em><br><br>
    I have spent a decade building frameworks for exactly that situation —
    across international development programs in West Africa, safety net
    benefits delivery in the United States, and global health funding decisions
    reaching millions of underserved people. These tools are the public-facing
    expression of that work.
    </div>
    <div class="award-row">
        <span class="award-pill">EB1-A Extraordinary Ability — USCIS, 2024</span>
        <span class="award-pill">Obama Foundation Leaders Award — Top 1.3%, 2023</span>
        <span class="award-pill">Mandela Washington Fellow — Top 0.3%, U.S. Dept of State</span>
        <span class="award-pill">Harvard Business School — Senior Executive Program</span>
        <span class="award-pill">USADF + Citibank Grant — Top 0.1% globally</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── CONNECT ────────────────────────────────────────────────────
st.markdown(f"""
<div class="connect-row">
    <div class="connect-left">
        Sherriff Abdul-Hamid · Los Angeles, CA · sherriffhamid001@gmail.com
    </div>
    <div class="connect-links">
        <a href="https://www.linkedin.com/in/abdul-hamid-sherriff-08583354/"
           target="_blank" class="connect-link">LinkedIn</a>
        <a href="mailto:sherriffhamid001@gmail.com"
           class="connect-link">Email</a>
    </div>
</div>
""", unsafe_allow_html=True)
