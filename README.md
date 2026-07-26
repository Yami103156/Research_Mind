                  ![Python](https://img.shields.io/badge/Python-3.13-blue)  ![LangChain](https://img.shields.io/badge/LangChain-AI-green)![Gemini](https://img.shields.io/badge/Google-Gemini-orange)  ![Streamlit](https://img.shields.io/badge/Streamlit-App-red)  ![Render](https://img.shields.io/badge/Deploy-Render-purple)  ![License](https://img.shields.io/badge/License-MIT-yellow)

<div align="center">

# 🧠 ResearchMind AI

### Autonomous Multi-Agent AI Research Assistant

Generate high-quality research reports using an AI-powered multi-agent workflow built with LangChain, Gemini, Tavily Search, and Streamlit.

🌐 **Live Demo:** https://research-mind-kmhu.onrender.com/

</div>

---

## 📌 Overview

ResearchMind AI is an autonomous AI research assistant that performs deep web research through a coordinated multi-agent architecture.

Instead of asking a single LLM to generate an answer, the system divides the task among specialized AI agents that collaboratively:

- Plan research
- Search the web
- Read webpages
- Generate reports
- Critique the output
- Improve the report automatically

The application provides an interactive Streamlit dashboard for exploring generated reports, sources, and AI feedback.

---

# ✨ Features

✅ Autonomous Multi-Agent Workflow

✅ AI Research Planner

✅ Web Search using Tavily API

✅ Intelligent Webpage Reader

✅ AI Report Generator

✅ Report Critic Agent

✅ Automatic Report Improvement

✅ Modern Streamlit Dashboard

✅ Download Research Report

✅ Download Critic Feedback

---

# 🏗 Architecture

```
                User
                  │
                  ▼
          Streamlit Interface
                  │
                  ▼
          Planner Agent
                  │
                  ▼
          Search Agent
                  │
                  ▼
          Reader Agent
                  │
                  ▼
          Writer Agent
                  │
                  ▼
          Critic Agent
                  │
                  ▼
      Auto Improvement Loop
                  │
                  ▼
          Final Research Report
```

---

# 🤖 AI Agents

## 🧠 Planner Agent

Generates an optimized research strategy.

Outputs:

- Research goal
- Search queries
- Focus areas

---

## 🌐 Search Agent

Searches the web using Tavily.

Responsibilities

- Executes research queries
- Retrieves relevant webpages
- Removes duplicate links

---

## 📖 Reader Agent

Reads and extracts information from webpages.

Responsibilities

- Web scraping
- HTML cleaning
- Content extraction

---

## ✍ Writer Agent

Synthesizes all collected evidence into a professional research report.

Includes

- Executive Summary
- Introduction
- Key Findings
- Detailed Analysis
- Conclusion

---

## 🧐 Critic Agent

Reviews the generated report.

Evaluates

- Accuracy
- Completeness
- Structure
- Readability
- Research Quality

Returns

- Feedback
- Suggestions
- Overall Score

---

# 🛠 Tech Stack

### Frontend

- Streamlit
- HTML
- CSS

### AI

- Google Gemini
- LangChain

### Search

- Tavily Search API

### Web Scraping

- BeautifulSoup
- Requests

### Utilities

- Pydantic
- Rich Console
- Tenacity

---


---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ResearchMind-AI.git

cd ResearchMind-AI
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
GOOGLE_API_KEY=your_gemini_api_key

TAVILY_API_KEY=your_tavily_api_key
```

---

# ▶ Running the Application

```bash
streamlit run app.py
```

---

# 🌍 Live Demo

https://research-mind-kmhu.onrender.com/

---




# Skills Demonstrated

- Multi-Agent AI Systems
- Prompt Engineering
- LangChain
- LLM Orchestration
- Web Search Integration
- Web Scraping
- AI Workflow Automation
- Streamlit Development
- Python
- REST APIs

---

# Deployment

The application is deployed using **Render**.

---

# License

MIT License

---

# Author

**Yamini**


