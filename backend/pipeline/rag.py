from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from llm import get_llm
from retrieve import get_retriever


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_rag_pipeline():

    retriever = get_retriever()
    llm = get_llm()

    prompt = ChatPromptTemplate.from_template("""
    You are SilentChill, an AI assistant for pharmaceutical
    cold-chain logistics.

    Answer the question using the provided context.
    Do not invent SOP requirements.
    If the context is insufficient, say so clearly.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """)

    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain



