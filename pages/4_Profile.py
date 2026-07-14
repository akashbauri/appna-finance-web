"""
APPNA FINANCE - Profile Page
Filename: pages/4_Profile.py
Role: Senior UI/UX Designer & FinTech Architect
Design Language: Luxury Black & Metallic Gold Glassmorphism (Mapped to styles/custom.css)
"""

import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Profile | APPNA FINANCE",
    page_icon="assets/favicon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SIDEBAR CONFIGURATION ---
with st.sidebar:
    if os.path.exists("assets/logo.png"):
        st.image("assets/logo.png", width=170)
    else:
        st.warning("Logo not found")
    
    st.markdown("### APPNA FINANCE")
    st.markdown("👤 **Profile Page**")
    st.markdown("---")
    
    st.info("💡 Status: Frontend MVP (Backend Integration Coming Soon)")
    
    st.markdown("**Future Features**")
    st.markdown(
        """
        - 🔐 Supabase Authentication
        - 🔑 Google Login
        - 🧠 AI Personalization
        - 💬 Chat History
        - 📚 Saved Learning
        """
    )
    st.markdown("---")
    st.markdown("<small>Created with ❤️ for a financially literate India.</small>", unsafe_allow_html=True)


# --- MAIN HEADER ---
st.markdown(
    """
    <div class="hero-container">
        <h1>👤 My Profile</h1>
        <p style="color: #D4AF37; font-size: 1.2rem; font-weight: 600; margin-top: -0.5rem; letter-spacing: 0.05em;">
            Manage your APPNA FINANCE account and learning journey.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("<br/>", unsafe_allow_html=True)


# --- PROFILE SECTION (TWO COLUMNS) ---
profile_cols = st.columns([1, 3])

with profile_cols[0]:
    avatar_path = "assets/team/akash_bauri.png"
    if os.path.exists(avatar_path):
        st.image(avatar_path, width=250)
    else:
        st.warning("User avatar image not found.")

with profile_cols[1]:
    st.markdown(
        """
        <div class="premium-card" style="border: 1px solid rgba(212, 175, 55, 0.25); background: rgba(26, 29, 36, 0.95); height: 100%; display: flex; flex-direction: column; justify-content: center; padding: 1.5rem !important;">
            <h2 style="color: #D4AF37; margin: 0; font-size: 2rem;">Akash Bauri</h2>
            <p style="color: #FFFFFF; font-weight: 600; font-size: 1.1rem; margin: 0.25rem 0 0 0;">Founder, CEO & Founding AI Engineer</p>
            <div style="margin-top: 1rem; display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem;">
                <div><span style="color: #808080; font-size: 0.9rem;">Membership:</span> <strong style="color: #D4AF37;">Founder Account</strong></div>
                <div><span style="color: #808080; font-size: 0.9rem;">Status:</span> <span style="color: #55D437; font-weight: 600;">Frontend MVP</span></div>
                <div><span style="color: #808080; font-size: 0.9rem;">Backend:</span> <span style="color: #FFA500; font-weight: 600;">Coming Soon</span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br/>", unsafe_allow_html=True)


# --- INFO & STATUS CARDS ---
info_cols = st.columns(2)

with info_cols[0]:
    st.markdown(
        """
        <div class="grid-card" style="min-height: 250px;">
            <h4 style="color: #D4AF37; margin-top: 0;">📋 Personal Information</h4>
            <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem; color: #B0B0B0; font-size: 0.95rem;">
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding: 6px 0; color: #808080;">Full Name</td><td style="color: #FFF; font-weight: 500;">Akash Bauri</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding: 6px 0; color: #808080;">Email</td><td style="font-style: italic;">Coming Soon</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding: 6px 0; color: #808080;">Phone</td><td style="font-style: italic;">Coming Soon</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding: 6px 0; color: #808080;">State</td><td style="color: #FFF;">Jharkhand</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding: 6px 0; color: #808080;">District</td><td style="color: #FFF;">Dhanbad</td></tr>
                <tr><td style="padding: 6px 0; color: #808080;">Preferred Language</td><td style="color: #D4AF37; font-weight: 500;">English</td></tr>
            </table>
        </div>
        """,
        unsafe_allow_html=True
    )

with info_cols[1]:
    st.markdown(
        """
        <div class="grid-card" style="min-height: 250px;">
            <h4 style="color: #D4AF37; margin-top: 0;">🛡️ Account & Integration Status</h4>
            <ul style="list-style: none; padding-left: 0; margin-top: 0.75rem; line-height: 1.8; color: #B0B0B0; font-size: 0.95rem;">
                <li style="margin-bottom: 0.4rem;">🟢 <strong style="color: #55D437;">Frontend Ready</strong> - Premium UI Complete</li>
                <li style="margin-bottom: 0.4rem;">⏳ <strong>Supabase Authentication</strong> - Integration Pending</li>
                <li style="margin-bottom: 0.4rem;">⏳ <strong>Google Login</strong> - OAuth Protocol Setup Next</li>
                <li style="margin-bottom: 0.4rem;">⏳ <strong>FastAPI Backend</strong> - Architecture Mapping Complete</li>
                <li>⏳ <strong>AI Chat History</strong> - Persisted RAG Logging Next</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )


# --- LEARNING PROGRESS LOGIC ---
st.markdown("---")
st.markdown("### 📈 Learning Progress")

metric_cols = st.columns(4)
with metric_cols[0]:
    st.metric(label="Financial Lessons", value="24", delta="Demo Account")
with metric_cols[1]:
    st.metric(label="AI Conversations", value="0", delta="Awaiting Backend")
with metric_cols[2]:
    st.metric(label="Videos Watched", value="12", delta="Active Learner")
with metric_cols[3]:
    st.metric(label="Knowledge Score", value="92%", delta="+5% this week")


# --- ACHIEVEMENTS SECTION ---
st.markdown("<br/>", unsafe_allow_html=True)
st.markdown("### 🏅 Achievements")

achieve_cols = st.columns(4)

achievements = [
    ("🏆 Early Supporter", "Granted to founding contributors exploring the alpha builds."),
    ("🤖 AI Explorer", "Ready to query the intelligent engine across multilingual concepts."),
    ("📚 Finance Learner", "Consistently engaging with courses, video models, and tax rules."),
    ("🚀 APPNA Founder", "Core system developer credentials enabled on this workspace profile.")
]

for idx, (title, desc) in enumerate(achievements):
    with achieve_cols[idx]:
        st.markdown(
            f"""
            <div class="grid-card" style="min-height: 120px; text-align: center; border: 1px solid rgba(212, 175, 55, 0.15);">
                <div style="color: #D4AF37; font-size: 1.1rem; font-weight: bold;">{title}</div>
                <div style="color: #808080; font-size: 0.85rem; margin-top: 0.4rem; line-height: 1.4;">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- SETTINGS SECTION ---
st.markdown("---")
st.markdown("### ⚙️ Settings")

settings_cols = st.columns(2)

with settings_cols[0]:
    st.selectbox(
        "Preferred Interface Language",
        options=["English", "Hindi", "Bengali"],
        index=0,
        disabled=True,
        help="Backend configuration locked in Frontend MVP stage."
    )
    st.checkbox("Enable Push & Email Notifications", value=False, disabled=True)

with settings_cols[1]:
    st.checkbox("Force High-Contrast Dark Theme (Glassmorphism)", value=True, disabled=True)
    st.checkbox("Enable Personalized AI Recommendations", value=False, disabled=True)


# --- UPCOMING FEATURES SECTION ---
st.markdown("---")
st.markdown("### 🔮 Upcoming Core Engine Enhancements")

upcoming_cols = st.columns(4)

features = [
    ("💬 Chat History", "Access, export, and review your previous conversations and technical dynamic roadmaps natively."),
    ("📝 Saved Notes", "Bookmark key financial terms, personalized tax summaries, and study models effortlessly."),
    ("🎥 Saved Videos", "Keep a tailored watch list of educational finance shorts and modules handy."),
    ("🎙️ Voice Assistant", "Ask questions naturally using audio streaming inputs configured for regional accents."),
    ("📊 Financial Reports", "Generate personalized financial charts based on your mock portfolio practice sessions."),
    ("🧠 Personalized Learning", "AI dynamically optimizes study sequences matching your operational sector."),
    ("🤖 AI Recommendations", "Proactive delivery of relevant welfare updates or financial guidelines automatically."),
    ("🔒 Secure Vault", "Encrypt sensitive practice entries dynamically mapped under isolated user states.")
]

for idx, (title, desc) in enumerate(features):
    col_idx = idx % 4
    with upcoming_cols[col_idx]:
        st.markdown(
            f"""
            <div class="grid-card" style="min-height: 140px; margin-bottom: 1rem;">
                <div style="color: #D4AF37; font-size: 1.05rem; font-weight: 600;">✨ {title}</div>
                <div style="color: #808080; font-size: 0.85rem; margin-top: 0.35rem; line-height: 1.4;">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- CUSTOM FOOTER ---
st.markdown("<br/><br/>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="custom-footer">
        <h4>APPNA FINANCE</h4>
        <p style="color: #D4AF37; margin-bottom: 0.75rem; font-weight: 500; letter-spacing: 0.15em;">
            LEARN • GROW • PROSPER
        </p>
        <p style="font-size: 0.85rem; color: #808080;">
            AI Powered Financial Education Platform<br/>
            Copyright © 2026 APPNA FINANCE. All rights reserved.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
