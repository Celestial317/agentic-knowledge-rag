# Query-Based Knowledge Agent

A smart knowledge agent that routes queries to the appropriate information sources (arXiv papers, Wikipedia, or Tavily search) based on the query content.

## Overview

This system uses LangChain and Google Gemini to create a knowledge retrieval system with intelligent routing. When you ask a question, the system automatically decides whether to search arXiv scientific papers, Wikipedia for general knowledge, or use the Tavily search API for current information based on the nature of your query.

## Setup

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the `Query_Based_Agent` directory with the following variables:

```
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Usage

### Running the Agent

```bash
python main.py
```

This will start the agent in interactive mode. You can ask questions, and the system will intelligently route your query to the appropriate knowledge source.

### Interactive Mode

The agent runs in interactive mode and will:
- Automatically select the appropriate source for your query
- Show which source was chosen (arXiv, Wikipedia, or Tavily)
- Process your query against that information source
- Present the answer with clear formatting

You can:
- Type `exit` or `quit` to exit the application
- Ask any question and let the router decide which source to use

Example:
```
Your query:
What is the latest research on transformer models?

Processing....
Chosen Source: arxiv
Processing....
Answer:
[Detailed response about transformer models from arXiv papers]

--------------------------------------------------
```

## Components

- `knowledge_rag.py`: Contains the retrieval chains for different knowledge sources including arXiv, Wikipedia, and Tavily
- `main.py`: Implements the router logic and interactive query interface

## Source Selection Logic

The router automatically selects the most appropriate source based on the following criteria:

- **arXiv**: Used for scientific papers, research, academic topics, machine learning, medical research, and educational domains
- **Wikipedia**: Used for factual information, historical data, and encyclopedia-style knowledge
- **Tavily**: Used for current events, news, general web search, and topics not well-covered by academic papers or reference materials

## Technical Implementation

The system uses LangChain's components:
- Retrieval chains built with RunnablePassthrough for efficient data processing
- Specialized retrievers for each source (arXiv, Wikipedia, Tavily)
- Custom prompts tailored to each information source
- Gemini model for both routing decisions and answer generation

## Example Queries and Outputs

### Scientific Research (arXiv)
```
Your query:
What are the latest advances in large language models?

Processing....
Chosen Source: arxiv
Processing....
Answer:
Recent advances in large language models (LLMs) include architectural improvements like mixture-of-experts (MoE), better training techniques such as reinforcement learning from human feedback (RLHF), and innovations in multimodal capabilities allowing models to process text, images, and audio together.
```

### General Knowledge (Wikipedia)
```
Your query:
What was the impact of the Industrial Revolution?

Processing....
Chosen Source: wikipedia
Processing....
Answer:
The Industrial Revolution, which began in the late 18th century, transformed economies from agrarian to industrial, introduced mechanized manufacturing, steam power, and factory systems. Its impacts included urbanization, improved living standards, technological innovation, but also pollution, poor working conditions, and social inequality.
```

### Current Information (Tavily)
```
Your query:
What are the latest developments in renewable energy technology?

Processing....
Chosen Source: tavily
Processing....
Answer:
Recent developments in renewable energy technology include advanced perovskite solar cells achieving higher efficiency rates, floating offshore wind farms expanding global capacity, improved energy storage solutions like solid-state batteries, green hydrogen production scaling up, and AI optimization of grid management systems.
```
