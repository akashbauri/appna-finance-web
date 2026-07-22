# 🤖 APPNA FINANCE

<div align="center">

### AI-Powered Financial Education Platform

**Making Financial Knowledge Simple, Trustworthy and Accessible for Every Indian.**

Learn • Grow • Prosper

</div>

---

# 📖 About APPNA FINANCE

APPNA FINANCE is an AI-powered financial education platform that helps users understand banking, stock markets, investments, loans, insurance, taxes, government schemes, and personal finance in simple language.

The platform combines Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), vector search, and multilingual AI to provide accurate educational answers from a curated financial knowledge base.

The project is designed especially for:

- 🎓 Students
- 🚜 Farmers
- 👨‍💼 Professionals
- 🏢 MSMEs
- 👨‍👩‍👧 Families
- 📈 First-Time Investors

---

# ✨ Features

## 🤖 AI Financial Assistant

- AI-powered financial chatbot
- Groq LLM Integration
- FastAPI Backend
- Streamlit Frontend
- Context-aware responses
- Educational financial guidance

---

## 📚 Financial Topics

- Banking
- Savings Accounts
- Fixed Deposits
- Recurring Deposits
- Mutual Funds
- SIP
- Stock Market
- Insurance
- Income Tax
- Loans
- MSME Schemes
- Government Schemes
- Digital Banking
- UPI
- Financial Planning

---

## 🌍 Multilingual Support

Supports:

- English
- Hindi
- Bengali

---

## 🧠 AI Technologies

- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Database
- Semantic Search
- PDF Knowledge Base
- Groq LLM
- Intelligent Context Retrieval

---

# 🏗️ Project Architecture

```
                User
                  │
                  ▼
      Streamlit Frontend
                  │
                  ▼
        FastAPI REST API
                  │
                  ▼
      Redis Cache Layer
                  │
                  ▼
        RAG Search Engine
                  │
         ┌────────┴────────┐
         │                 │
         ▼                 ▼
     ChromaDB         PDF Knowledge Base
         │
         ▼
      Groq LLM
         │
         ▼
   Financial Response
```

---

# ⚙️ Tech Stack

## Frontend

- Streamlit
- Python
- HTML
- CSS

## Backend

- FastAPI
- Uvicorn
- Pydantic

## AI

- Groq API
- Qwen 3.6 27B
- RAG Pipeline
- ChromaDB

## Database

- ChromaDB
- Redis

## Deployment

- Railway (Backend)
- Streamlit Cloud (Frontend)

---

# 📂 Project Structure

```
APPNA-FINANCE/

│
├── app.py
├── pages/
├── assets/
├── styles/
├── requirements.txt
├── README.md
│
└── Backend (Separate Repository)
        │
        ├── app/
        ├── api/
        ├── services/
        ├── models/
        ├── database/
        ├── pdfs/
        └── chroma_db/
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/appna-finance-web.git
```

```
cd appna-finance-web
```

Install packages

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

---

# 🔗 Backend

Backend Repository

```
FastAPI
```

Features

- REST API
- Redis Cache
- ChromaDB
- Groq LLM
- Whisper Support
- PDF RAG

---

# API Endpoint

```
POST /api/v1/chat
```

Request

```json
{
    "question":"What is SIP?"
}
```

Response

```json
{
    "user_speech_text":"What is SIP?",
    "detected_language":"English",
    "answer":"SIP stands for Systematic Investment Plan...",
    "source_type":"knowledge_base",
    "source_name":"PDF Knowledge Base"
}
```

---

# Future Roadmap

- Voice Assistant
- OCR
- PDF Upload
- Image Understanding
- Personalized Learning
- Financial Calculators
- Loan Recommendation
- Government Scheme Finder
- Portfolio Learning
- Mobile App
- Android Application
- iOS Application

---

# Security

- Input Validation
- Error Handling
- Cache Management
- Admin Authentication
- Protected Reindex Endpoint

---

# Performance

- Redis Cache
- FastAPI Async
- ChromaDB Search
- Optimized Prompt Engineering
- Vector Search

---

# Founder

## Akash Bauri

Founder, CEO & Founding AI Engineer

AI Engineer focused on

- Artificial Intelligence
- Machine Learning
- Generative AI
- LLMs
- RAG Systems
- AI Agents
- Intelligent Automation

---

# Mission

> Making Financial Knowledge Simple, Trustworthy and Accessible for Every Indian.

---

# License

This project is released under the MIT License.

---

# Acknowledgements

Special thanks to

- Groq
- FastAPI
- Streamlit
- ChromaDB
- Railway
- Python Community

---

<div align="center">

## ⭐ If you like this project, don't forget to star the repository.

Made with ❤️ in India

APPNA FINANCE

Learn • Grow • Prosper

</div>
