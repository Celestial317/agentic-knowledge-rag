---

# 🧠**RAG-Powered Knowledge Agent with Query Routing**

A **knowledge-based Retrieval-Augmented Generation (RAG)** system powered by a **Query Agent** that smartly routes user questions to the most relevant source — **arXiv**, **Wikipedia**, or **Tavily** — for accurate and contextual answers.

---

## 🔍 Overview

This project combines the power of **LangChain**, **Google Gemini**, and **multi-source routing** to intelligently fetch answers based on the nature of a user's query. The agent analyzes your input and decides which knowledge base to consult, delivering answers with minimal effort and maximum relevance.

---

## ⚙️ Setup

1. **Install dependencies**:

```bash
pip install -r requirements.txt
```

2. **Create a `.env` file** in the project root:

```
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## 🚀 How to Use

Run the agent using:

```bash
python main.py
```

Then simply enter your query. The system will:

* Detect the intent of your question
* Route it to arXiv (for research), Wikipedia (for general facts), or Tavily (for current events)
* Display a well-formatted answer in your terminal

---

## 💬 Example Session

```
Your query:
What are the breakthroughs in AI safety research?

Processing....
Chosen Source: arxiv
Processing....
Answer:
Recent papers discuss interpretability, alignment techniques, and robust training strategies for safer AI development.
```

```
Your query:
Who invented the telephone?

Processing....
Chosen Source: wikipedia
Processing....
Answer:
Alexander Graham Bell is credited with inventing the first practical telephone in 1876.
```

---

## 🧩 Project Structure

| File               | Purpose                                                |
| ------------------ | ------------------------------------------------------ |
| `main.py`          | CLI and routing logic for handling queries             |
| `knowledge_rag.py` | Chains for fetching data from arXiv, Wikipedia, Tavily |

---

## 🤖 Source Routing Logic

The system uses a **Gemini-powered LLM** to classify the query and choose from:

* **arXiv** → Academic/scientific questions
* **Wikipedia** → Historical or factual general knowledge
* **Tavily** → Live/current events and web-based search

---

## 🎯 Motivation

This project was built to simplify multi-source information retrieval. Instead of hardcoding the source or relying on a single tool, we built a **flexible Query Agent** that picks the right tool for the job — enhancing **accuracy**, **speed**, and **usability**.

---

## 👨‍💻 Created By

**Soumya Sourav Das**

> An AI-ML enthusiast
---

