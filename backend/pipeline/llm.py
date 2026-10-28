from langchain_groq import ChatGroq
from config import settings

def get_llm() -> ChatGroq:
    """Initialize and return the Groq language model."""

    llm = ChatGroq(
        model=settings.llm_model,
        api_key=settings.groq_api_key.get_secret_value(),
        temperature=0,
    )

    return llm