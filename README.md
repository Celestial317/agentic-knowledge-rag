---

# **RAG-Powered Knowledge Agent with Intelligent Query Routing**

A **Retrieval-Augmented Generation (RAG)** system enhanced with a **Query Agent** that intelligently routes user queries to the most suitable knowledge source—**arXiv**, **Wikipedia**, or **Tavily**—for contextually accurate and up-to-date responses.

---

## Overview

This project integrates **LangChain**, **Google Gemini**, and multi-source retrieval mechanisms to create an intelligent knowledge system. Based on the semantic content of a user's query, the agent dynamically selects the most relevant source and delivers precise, high-quality answers with minimal user effort.

---

## Setup Instructions

1. **Install required dependencies:**

```bash
pip install -r requirements.txt
```

2. **Configure environment variables** by creating a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Usage Guide

To start the system, run:

```bash
python main.py
```

Once running, you can input a natural language query. The agent will:

* Interpret the intent of the query
* Route it to the appropriate data source (arXiv, Wikipedia, or Tavily)
* Retrieve and format the response for terminal display

---

## Example Interaction

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

## Project Structure

| File               | Description                                              |
| ------------------ | -------------------------------------------------------- |
| `main.py`          | Handles CLI, routing logic, and system orchestration     |
| `knowledge_rag.py` | Implements retrieval chains for arXiv, Wikipedia, Tavily |

---

## Query Routing Logic

A Gemini-powered large language model is used to classify incoming queries and select one of the following sources:

* **arXiv**: For technical, scientific, or academic topics
* **Wikipedia**: For general knowledge, factual history, and definitions
* **Tavily**: For current events and real-time web content

This automated source selection ensures that each query is matched with the most relevant and reliable data.

---

## Project Motivation

The goal of this project is to streamline knowledge retrieval by combining multiple sources into a unified, intelligent agent. Rather than relying on static search logic or a single API, this system employs a dynamic routing approach that enhances:

* Precision in selecting data sources
* Responsiveness for time-sensitive information
* User experience through automation and clarity

---

## Author

**Soumya Sourav Das**
> AI & Machine Learning Enthusiast

---
