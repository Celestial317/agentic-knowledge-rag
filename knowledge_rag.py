from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_community.retrievers import ArxivRetriever, TavilySearchAPIRetriever, WikipediaRetriever
from langchain.chains import RetrievalQA, LLMChain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"C:\codesVSCApril\AIMS\Query_Based_Agent\.env")

google_api_key = os.getenv("GOOGLE_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=google_api_key, temperature=0.7)


arxiv_prompt = ChatPromptTemplate.from_template(
    '''You are a research assistant specialized in scientific literature. 
    Based on the following context from arXiv papers, please provide a comprehensive answer to the query.
    
    Context: {context}
    
    Question: {question}
    
    Your response should:
    1. Directly address the query
    2. Include relevant technical details from the papers
    '''
)
arxiv_retriever = ArxivRetriever(
    load_max_docs=4,
    doc_content_chars_max=40000
)
arxiv_chain = (
    {"context": arxiv_retriever, "question": RunnablePassthrough()}
    | arxiv_prompt
    | llm
    | StrOutputParser()
)

wikipedia_prompt = ChatPromptTemplate.from_template('''
Answer the question based only on the context provided using Wikipedia for fact checks.
    Context: {context}
    Question: {question}
''')

wikipedia_retriever = WikipediaRetriever() 

wiki_chain = (
    {"context": wikipedia_retriever, "question": RunnablePassthrough()}
    | wikipedia_prompt
    | llm
    | StrOutputParser()
)


tavily_prompt = ChatPromptTemplate.from_template(
    """Answer the question based only on the context provided using Tavily for search.

Context: {context}

Question: {question}"""
)

tavily_retriever = TavilySearchAPIRetriever(
    max_results=5,
    api_key=tavily_api_key)

tavily_chain = (
    {"context": tavily_retriever, "question": RunnablePassthrough()}
    | tavily_prompt
    | llm
    | StrOutputParser()
)


