"""
APPNA FINANCE - AI Financial Assistant Page
Filename: pages/1_AI_Assistant.py
Role: Senior Streamlit UI/UX & AI Product Frontend
Design Language: Luxury Black & Metallic Gold Glassmorphism (Mapped to styles/custom.css)
"""

import streamlit as st
import requests
import time

# ==========================================
# BACKEND CONFIGURATION
# ==========================================
API_URL = "https://agent-production-c6e4.up.railway.app/api/v1/chat"

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Financial Assistant | APPNA FINANCE",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --- HELPERS & STATE INITIALIZATION ---
def initialize_session_state():
    """Initializes the chat history state if not already existing."""
    if "chat_history" not in st.session_state:
        # Default welcoming system message
        st.session_state.chat_history = [
            {
                "role": "ai",
                "message": (
                    "Welcome to APPNA FINANCE! I'm your AI Financial Assistant. "
                    "Ask me anything about banking, stock markets, personal finance, "
                    "loans, insurance, taxes, or government schemes. I'll explain everything in simple language."
                )
            }
        ]
    if "chat_input_val" not in st.session_state:
        st.session_state.chat_input_val = ""


def handle_send_message(user_query: str):

    if not user_query.strip():
        return

    st.session_state.chat_history.append(
        {
            "role": "user",
            "message": user_query
        }
    )

    try:

        response = requests.post(
            API_URL,
            json={
                "question": user_query
            },
            timeout=60
        )

        if response.status_code == 200:

            data = response.json()

            ai_response = data.get(
                "answer",
                "No response received."
            )

        else:

            ai_response = f"Backend Error: {response.status_code}\n\n{response.text}"

    except Exception as e:

        ai_response = f"Connection Error:\n\n{e}"

    st.session_state.chat_history.append(
        {
            "role": "ai",
            "message": ai_response
        }
    )

    st.session_state.chat_input_val = ""


# Initialize state elements
initialize_session_state()


# --- 9. SIDEBAR INFORMATION ---
with st.sidebar:
    st.markdown("### APPNA FINANCE")
    st.markdown("🤖 **AI Assistant Panel**")
    st.markdown("---")
    
    # Technical Architecture Details (Reflecting target state)
    st.markdown("**System Architecture Overview**")
    st.info("💡 Status: CONNECTED TO BACKEND")
    
    # Metadata Key-Values
    st.markdown(
        """
        | Component | Environment |
        | :--- | :--- |
        | **Backend** | `Live (Railway)` |
        | **User Auth** | `Supabase (Future)` |
        | **Gateway** | `FastAPI` |
        | **LLM Engine** | `Qwen (Groq)` |
        | **LLM Orchestrator** | `Groq Client` |
        | **Vector DB** | `ChromaDB (RAG)` |
        """
    )
    st.markdown("---")
    st.markdown("<small>Designed for absolute financial clarity.</small>", unsafe_allow_html=True)


