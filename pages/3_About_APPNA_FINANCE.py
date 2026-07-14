"""
APPNA FINANCE - About Page
Filename: pages/3_About_APPNA_FINANCE.py
Role: Senior UI/UX Designer & FinTech Architect
Design Language: Luxury Black & Metallic Gold Glassmorphism (Mapped to styles/custom.css)
"""

import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="About Us | APPNA FINANCE",
    page_icon="assets/favicon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SIDEBAR CONFIGURATION ---
with st.sidebar:
    if os.path.exists("assets/logo.png"):
        st.image("assets/logo.png", width=170)
    
    st.markdown("### APPNA FINANCE")
    st.markdown("🏢 **About Page**")
    st.markdown("---")
    
    # Updated to sound more polished and consistent with the project stage
    st.info("💡 Status: Frontend MVP (Backend Integration Coming Soon)")
    
    st.markdown("**Future Capabilities**")
    st.markdown(
        """
        - 🔗 Supabase Secure Auth
        - ☁️ FastAPI Live Backend
        - 🤖 Multi-LLM Orchestration
        - 🧠 Personalized Dynamic Roadmap
        """
    )
    st.markdown("---")
    st.markdown("<small>Created with ❤️ for a financially literate India.</small>", unsafe_allow_html=True)


# --- 1. HERO SECTION ---
st.markdown(
    """
    <div class="hero-container">
        <h1>🏢 About APPNA FINANCE</h1>
        <p style="color: #D4AF37; font-size: 1.3rem; font-weight: 600; margin-top: -0.5rem; letter-spacing: 0.05em;">
            Making Financial Knowledge Simple, Trustworthy, and Accessible for Every Indian.
        </p>
        <p style="color: #B0B0B0; font-size: 1.05rem; max-width: 850px; margin: 0.5rem auto 1.5rem auto; line-height: 1.6;">
            APPNA FINANCE is an AI-powered financial education platform. We help students, farmers, 
            professionals, MSMEs, entrepreneurs, families, and first-time investors understand 
            money and banking through simple explanations, smart AI conversations, and quick educational videos.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Hero Call-to-Action Buttons
hero_btn_cols = st.columns([1, 1, 1, 1])
with hero_btn_cols[1]:
    # TODO: Connect anchor scroll telemetry to measure user interaction
    st.button("🚀 Explore Our Mission", use_container_width=True, type="primary")
with hero_btn_cols[2]:
    st.button("👨 Meet Our Team", use_container_width=True)


# --- Visual Divider (Hero Image Asset) ---
st.markdown("<br/>", unsafe_allow_html=True)

hero_banner = "assets/hero_banner.png"
if os.path.exists(hero_banner):
    st.image(
        hero_banner,
        use_container_width=True,
        caption="Empowering rural and urban communities with simple, accessible digital finance education."
    )
else:
    st.warning("Hero banner not found.")


# --- 2. OUR MISSION ---
st.markdown("---")
st.markdown("### 🎯 Our Mission")
st.write("We are breaking down complex financial concepts into simple, everyday modules:")

mission_cols = st.columns(3)

missions = [
    ("📚 Financial Education", "Easy learning resources covering everyday money management, saving hacks, and investment options."),
    ("🤖 AI Powered Learning", "An active AI assistant available 24/7 to solve your questions in simple words without technical jargon."),
    ("🏦 Banking Knowledge", "A clear guide to savings accounts, FD rates, online transactions, and staying safe from financial fraud."),
    ("📈 Stock Market Basics", "Demystifying mutual funds, stocks, indices (NSE/BSE), and smart portfolio investing."),
    ("🛡️ Loans, Insurance & Tax", "Understand different loans, find the right insurance cover, and navigate income tax slabs easily."),
    ("🌾 Government Schemes", "Easy instructions explaining rural subsidies, MSME grants, and social welfare programs.")
]

for idx, (title, desc) in enumerate(missions):
    col_idx = idx % 3
    with mission_cols[col_idx]:
        st.markdown(
            f"""
            <div class="grid-card" style="min-height: 160px; margin-bottom: 1rem;">
                <div class="stat-label" style="color: #D4AF37; font-size: 1.1rem; font-weight: 600;">{title}</div>
                <div style="color: #B0B0B0; font-size: 0.88rem; margin-top: 0.4rem; line-height: 1.5;">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- 3. WHO WE SERVE ---
st.markdown("---")
st.markdown("### 👥 Who We Serve")

serve_cols = st.columns(3)

audience = [
    ("🎓 Students", "Learn how to build early savings, understand money basics, and prepare for student loan decisions early."),
    ("👨‍🌾 Farmers", "Know your options under the Kisan Credit Card (KCC), crop insurance coverage, and farm business grants."),
    ("👨‍💼 Professionals", "Master active tax savings strategies, asset allocation, smart budget rules, and long-term investment setups."),
    ("🏪 MSMEs", "Scale your small business with secure startup capital guidance, business loans, and MSME tax benefits."),
    ("👨‍👩‍👧 Families", "Set up robust emergency funds, plan family insurance plans, and organize life goals seamlessly."),
    ("📊 First-Time Investors", "Step confidently into SIPs, mutual funds, and stock markets without fear of complicated jargon.")
]

for idx, (title, desc) in enumerate(audience):
    col_idx = idx % 3
    with serve_cols[col_idx]:
        st.markdown(
            f"""
            <div class="grid-card" style="min-height: 160px; margin-bottom: 1rem;">
                <div class="stat-label" style="color: #D4AF37; font-size: 1.1rem; font-weight: 600;">{title}</div>
                <div style="color: #B0B0B0; font-size: 0.88rem; margin-top: 0.4rem; line-height: 1.5;">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- 4. OUR VISION ---
st.markdown("---")
st.markdown("### 🌍 Our Vision")

# Updated vision wording from "bilingual" to "multilingual" to accurately support English, Hindi, and Bengali
st.markdown(
    """
    <div class="premium-card" style="border: 1px solid rgba(212, 175, 55, 0.4); background: rgba(26, 29, 36, 0.95); text-align: center; padding: 2rem !important;">
        <h4 style="color: #D4AF37; margin-bottom: 0.75rem;">Becoming India's Most Trusted Education Platform</h4>
        <p style="color: #FFFFFF; font-size: 1.1rem; max-width: 800px; margin: 0 auto; line-height: 1.6; font-weight: 500;">
            "To make high-quality financial knowledge simple, multilingual, and free for every single Indian household."
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# --- 5. OUR CORE VALUES ---
st.markdown("<br/>", unsafe_allow_html=True)
st.markdown("### 💡 Our Core Values")

val_cols = st.columns(4)

values = [
    ("📚 Education First", "Our central goal is to teach you how money works, not sell you financial products."),
    ("🤖 AI for Good", "Applying state-of-the-art conversational AI to solve personal financial confusion on demand."),
    ("🔒 Trust & Transparency", "Unbiased information without high-interest loans, promotions, or hidden sales scripts."),
    ("🌍 Financial Inclusion", "Reaching remote towns, agricultural zones, and everyday households with regional language dialects."),
    ("💡 Purposeful Tech", "Designing clear, low-friction interfaces so even a beginner can learn easily."),
    ("❤️ Customer First", "Structuring our learning flows, roadmaps, and videos around your questions and needs."),
    ("🇮🇳 Empowering India", "Doing our part to build a financially literate, self-reliant, and money-smart nation.")
]

for idx, (title, desc) in enumerate(values):
    col_idx = idx % 4
    with val_cols[col_idx]:
        st.markdown(
            f"""
            <div class="grid-card" style="min-height: 160px; margin-bottom: 1rem;">
                <div class="stat-label" style="color: #D4AF37; font-size: 1.05rem; font-weight: 600;">{title}</div>
                <div style="color: #B0B0B0; font-size: 0.85rem; margin-top: 0.4rem; line-height: 1.45;">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- 6. OUR TECHNOLOGY STACK ---
st.markdown("---")
st.markdown("### 🛠️ Our Tech Stack")

tech_cols = st.columns(3)

tech_stack = [
    ("💻 Frontend", "Streamlit", "Powering a beautiful, responsive, premium glassmorphic visual interface."),
    ("⚙️ Backend", "FastAPI (Upcoming)", "A high-performance backend processing fast user queries and orchestrations."),
    ("🧠 AI Engine", "Vertex AI & Groq LLM", "Generating simple, accurate, multilingual answers in seconds."),
    ("📂 Knowledge Base", "ChromaDB (RAG)", "Empowering the AI assistant with verified financial books and guidelines."),
    ("🔒 Security & Auth", "Supabase (Upcoming)", "Ensuring highly secure user logins and personalized tracking metrics."),
    ("☁️ Infrastructure", "Google Cloud Platform", "Hosting scalable servers to deliver seamless education nationwide.")
]

for idx, (category, name, desc) in enumerate(tech_stack):
    col_idx = idx % 3
    with tech_cols[col_idx]:
        st.markdown(
            f"""
            <div class="grid-card" style="min-height: 155px; margin-bottom: 1rem;">
                <div class="stat-label" style="color: #D4AF37; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em;">{category}</div>
                <div style="color: #FFFFFF; font-size: 1.15rem; font-weight: 600; margin-top: 0.15rem;">{name}</div>
                <div style="color: #808080; font-size: 0.85rem; margin-top: 0.4rem; line-height: 1.4;">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- 7. OUR ROADMAP ---
st.markdown("---")
st.markdown("### 🗺️ Our Evolutionary Journey")

st.markdown(
    """
    <div style="margin-top: 1.5rem;">
        <div style="border-left: 3px solid #D4AF37; margin-left: 20px; padding-left: 30px; position: relative; margin-bottom: 2rem;">
            <div style="position: absolute; left: -11px; top: 0; background: #55D437; width: 20px; height: 20px; border-radius: 50%;"></div>
            <strong style="color: #55D437; font-size: 1.15rem;">Phase 1: Frontend MVP (Completed)</strong>
            <p style="color: #B0B0B0; margin: 0.25rem 0 0 0; font-size: 0.95rem;">Successfully constructed premium luxury user interfaces, demo chat engines, and structured learning categories.</p>
        </div>
        <div style="border-left: 3px solid #D4AF37; margin-left: 20px; padding-left: 30px; position: relative; margin-bottom: 2rem;">
            <div style="position: absolute; left: -11px; top: 0; background: #D4AF37; width: 20px; height: 20px; border-radius: 50%;"></div>
            <strong style="color: #D4AF37; font-size: 1.15rem;">Phase 2: AI Assistant Core (In Progress)</strong>
            <p style="color: #B0B0B0; margin: 0.25rem 0 0 0; font-size: 0.95rem;">Tuning our LLM engines to explain personal finance in highly conversational, simplified regional languages.</p>
        </div>
        <div style="border-left: 3px solid #D4AF37; margin-left: 20px; padding-left: 30px; position: relative; margin-bottom: 2rem;">
            <div style="position: absolute; left: -11px; top: 0; background: #808080; width: 20px; height: 20px; border-radius: 50%;"></div>
            <strong style="color: #808080; font-size: 1.15rem;">Phase 3: Google Cloud Integration (Upcoming)</strong>
            <p style="color: #B0B0B0; margin: 0.25rem 0 0 0; font-size: 0.95rem;">Deploying secure database layers, establishing RAG architecture models, and connecting backend routes via FastAPI.</p>
        </div>
        <div style="border-left: 3px solid #D4AF37; margin-left: 20px; padding-left: 30px; position: relative; margin-bottom: 2rem;">
            <div style="position: absolute; left: -11px; top: 0; background: #808080; width: 20px; height: 20px; border-radius: 50%;"></div>
            <strong style="color: #808080; font-size: 1.15rem;">Phase 4: Voice & Regional Dialect (Upcoming)</strong>
            <p style="color: #B0B0B0; margin: 0.25rem 0 0 0; font-size: 0.95rem;">Enabling natural vocal inputs and audio responses to make the app friendly for elderly and rural users.</p>
        </div>
        <div style="border-left: 3px solid #D4AF37; margin-left: 20px; padding-left: 30px; position: relative; margin-bottom: 2rem;">
            <div style="position: absolute; left: -11px; top: 0; background: #808080; width: 20px; height: 20px; border-radius: 50%;"></div>
            <strong style="color: #808080; font-size: 1.15rem;">Phase 5: Automated Document Summarizer (Upcoming)</strong>
            <p style="color: #B0B0B0; margin: 0.25rem 0 0 0; font-size: 0.95rem;">Enable simple PDF audits to scan complex loan contracts, bank letters, or taxes instantly with AI.</p>
        </div>
        <div style="border-left: 3px solid #D4AF37; margin-left: 20px; padding-left: 30px; position: relative; margin-bottom: 1rem;">
            <div style="position: absolute; left: -11px; top: 0; background: #808080; width: 20px; height: 20px; border-radius: 50%;"></div>
            <strong style="color: #808080; font-size: 1.15rem;">Phase 6: National Scale Release (Future)</strong>
            <p style="color: #B0B0B0; margin: 0.25rem 0 0 0; font-size: 0.95rem;">Official platform rollout helping millions across schools, colleges, cooperatives, and small businesses.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# --- 8. FOUNDER SPOTLIGHT ---
st.markdown("---")
st.markdown("### 👨‍💻 Founder Profile")

# Layout integration for real founder spotlight image safely aligned with details
spotlight_cols = st.columns([1, 3])

with spotlight_cols[0]:
    founder_img_path = "assets/team/akash_bauri.png"
    if os.path.exists(founder_img_path):
        st.image(founder_img_path, width=280)
    else:
        st.warning("Image not found")

with spotlight_cols[1]:
    st.markdown(
        """
        <div class="premium-card" style="border: 1px solid rgba(212, 175, 55, 0.25); background: rgba(26, 29, 36, 0.95); height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <div>
                <h3 style="color: #D4AF37; margin: 0; font-size: 1.6rem;">Akash Bauri</h3>
                <p style="color: #FFFFFF; font-weight: 500; margin: 0.25rem 0 0 0;">Founder, CEO & Founding AI Engineer</p>
                <p style="color: #D4AF37; font-size: 0.95rem; font-weight: 500; margin: 0.15rem 0 0 0; letter-spacing: 0.02em;">AI Researcher | Product Architect</p>
                <p style="color: #808080; font-size: 0.85rem; margin: 0.25rem 0 0 0;">APPNA FINANCE</p>
                <p style="color: #B0B0B0; font-size: 0.92rem; line-height: 1.5; margin-top: 0.75rem;">
                    Akash Bauri is the Founder, Chief Executive Officer (CEO), and Founding AI Engineer of APPNA FINANCE. Akash Bauri is an AI Engineer, entrepreneur, and product builder dedicated to transforming financial education through Artificial Intelligence. His work combines Generative AI, Large Language Models, Machine Learning, Retrieval-Augmented Generation (RAG), and intelligent automation to make financial knowledge simple, trustworthy, and accessible for every Indian.
                    <br/><br/>
                    He has hands-on experience in Artificial Intelligence, Machine Learning, Generative AI, Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), AI Agents, Prompt Engineering, Automation, and Intelligent Financial Systems.
                    <br/><br/>
                    His vision is to bridge the financial knowledge gap in India by helping students, farmers, working professionals, entrepreneurs, first-time investors, and families understand banking, investments, stock markets, personal finance, insurance, taxation, and government financial schemes through AI-powered education.
                    <br/><br/>
                    Under his leadership, APPNA FINANCE is being developed as a multilingual AI-powered financial education platform supporting English, Hindi, and Bengali, making financial knowledge accessible to users from both urban and rural communities.
                    <br/><br/>
                    His long-term mission is to build one of India's most trusted AI-powered financial education platforms while contributing to financial literacy, financial inclusion, and responsible financial decision-making across the country.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br/>", unsafe_allow_html=True)
social_cols = st.columns([1, 1, 1, 1])
# TODO: Connect actual verified founder social profiles dynamically from global configuration
with social_cols[0]:
    st.button("🔗 LinkedIn", use_container_width=True, disabled=True)
with social_cols[1]:
    st.button("🐙 GitHub", use_container_width=True, disabled=True)
with social_cols[2]:
    st.button("📺 YouTube", use_container_width=True, disabled=True)
with social_cols[3]:
    st.button("📧 Contact Direct", use_container_width=True, disabled=True)


# --- 9. OUR TEAM ---
st.markdown("---")
st.markdown("### 👥 The Founding Team")

team_cols = st.columns(3)

team_members = [
    {
        "name": "Akash Bauri",
        "role": "Founder, CEO & Founding AI Engineer",
        "desc": "Responsible for the overall vision, AI architecture, product strategy, research, backend system design, RAG pipeline, AI agent development, machine learning integration, prompt engineering, and long-term technology roadmap of APPNA FINANCE.",
        "img": "assets/team/akash_bauri.png"
    },
    {
        "name": "Jyoti Bouri",
        "role": "Co-Founder | Operations & Business Support",
        "desc": "Supports business operations, customer relationship management, accounting coordination, financial documentation, administrative planning, partnership support, and organizational growth while helping build a reliable and customer-focused financial education platform.",
        "img": "assets/team/jyoti_bouri.jpg"
    },
    {
        "name": "Shanmugapriya Subramani",
        "role": "Lead Frontend Engineer",
        "desc": "Leads frontend architecture and user experience design by developing modern, responsive, and scalable interfaces. Responsible for implementing premium UI components, improving usability, maintaining design consistency, and delivering a seamless learning experience across the APPNA FINANCE platform.",
        "img": "assets/team/shanmugapriya_subramani.png"
    }
]

for idx, member in enumerate(team_members):
    with team_cols[idx]:
        if os.path.exists(member["img"]):
            st.image(member["img"], width=80)
        else:
            st.warning("Image not found")
            
        st.markdown(
            f"""
            <div class="grid-card" style="min-height: 300px;">
                <div style="color: #FFFFFF; font-size: 1.15rem; font-weight: bold; margin-top: 0.5rem;">{member['name']}</div>
                <div style="color: #D4AF37; font-size: 0.85rem; font-weight: 500; margin-top: 0.15rem;">{member['role']}</div>
                <div style="color: #808080; font-size: 0.82rem; margin-top: 0.5rem; line-height: 1.4;">{member['desc']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Team Expansion Notice
st.markdown("<br/>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; color: #808080; font-size: 0.9rem; font-style: italic;">
        🚀 We are growing! More roles, financial creators, and engineering positions are coming soon.
    </div>
    """,
    unsafe_allow_html=True
)


# --- 10. WHY APPNA FINANCE ---
st.markdown("---")
st.markdown("### 🏆 Why Choose APPNA FINANCE?")

why_cols = st.columns(4)

reasons = [
    ("✔ Trusted Knowledge", "Verified financial study guides from government institutions and bank policies."),
    ("✔ AI Powered Learning", "Ask dynamic questions and get smart, clear solutions instantly."),
    ("✔ Beginner Friendly", "Zero jargon. Everything is explained like we're speaking with a young student."),
    ("✔ Regional Support", "Learn comfortably with English, Hindi, and Bengali configurations.")
]

for idx, (title, desc) in enumerate(reasons):
    with why_cols[idx]:
        st.markdown(
            f"""
            <div class="grid-card" style="min-height: 140px;">
                <div class="stat-label" style="color: #55D437; font-size: 1.1rem; font-weight: bold;">{title}</div>
                <div style="color: #B0B0B0; font-size: 0.85rem; margin-top: 0.4rem; line-height: 1.45;">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- 11. CONTACT SECTION ---
st.markdown("---")
st.markdown("### 📞 Get in Touch")

contact_cols = st.columns(5)

contact_details = [
    ("📧 Email", "Coming Soon"),
    ("🌐 Website", "Coming Soon"),
    ("🐙 GitHub", "Coming Soon"),
    ("🔗 LinkedIn", "Coming Soon"),
    ("📺 YouTube Channel", "https://youtube.com/@akashlearninghub-m7n")
]

for idx, (label, link) in enumerate(contact_details):
    with contact_cols[idx]:
        if "https" in link:
            st.markdown(
                f"""
                <div class="grid-card" style="min-height: 100px; text-align: center; display: flex; flex-direction: column; justify-content: center;">
                    <div style="color: #D4AF37; font-size: 0.85rem; font-weight: bold; text-transform: uppercase;">{label}</div>
                    <a href="{link}" target="_blank" style="color: #FFFFFF; font-size: 0.85rem; text-decoration: none; margin-top: 0.35rem; display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                        Visit Channel 🔗
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="grid-card" style="min-height: 100px; text-align: center; display: flex; flex-direction: column; justify-content: center;">
                    <div style="color: #D4AF37; font-size: 0.85rem; font-weight: bold; text-transform: uppercase;">{label}</div>
                    <div style="color: #808080; font-size: 0.85rem; margin-top: 0.35rem;">{link}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


# --- 12. CUSTOM FOOTER ---
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
