from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from knowledge_rag import arxiv_chain, wiki_chain, tavily_chain
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"C:\codesVSCApril\AIMS\Query_Based_Agent\.env")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3
)

router = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(
        """You are a router. Given a query, return one source based on the query
        If query is history related or need encyclopedia use wikipedia
        if research paper, science, machine learning, medical or any educational domain etc related use arxiv
        if normal facts, search, about nouns, crawling of current scenario, use Tavily
        Just return one word, source: "arxiv", "wikipedia", or "tavily".
        Query: {query}"""
    ),
    output_key="source"
)

chains = {
    "arxiv": arxiv_chain,
    "wikipedia": wiki_chain,
    "tavily": tavily_chain
}

while True:
    q = input("Your query:\n")
    if q.lower() in ["exit", "quit"]:
        break
    print("Processing....")
    s = router.invoke({"query": q})["source"].strip().lower()
    if s not in chains:
        s = "tavily"
    print(f"Chosen Source: {s}")
    print("Processing....")
    print("Answer:")
    print(chains[s].invoke(q))
    print("\n")
    print("--------------------------------------------------")
