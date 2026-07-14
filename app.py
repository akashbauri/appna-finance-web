# app.py
"""
APPNA FINANCE - AI-Powered Financial Education Platform
Author: Senior Python Engineer, UI/UX Designer & FinTech Product Engineer
Clean Architecture - Home Page (Entrypoint)
"""

import streamlit as st
import os

# ==========================================
# 1. STREAMLIT CONFIGURATION & SETTINGS
# ==========================================
st.set_page_config(
    page_title="APPNA FINANCE | Financial Education for Everyone",
    page_icon="assets/favicon.png",  # Refinement 1: Updated page icon source
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. UI/UX CONFIGURATION & STYLING
# ==========================================
def load_custom_css():
    """Loads external stylesheet or falls back to production premium dark theme with custom styling."""
    css_path = os.path.join("styles", "custom.css")
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        # High-fidelity glassmorphism style rules targeting responsiveness and smooth transitions
        fallback_css = """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Poppins:wght@400;600;700&display=swap');
        
        /* Global & Reset Styles */
        html, body, [class*="css"], .stMarkdown {
            font-family: 'Inter', sans-serif;
            color: #F5F5F7;
        }
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            color: #F4C430 !important;
            margin-bottom: 12px;
        }
        
        /* Premium Card styling (Glassmorphism + Gold Border + Responsive Wrap) */
        .premium-card {
            background: rgba(26, 29, 36, 0.75);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(212, 175, 55, 0.15);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 24px;
            box-shadow: 0 10px 40px 0 rgba(0, 0, 0, 0.4);
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            word-wrap: break-word;
        }
        .premium-card:hover {
            transform: translateY(-5px);
            border-color: rgba(244, 196, 48, 0.4);
            box-shadow: 0 15px 45px 0 rgba(212, 175, 55, 0.08);
        }
        
        /* Premium Mini Stat Cards */
        .stat-card {
            background: linear-gradient(135deg, rgba(26, 29, 36, 0.9) 0%, rgba(18, 20, 26, 0.9) 100%);
            border: 1px solid rgba(212, 175, 55, 0.12);
            border-radius: 16px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            transition: transform 0.3s ease;
            margin-bottom: 16px;
        }
        .stat-card:hover {
            transform: translateY(-3px);
            border-color: rgba(212, 175, 55, 0.3);
        }
        .stat-value {
            font-family: 'Poppins', sans-serif;
            font-size: 2.3rem;
            font-weight: 700;
            background: linear-gradient(135deg, #F4C430 0%, #D4AF37 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
        }
        .stat-label {
            font-size: 0.85rem;
            color: rgba(245, 245, 247, 0.7);
            margin-top: 5px;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        /* Grid Cards (Services and Pillars) */
        .grid-card {
            background: rgba(26, 29, 36, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 25px;
            text-align: left;
            min-height: 180px;
            box-shadow: 0 4px 25px rgba(0,0,0,0.25);
            transition: all 0.3s ease;
            margin-bottom: 20px;
            word-wrap: break-word;
        }
        .grid-card:hover {
            background: rgba(26, 29, 36, 0.85);
            border-color: rgba(212, 175, 55, 0.25);
            transform: scale(1.02);
        }
        .grid-icon {
            font-size: 2rem;
            margin-bottom: 12px;
        }
        .grid-title {
            font-family: 'Poppins', sans-serif;
            font-size: 1.15rem;
            font-weight: 600;
            color: #FFFFFF;
            margin-bottom: 6px;
        }
        .grid-desc {
            font-size: 0.85rem;
            color: rgba(245, 245, 247, 0.65);
            line-height: 1.4;
        }

        /* Standardized Premium Gradient Buttons override for native st.button */
        div.stButton > button {
            background: linear-gradient(135deg, #D4AF37 0%, #F4C430 100%) !important;
            color: #0E1117 !important;
            font-weight: 600 !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 10px 24px !important;
            box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3) !important;
            transition: all 0.25s ease-in-out !important;
        }
        div.stButton > button:hover {
            transform: scale(1.02);
            box-shadow: 0 6px 20px rgba(244, 196, 48, 0.5) !important;
        }

        /* Responsive Pills */
        .pill-badge {
            background: rgba(212, 175, 55, 0.08); 
            border: 1px solid rgba(212, 175, 55, 0.25); 
            border-radius: 30px; 
            padding: 10px 24px; 
            font-size: 0.95rem; 
            color: #FFFFFF; 
            font-weight: 500;
            display: inline-block;
            margin: 5px;
        }

        /* Main Menu hiding to elevate product feel */
        footer {visibility: hidden;}
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        </style>
        """
        st.markdown(fallback_css, unsafe_allow_html=True)

load_custom_css()

# ==========================================
# 3. SIDEBAR BRANDING
# ==========================================
def render_sidebar_branding():
    """Renders either the high-quality assets/logo.png or clean localized fallbacks."""
    logo_path = os.path.join("assets", "logo.png")
    if os.path.exists(logo_path):
        st.sidebar.image(logo_path, use_container_width=True)
    else:
        st.sidebar.markdown(
            """
            <div style="text-align: center; padding: 25px 0px 10px 0px;">
                <h1 style="margin: 0; font-size: 1.8rem; font-weight: 700; letter-spacing: 2px; color: #FFFFFF;">APPNA</h1>
                <p style="color: #D4AF37; font-size: 0.85rem; letter-spacing: 3.5px; text-transform: uppercase; margin-top: -3px; font-weight: 500;">Finance</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.sidebar.markdown('<hr style="border-color: rgba(212, 175, 55, 0.15); margin: 10px 0px 25px 0px;" />', unsafe_allow_html=True)
    
    # Refinement 2: Updated Sidebar Copy to match the new, highly professional design goals
    st.sidebar.markdown(
        """
        <div style="padding: 0 5px;">
            <p style="font-weight: 600; color: #FFFFFF; margin-bottom: 4px; font-size: 1rem;">Welcome to APPNA FINANCE</p>
            <p style="color: #D4AF37; font-size: 0.8rem; margin-bottom: 12px; font-weight: 500;">AI Powered Financial Education Platform</p>
            <p style="color: rgba(245, 245, 247, 0.75); font-size: 0.85rem; line-height: 1.4; margin-bottom: 16px;">Helping Every Indian Learn Finance.</p>
            <p style="color: rgba(245, 245, 247, 0.5); font-size: 0.8rem; font-style: italic;">Choose a page from the sidebar.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

render_sidebar_branding()

# ==========================================
# 4. HOME PAGE SECTIONS
# ==========================================

# 4.1 HERO SECTION
def render_hero_section():
    st.markdown(
        """
        <div class="premium-card" style="text-align: center; padding: 65px 20px; background: radial-gradient(circle at top right, rgba(212,175,55,0.08) 0%, rgba(26,29,36,0.85) 80%);">
            <h1 style="font-size: 3.2rem; font-weight: 700; margin-bottom: 5px; color: #FFFFFF !important; letter-spacing: 1px;">APPNA FINANCE</h1>
            <h2 style="font-size: 1.4rem; font-weight: 400; color: #D4AF37 !important; margin-bottom: 15px; letter-spacing: 2px; text-transform: uppercase;">AI Powered Financial Education Platform</h2>
            <div style="font-size: 1.15rem; font-weight: 600; color: rgba(245,245,247,0.9); margin-bottom: 15px; word-spacing: 5px;">Learn • Grow • Prosper</div>
            <p style="font-size: 1rem; color: rgba(245,245,247,0.65); max-width: 700px; margin: 0 auto; line-height: 1.6;">
                Making Financial Knowledge Simple, Trustworthy, and Accessible for Every Indian. Start navigating your educational journey with smart, localized technology.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Hero Call-To-Actions
    btn_col1, btn_col2, _ = st.columns([1.5, 1.5, 3])
    with btn_col1:
        if st.button("🚀 Start Learning", key="hero_start_btn", use_container_width=True):
            # TODO: Add dynamic tracking or direct interaction logic
            st.toast("💡 Visit the '2 Learning Hub' page in the sidebar to get started!", icon="🎓")
    with btn_col2:
        if st.button("📖 Learning Hub", key="hero_hub_btn", use_container_width=True):
            # TODO: Add dynamic tracking or direct interaction logic
            st.toast("💡 Access the full program catalog from '2 Learning Hub' in the sidebar.", icon="🎓")

render_hero_section()
st.markdown("<br>", unsafe_allow_html=True)


# 4.2 STATISTICS
def render_statistics_section():
    st.markdown("### 📊 Platform Scalability")
    col1, col2, col3, col4 = st.columns(4)
    
    stats = [
        {"val": "50+", "label": "Financial Topics"},
        {"val": "3", "label": "Languages (EN, HI, BN)"},
        {"val": "24/7", "label": "AI Learning"},
        {"val": "100%", "label": "Free Education"}
    ]
    
    cols = [col1, col2, col3, col4]
    for idx, stat in enumerate(stats):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="stat-card">
                    <div class="stat-value">{stat['val']}</div>
                    <div class="stat-label">{stat['label']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

render_statistics_section()
st.markdown("<br>", unsafe_allow_html=True)


# 4.3 SERVICE CARDS
def render_service_cards():
    st.markdown("### 🛠️ Core Offerings")
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    
    services = [
        {"icon": "🤖", "title": "AI Assistant", "desc": "Contextual AI-driven answers to clarify complex financial terms and calculation metrics."},
        {"icon": "🏦", "title": "Banking", "desc": "Demystify compound savings accounts, modern deposit frameworks, and localized banking services."},
        {"icon": "📈", "title": "Stock Market", "desc": "Learn the essentials of equities, compounding mechanisms, indices, and disciplined strategies."},
        {"icon": "💳", "title": "Loans", "desc": "A direct guide explaining compound interest systems, EMIs, and sustainable debt management rules."},
        {"icon": "🛡️", "title": "Insurance", "desc": "Clear breakdowns of crop, life, and health insurance layouts keeping families fully prepared."},
        {"icon": "🎓", "title": "Learning Hub", "desc": "Structured educational pathways designed specifically for students, MSMEs, and rural families."}
    ]
    
    all_cols = [col1, col2, col3, col4, col5, col6]
    for idx, srv in enumerate(services):
        with all_cols[idx]:
            st.markdown(
                f"""
                <div class="grid-card">
                    <div class="grid-icon">{srv['icon']}</div>
                    <div class="grid-title">{srv['title']}</div>
                    <div class="grid-desc">{srv['desc']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

render_service_cards()
st.markdown("<br>", unsafe_allow_html=True)


# 4.4 WHY APPNA FINANCE
def render_why_appna_section():
    st.markdown("### ✨ Why APPNA FINANCE")
    col1, col2, col3 = st.columns(3)
    
    reasons = [
        {"title": "🧠 Financial Education", "desc": "Structured modules targeting long-term financial concepts without complicated financial jargon."},
        {"title": "⚡ AI-Powered Learning", "desc": "Get tailored guidance generated dynamically based on your questions, regional scenarios, and local goals."},
        {"title": "🗣️ Multilingual Support", "desc": "Breaking down systemic language barriers by offering training options across English, Hindi, and Bengali."}
    ]
    
    cols = [col1, col2, col3]
    for idx, rsn in enumerate(reasons):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="premium-card">
                    <h4 style="color:#D4AF37 !important;">{rsn['title']}</h4>
                    <p style="font-size:0.9rem; color:rgba(245,245,247,0.7); line-height:1.5; margin: 0;">{rsn['desc']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

render_why_appna_section()
st.markdown("<br>", unsafe_allow_html=True)


# 4.5 WHO WE SERVE
def render_who_we_serve():
    st.markdown("### 🤝 Who We Serve")
    st.markdown(
        """
        <div style="margin-bottom: 25px;">
            <span class="pill-badge">🎓 Students</span>
            <span class="pill-badge">🚜 Farmers</span>
            <span class="pill-badge">👔 Professionals</span>
            <span class="pill-badge">🏢 MSMEs</span>
            <span class="pill-badge">🏠 Families</span>
            <span class="pill-badge">🌱 First Time Investors</span>
        </div>
        """,
        unsafe_allow_html=True
    )

render_who_we_serve()


# 4.6 FINANCIAL CATEGORIES
def render_financial_categories():
    st.markdown("### 🗂️ Financial Categories")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    categories = [
        "🏦 Banking", 
        "📊 Stock Market", 
        "📈 Personal Finance", 
        "🛡️ Insurance", 
        "💸 Loans", 
        "🏛️ Govt Schemes"
    ]
    
    cols = [col1, col2, col3, col4, col5, col6]
    for idx, cat in enumerate(categories):
        with cols[idx]:
            st.markdown(
                f"<div class='grid-card' style='min-height:90px; text-align:center; padding: 20px 10px;'>{cat}</div>", 
                unsafe_allow_html=True
            )

render_financial_categories()
st.markdown("<br>", unsafe_allow_html=True)


# 4.7 LEARNING HUB PREVIEW
def render_learning_hub_preview():
    st.markdown("### 🎬 Learning Hub Preview")
    
    st.markdown(
        """
        <div class="premium-card" style="padding: 0px; overflow: hidden; background: #12141a;">
            <div style="background: linear-gradient(180deg, rgba(14,17,23,0) 40%, rgba(14,17,23,0.95) 95%), rgba(212, 175, 55, 0.05); height: 280px; display: flex; flex-direction: column; justify-content: flex-end; padding: 40px;">
                <span style="background: #D4AF37; color: #0E1117; font-size: 0.75rem; font-weight:700; border-radius: 4px; padding: 4px 8px; width: fit-content; margin-bottom: 12px; letter-spacing: 1px; text-transform: uppercase;">LEARN ON DEMAND</span>
                <h2 style="color: #FFFFFF !important; font-size: 2rem; margin: 0 0 8px 0;">Learn Finance with APPNA FINANCE</h2>
                <p style="color: rgba(245,245,247,0.7); margin: 0; font-size: 1rem; max-width: 700px;">
                    Explore topics like Banking, Stock Market, Personal Finance, Insurance, Government Schemes, Mutual Funds, Business Finance, and MSME solutions.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    btn_col, _ = st.columns([2, 4])
    with btn_col:
        # Refinement 3: Updated button label to "📺 Explore Learning Hub"
        if st.button("📺 Explore Learning Hub", key="visit_hub_action"):
            # TODO: Connect FastAPI tracking backend integration here to log user clicks
            # Example: requests.post("https://api.appnafinance.com/analytics/clicks", json={"element": "hub_preview_button"})
            st.toast("💡 Check the '2 Learning Hub' page in the sidebar!", icon="🎓")

render_learning_hub_preview()
st.markdown("<br>", unsafe_allow_html=True)


# 4.8 FOUNDER SPOTLIGHT
def render_founder_spotlight():
    st.markdown("### 👑 Founder Spotlight")
    
    # Refinement 4: Replaced robotic quote with your authentic voice
    authentic_quote = (
        '"Our mission is to make financial knowledge simple, trustworthy, and accessible '
        'so that every Indian can make better financial decisions with confidence."'
    )
    
    st.markdown(
        f"""
        <div class="premium-card" style="background: radial-gradient(circle at bottom left, rgba(212,175,55,0.06) 0%, rgba(26,29,36,0.85) 100%);">
            <h2 style="margin:0 0 5px 0; color:#FFFFFF !important;">Akash Bauri</h2>
            <h4 style="color:#D4AF37 !important; margin:0 0 15px 0; font-weight: 400; letter-spacing: 1.5px; text-transform: uppercase; font-size: 0.9rem;">Founder, CEO & Founding AI Engineer</h4>
            <p style="font-size:1.1rem; color:rgba(245,245,247,0.85); line-height:1.6; font-style: italic; margin-bottom: 25px;">
                {authentic_quote}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    btn_col, _ = st.columns([1.5, 4.5])
    with btn_col:
        if st.button("Learn More", key="founder_more_action"):
            # TODO: Connect analytical logging or dynamic redirection to '3 About APPNA FINANCE'
            st.toast("💡 Visit the '3 About APPNA FINANCE' page in the sidebar!", icon="👑")

render_founder_spotlight()
st.markdown("<br>", unsafe_allow_html=True)


# 4.9 MISSION PREVIEW
def render_mission_preview():
    st.markdown("### 🎯 Mission Preview")
    st.markdown(
        """
        <div class="premium-card" style="text-align: center; border-left: 5px solid #D4AF37;">
            <p style="font-family: 'Poppins', sans-serif; font-size: 1.3rem; font-style: italic; color: #FFFFFF; max-width: 850px; margin: 0 auto;">
                "Making Financial Knowledge Simple, Trustworthy and Accessible for Every Indian."
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    btn_col, _ = st.columns([1.5, 4.5])
    with btn_col:
        if st.button("Read More", key="mission_more_action"):
            # TODO: Connect tracker or routing helper here
            st.toast("💡 Explore the '3 About APPNA FINANCE' page in the sidebar!", icon="🎯")

render_mission_preview()
st.markdown("<br>", unsafe_allow_html=True)


# 4.10 FOOTER
def render_footer():
    st.markdown(
        """
        <hr style="border-color: rgba(212, 175, 55, 0.15); margin: 40px 0px 20px 0px;" />
        <div style="text-align: center; padding: 20px 0px 50px 0px;">
            <h2 style="margin: 0; font-size: 1.5rem; letter-spacing: 2px; font-weight:700;">🎓 APPNA FINANCE</h2>
            <div style="color: #D4AF37; font-size: 0.8rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 15px;">Learn • Grow • Prosper</div>
            <p style="color: rgba(245, 245, 247, 0.5); font-size: 0.85rem; max-width: 650px; margin: 0 auto 15px auto; line-height: 1.5;">
                APPNA FINANCE is an AI-powered financial education platform dedicated to making financial knowledge simple, trustworthy, and accessible for every Indian.
            </p>
            <p style="color: rgba(245, 245, 247, 0.3); font-size: 0.75rem;">
                &copy; 2026 APPNA FINANCE System. All Rights Reserved.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

render_footer()
