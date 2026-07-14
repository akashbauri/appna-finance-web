"""
APPNA FINANCE - Financial Learning Hub Page
Filename: pages/2_Learning_Hub.py
Role: Senior Streamlit UI/UX & EdTech Product Architect
Design Language: Luxury Black & Metallic Gold Glassmorphism (Mapped to styles/custom.css)
"""

import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Learning Hub | APPNA FINANCE",
    page_icon="📺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SIDEBAR CONFIGURATION ---
with st.sidebar:
    st.markdown("### APPNA FINANCE")
    st.markdown("📺 **Learning Hub**")
    st.markdown("---")
    
    st.info("💡 Status: FRONTEND DEMO")
    
    st.markdown("**Future Integrations**")
    st.markdown(
        """
        - 🔗 YouTube Data API v3
        - ☁️ Google Cloud Vertex AI
        - 🤖 Personalized AI Recommendations
        - 📈 User Progress & Badges Tracking
        """
    )
    st.markdown("---")
    st.markdown("<small>Simplifying finance for every Indian.</small>", unsafe_allow_html=True)


# --- 1. HERO SECTION ---
st.markdown(
    """
    <div class="hero-container">
        <h1>📺 Learning Hub</h1>
        <p style="color: #D4AF37; font-size: 1.3rem; font-weight: 600; margin-top: -0.5rem; letter-spacing: 0.05em;">
            Learn Finance Visually with APPNA FINANCE
        </p>
        <p style="color: #B0B0B0; font-size: 1.05rem; max-width: 800px; margin: 0.5rem auto 1.5rem auto; line-height: 1.6;">
            Welcome to the official APPNA FINANCE Learning Hub. Learn Banking, Stock Market, 
            Personal Finance, Government Schemes, and Business Finance through simple, 
            beginner-friendly educational videos.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Hero Call-to-Action Buttons
hero_btn_cols = st.columns([1, 1, 1, 1])
with hero_btn_cols[1]:
    # TODO: Add dynamic anchor scroll to Learning Categories section
    st.button("▶ Explore Topics", use_container_width=True, type="primary")
with hero_btn_cols[2]:
    # TODO: Implement redirect click-tracking telemetry
    st.link_button(
        "📺 Visit YouTube Channel", 
        "https://youtube.com/@akashlearninghub-m7n", 
        use_container_width=True
    )


# --- 2. WHY LEARN WITH APPNA FINANCE ---
st.markdown("<br/>", unsafe_allow_html=True)
st.markdown("### 🌟 Why Learn with APPNA FINANCE?")

why_cols = st.columns(4)

why_data = [
    ("📚 Beginner Friendly", "Simple Explanations", "Demystifying complex terminology into simple, everyday language that anyone can easily follow."),
    ("🏦 Practical Finance", "Real-world Examples", "No dry theory. Learn with practical real-life case studies, calculation steps, and realistic scenarios."),
    ("🤖 AI Powered", "Smart Learning", "Complement your video watching experience with real-time interactive AI chats and tailored conceptual breakdowns."),
    ("🌍 Multilingual", "Regional Reach", "Breaking linguistic barriers. Highly specialized finance modules explained clearly in English, Hindi, and Bengali.")
]

for idx, (title, subtitle, desc) in enumerate(why_data):
    with why_cols[idx]:
        st.markdown(
            f"""
            <div class="grid-card" style="min-height: 190px;">
                <div class="stat-label" style="color: #D4AF37; font-size: 1.05rem; font-weight: 600;">{title}</div>
                <div style="color: #FFFFFF; font-size: 0.9rem; font-weight: 500; margin-top: 0.25rem;">{subtitle}</div>
                <div style="color: #808080; font-size: 0.85rem; margin-top: 0.5rem; line-height: 1.5;">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- 3. LEARNING CATEGORIES ---
st.markdown("---")
st.markdown("<h3 id='categories'>🗂️ Core Financial Pillars</h3>", unsafe_allow_html=True)
st.write("Browse through our carefully structured pathways designed to take you from beginner to financially confident.")

# Define categories and their topics
categories = {
    "🏦 Banking": [
        "Savings Account", "Current Account", "Fixed Deposits (FD)", "Recurring Deposits (RD)",
        "Unified Payments Interface (UPI)", "Debit Cards vs. Credit Cards", "Internet Banking Basics",
        "Mobile Banking Safety", "Financial Fraud Awareness"
    ],
    "📈 Stock Market": [
        "Stock Market Basics", "NSE & BSE Exchanges", "Initial Public Offerings (IPO)",
        "Mutual Funds Explainer", "Systematic Investment Plans (SIP)", "Risk Management Techniques",
        "Portfolio Diversification", "Long-Term Value Investing"
    ],
    "💰 Personal Finance": [
        "Zero-Based Budgeting", "Smart Saving Strategies", "Building Emergency Funds",
        "Life & Health Insurance", "Tax Planning (Old vs. New)", "Defining Smart Financial Goals",
        "Early Retirement Planning"
    ],
    "💼 Business Finance": [
        "Understanding MSMEs", "Securing Business Loans", "Strategic Government Schemes",
        "Startup Seed Capital", "Fundamentals of Entrepreneurship", "Drafting a Bulletproof Business Plan"
    ],
    "🌾 Agriculture Finance": [
        "Kisan Credit Card (KCC)", "Agriculture & Crop Loans", "Pradhan Mantri Fasal Bima",
        "Government Subsidies & Schemes"
    ]
}

# Layout pillars using custom grid structures
cat_cols = st.columns(3)

# First Row of Pillars
with cat_cols[0]:
    st.markdown(
        f"""
        <div class="grid-card" style="min-height: 380px; display: flex; flex-direction: column;">
            <div class="stat-label" style="color: #D4AF37; font-size: 1.2rem; font-weight: bold; margin-bottom: 0.75rem;">🏦 Banking</div>
            <div style="color: #E0E0E0; font-size: 0.9rem; line-height: 1.8;">
                {"<br/>".join([f"• {topic}" for topic in categories["🏦 Banking"]])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    # TODO: Add dynamic progress indicators for completed sub-topics

with cat_cols[1]:
    st.markdown(
        f"""
        <div class="grid-card" style="min-height: 380px; display: flex; flex-direction: column;">
            <div class="stat-label" style="color: #D4AF37; font-size: 1.2rem; font-weight: bold; margin-bottom: 0.75rem;">📈 Stock Market</div>
            <div style="color: #E0E0E0; font-size: 0.9rem; line-height: 1.8;">
                {"<br/>".join([f"• {topic}" for topic in categories["📈 Stock Market"]])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with cat_cols[2]:
    st.markdown(
        f"""
        <div class="grid-card" style="min-height: 380px; display: flex; flex-direction: column;">
            <div class="stat-label" style="color: #D4AF37; font-size: 1.2rem; font-weight: bold; margin-bottom: 0.75rem;">💰 Personal Finance</div>
            <div style="color: #E0E0E0; font-size: 0.9rem; line-height: 1.8;">
                {"<br/>".join([f"• {topic}" for topic in categories["💰 Personal Finance"]])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Second Row of Pillars
st.markdown("<br/>", unsafe_allow_html=True)
cat_cols_bottom = st.columns(2)

with cat_cols_bottom[0]:
    st.markdown(
        f"""
        <div class="grid-card" style="min-height: 280px; display: flex; flex-direction: column;">
            <div class="stat-label" style="color: #D4AF37; font-size: 1.2rem; font-weight: bold; margin-bottom: 0.75rem;">💼 Business Finance</div>
            <div style="color: #E0E0E0; font-size: 0.9rem; line-height: 1.8;">
                {"<br/>".join([f"• {topic}" for topic in categories["💼 Business Finance"]])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with cat_cols_bottom[1]:
    st.markdown(
        f"""
        <div class="grid-card" style="min-height: 280px; display: flex; flex-direction: column;">
            <div class="stat-label" style="color: #D4AF37; font-size: 1.2rem; font-weight: bold; margin-bottom: 0.75rem;">🌾 Agriculture Finance</div>
            <div style="color: #E0E0E0; font-size: 0.9rem; line-height: 1.8;">
                {"<br/>".join([f"• {topic}" for topic in categories["🌾 Agriculture Finance"]])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# --- 4. LEARNING ROADMAP ---
st.markdown("---")
st.markdown("### 🗺️ Recommended Roadmap")
st.write("Follow this structured milestone timeline to progressively elevate your financial intelligence.")

# Premium Interactive Learning Timeline
st.markdown(
    """
    <div style="margin-top: 1.5rem;">
        <div style="border-left: 3px solid #D4AF37; margin-left: 20px; padding-left: 30px; position: relative; margin-bottom: 2rem;">
            <div style="position: absolute; left: -11px; top: 0; background: #D4AF37; width: 20px; height: 20px; border-radius: 50%;"></div>
            <strong style="color: #D4AF37; font-size: 1.15rem;">Step 1: Learn Banking</strong>
            <p style="color: #B0B0B0; margin: 0.25rem 0 0 0; font-size: 0.95rem;">Understand daily transactions, accounts, UPI, safe digital habits, and bank integrations.</p>
        </div>
        <div style="border-left: 3px solid #D4AF37; margin-left: 20px; padding-left: 30px; position: relative; margin-bottom: 2rem;">
            <div style="position: absolute; left: -11px; top: 0; background: #D4AF37; width: 20px; height: 20px; border-radius: 50%;"></div>
            <strong style="color: #D4AF37; font-size: 1.15rem;">Step 2: Understand Personal Finance</strong>
            <p style="color: #B0B0B0; margin: 0.25rem 0 0 0; font-size: 0.95rem;">Master the art of budgeting, dynamic saving, taking the right insurance, and emergency shield creation.</p>
        </div>
        <div style="border-left: 3px solid #D4AF37; margin-left: 20px; padding-left: 30px; position: relative; margin-bottom: 2rem;">
            <div style="position: absolute; left: -11px; top: 0; background: #D4AF37; width: 20px; height: 20px; border-radius: 50%;"></div>
            <strong style="color: #D4AF37; font-size: 1.15rem;">Step 3: Learn Stock Market</strong>
            <p style="color: #B0B0B0; margin: 0.25rem 0 0 0; font-size: 0.95rem;">Get comfortable with stock indices, shares, and understanding equity instruments securely.</p>
        </div>
        <div style="border-left: 3px solid #D4AF37; margin-left: 20px; padding-left: 30px; position: relative; margin-bottom: 2rem;">
            <div style="position: absolute; left: -11px; top: 0; background: #D4AF37; width: 20px; height: 20px; border-radius: 50%;"></div>
            <strong style="color: #D4AF37; font-size: 1.15rem;">Step 4: Understand Investments</strong>
            <p style="color: #B0B0B0; margin: 0.25rem 0 0 0; font-size: 0.95rem;">Explore mutual funds, Systematic Investment Plans (SIP), asset allocation, and balanced risk profiles.</p>
        </div>
        <div style="border-left: 3px solid #D4AF37; margin-left: 20px; padding-left: 30px; position: relative; margin-bottom: 1rem;">
            <div style="position: absolute; left: -11px; top: 0; background: #D4AF37; width: 20px; height: 20px; border-radius: 50%;"></div>
            <strong style="color: #D4AF37; font-size: 1.15rem;">Step 5: Build Long-Term Wealth</strong>
            <p style="color: #B0B0B0; margin: 0.25rem 0 0 0; font-size: 0.95rem;">Deploy modern compounding portfolios, optimize taxes, and map strategies for long-term goals.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# --- 5. OFFICIAL YOUTUBE CHANNEL ---
st.markdown("---")
st.markdown("### 🎥 Primary Media Resource")

# Large Premium Card
st.markdown(
    """
    <div class="premium-card" style="border: 1px solid rgba(212, 175, 55, 0.3); background: rgba(26, 29, 36, 0.95);">
        <div style="display: flex; align-items: center; gap: 15px;">
            <div style="font-size: 2.5rem;">📺</div>
            <div>
                <h4 style="color: #D4AF37; margin: 0;">Official APPNA FINANCE Learning Hub</h4>
                <p style="color: #FFFFFF; margin: 0.25rem 0 0 0; font-size: 1rem;">
                    Watch beginner-friendly financial education videos designed strictly to match modern Indian market scenarios.
                </p>
                <p style="color: #808080; margin: 0.15rem 0 0 0; font-size: 0.85rem;">
                    Channel Handle: <strong style="color: #FFFFFF;">@akashlearninghub-m7n</strong>
                </p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br/>", unsafe_allow_html=True)
yt_cols = st.columns([1, 2, 1])
with yt_cols[1]:
    # TODO: Connect YouTube Analytics tracking database to monitor referral conversions
    st.link_button(
        "▶ Visit Official YouTube Channel",
        "https://youtube.com/@akashlearninghub-m7n",
        use_container_width=True,
        type="primary"
    )


# --- 6. WHAT YOU WILL LEARN ---
st.markdown("---")
st.markdown("### 🏷️ What You Will Learn")

pill_items = [
    "Banking", "Stock Market", "Mutual Funds", "Insurance", "Government Schemes", 
    "Loans", "Business Finance", "Personal Finance", "Investment Basics", 
    "Digital Payments", "Financial Planning", "AI Finance"
]

pill_html = "<div style='margin-bottom: 1.5rem; display: flex; flex-wrap: wrap; gap: 8px;'>"
for item in pill_items:
    pill_html += f'<span class="pill-badge" style="cursor: default;">{item}</span>'
pill_html += "</div>"
st.markdown(pill_html, unsafe_allow_html=True)


# --- 7. WHY THIS MATTERS ---
st.markdown(
    """
    <div class="premium-card" style="border-left: 4px solid #D4AF37; background: rgba(26, 29, 36, 0.85);">
        <h5 style="color: #D4AF37; margin-top: 0; margin-bottom: 0.5rem; font-size: 1.1rem; font-weight: bold;">
            🎓 Financial Education for Every Indian
        </h5>
        <p style="color: #E0E0E0; font-size: 0.95rem; line-height: 1.6; margin: 0;">
            APPNA FINANCE believes financial education should be simple, trustworthy, multilingual, and accessible. 
            Our mission is to help students, farmers, professionals, entrepreneurs, and families make informed 
            financial decisions through AI-powered learning modules and curated educational videos.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# --- 8. UPCOMING FEATURES ---
st.markdown("<br/>", unsafe_allow_html=True)
st.markdown("### 🚀 Upcoming Learning Innovations")

future_feats = [
    ("🎤 Voice Learning", "Listen to high-definition summary notes and curated lectures on the go without looking at your screen."),
    ("📄 Download Notes", "Instantly fetch simplified PDF cheat sheets, formula tables, and infographics for quick revision."),
    ("🤖 AI Video Recs", "Intelligent matching algorithms suggesting exactly what video to watch next based on your chat history.")
]

feat_cols = st.columns(3)
for idx, (title, desc) in enumerate(future_feats):
    with feat_cols[idx]:
        st.markdown(
            f"""
            <div class="grid-card" style="min-height: 190px;">
                <div class="stat-label" style="color: #D4AF37; font-size: 1.05rem; font-weight: bold;">{title}</div>
                <p style="color: #B0B0B0; font-size: 0.85rem; line-height: 1.5; margin-top: 0.5rem;">{desc}</p>
                <div class="pill-badge" style="border-color: #D4AF37; text-align: center; display: inline-block; padding: 2px 8px; font-size: 0.75rem; color: #D4AF37; margin-top: 0.5rem;">
                    Coming Soon
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- 10. CUSTOM FOOTER ---
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