# --- 1. TOP HERO SECTION ---
st.markdown(
    """
    <div class="hero-container">
        <h1>🤖 AI Financial Assistant</h1>
        <p style="color: #B0B0B0; font-size: 1.15rem; margin-top: -0.5rem;">
            Ask questions about banking, investments, loans, insurance, taxes, and government schemes in simple language.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Premium Information Card explaining project status
st.markdown(
    """
    <div class="premium-card">
        <h4 style="color: #D4AF37; margin-bottom: 0.5rem;">ℹ️ Connected Assistant</h4>
        <p style="color: #FFFFFF; margin: 0; line-height: 1.6;">
            <strong>APPNA FINANCE AI Assistant</strong> helps users understand financial concepts in simple, jargon-free language. 
            This interface is connected to our FastAPI backend running on Railway with Groq key management and multi-lingual AI support.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# --- 2. QUICK QUESTION CARDS ---
st.markdown("### 💡 Quick Starters")
st.write("Click any sample card below to auto-populate the AI input field and start learning instantly:")

quick_questions = [
    ("💳 Credit", "How to improve CIBIL Score?"),
    ("📈 Wealth", "Explain SIP."),
    ("🏦 Banking", "What is a Savings Account?"),
    ("⚡ UPI", "What is UPI?"),
    ("💰 Deposits", "Difference between FD and RD?"),
    ("📊 Funds", "What is a Mutual Fund?"),
    ("🎓 Loans", "How do Education Loans work?"),
    ("🚀 Investing", "How to start investing?")
]

# Layout quick cards in columns
cols = st.columns(4)
for i, (category, question) in enumerate(quick_questions):
    col_idx = i % 4
    with cols[col_idx]:
        # Utilizing predefined custom.css class 'grid-card'
        card_html = f"""
        <div class="grid-card" style="cursor: pointer; min-height: 110px !important; padding: 1.25rem !important; margin-bottom: 1rem;">
            <div class="stat-label" style="text-align: left; color: #D4AF37;">{category}</div>
            <div style="font-family: 'Inter', sans-serif; font-size: 0.95rem; font-weight: 500; color: #FFFFFF; margin-top: 0.25rem;">
                {question}
            </div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        # Unique key identifier for Streamlit button to intercept click
        if st.button(f"Ask: {category}", key=f"btn_{i}", use_container_width=True):
            st.session_state.chat_input_val = question
            st.rerun()


# --- 3. CHAT INTERFACE & 4. INPUT AREA ---
st.markdown("---")
st.markdown("### 💬 Interactive Chat Studio")

# Container for Chat Streams
chat_container = st.container()

with chat_container:
    # Render all historic system/user/ai bubbles
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(
                f"""
                <div style="display: flex; justify-content: flex-end; margin-bottom: 1rem;">
                    <div style="background: rgba(212, 175, 55, 0.15); border: 1px solid rgba(212, 175, 55, 0.3); 
                                padding: 1rem; border-radius: 16px 16px 4px 16px; max-width: 75%; color: #FFFFFF;">
                        <strong style="color: #F4C430;">You</strong><br/>{chat['message']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="display: flex; justify-content: flex-start; margin-bottom: 1rem;">
                    <div style="background: #1A1D24; border: 1px solid rgba(255, 255, 255, 0.05); 
                                padding: 1.25rem; border-radius: 16px 16px 16px 4px; max-width: 80%; color: #FFFFFF;">
                        <strong style="color: #D4AF37;">APPNA AI Expert</strong><br/>{chat['message']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown("<br/>", unsafe_allow_html=True)

# Input Box Integration
# Setting up columns for input field, trigger send button and coming soon mic widget
input_cols = st.columns([7, 2, 2])

with input_cols[0]:
    user_input = st.text_input(
        label="Query Input Box",
        value=st.session_state.chat_input_val,
        placeholder="Ask your financial question... (e.g., Explain compound interest)",
        label_visibility="collapsed",
        key="main_chat_input"
    )

with input_cols[1]:
    # Micro button styled automatically via custom.css override on stButton
    submit_clicked = st.button("Ask AI", use_container_width=True)

with input_cols[2]:
    # Non-functional mic button representing voice features
    st.button("🎤 Coming Soon", disabled=True, use_container_width=True)

# Run process loop if submit requested
if submit_clicked and user_input:
    handle_send_message(user_input)
    st.rerun()


# --- 6. SUGGESTED TOPICS ---
st.markdown("### 🏷️ Explore More Topics")
suggested_topics = [
    "Banking", "Stock Market", "Insurance", "Personal Finance", 
    "Mutual Funds", "Loans", "MSME", "Government Schemes", 
    "Income Tax", "Digital Banking", "UPI", "Financial Planning"
]

# Rendering using predetermined premium CSS styling class: 'pill-badge'
pill_container_html = "<div style='margin-bottom: 2rem;'>"
for topic in suggested_topics:
    pill_container_html += f'<span class="pill-badge">{topic}</span>'
pill_container_html += "</div>"
st.markdown(pill_container_html, unsafe_allow_html=True)


# --- 7. IMPORTANT NOTICE ---
st.markdown(
    """
    <div class="premium-card" style="border-left: 4px solid #F4C430; background: rgba(26, 29, 36, 0.8);">
        <h5 style="color: #F4C430; margin-top: 0; margin-bottom: 0.5rem;">⚠️ IMPORTANT EDUCATIONAL DISCLAIMER</h5>
        <p style="color: #B0B0B0; font-size: 0.9rem; line-height: 1.5; margin: 0;">
            APPNA FINANCE provides financial education for informational and knowledge purposes only. 
            It does not constitute personalized investment, legal, statutory or tax advice. 
            Always verify crucial financial actions or statutory decisions with qualified professional advisors.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# --- 8. FUTURE FEATURES ---
st.markdown("<br/>", unsafe_allow_html=True)
st.markdown("### 🚀 Future Envisioned AI Suite")

future_cols = st.columns(3)

with future_cols[0]:
    st.markdown(
        """
        <div class="grid-card">
            <div class="grid-icon">🎙️</div>
            <div class="grid-title">Voice Assistant</div>
            <div class="grid-desc">Talk directly to your advisor with real-time natural language auditory conversion.</div>
            <div class="pill-badge" style="margin: 8px 0 0 0; text-align: center; border-color: #D4AF37;">Coming Soon</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with future_cols[1]:
    st.markdown(
        """
        <div class="grid-card">
            <div class="grid-icon">📄</div>
            <div class="grid-title">Document Parsing</div>
            <div class="grid-desc">Upload financial sheets, tax forms, or company reports for instant semantic breakdown.</div>
            <div class="pill-badge" style="margin: 8px 0 0 0; text-align: center; border-color: #D4AF37;">Coming Soon</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with future_cols[2]:
    st.markdown(
        """
        <div class="grid-card">
            <div class="grid-icon">🌐</div>
            <div class="grid-title">Multi-lingual AI</div>
            <div class="grid-desc">Access high-quality financial education in your preferred regional dialect dynamically.</div>
            <div style="margin-top: 10px; display: flex; gap: 5px; flex-wrap: wrap;">
                <span class="pill-badge" style="margin: 0; font-size: 0.75rem; padding: 4px 10px;">English</span>
                <span class="pill-badge" style="margin: 0; font-size: 0.75rem; padding: 4px 10px;">Hindi</span>
                <span class="pill-badge" style="margin: 0; font-size: 0.75rem; padding: 4px 10px;">Bengali</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# --- 10. CUSTOM FOOTER ---
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
