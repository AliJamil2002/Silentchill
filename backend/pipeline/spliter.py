from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import settings


def get_splitter():
    """
    Return the text splitter."""
    return RecursiveCharacterTextSplitter(chunk_size=settings.chunk_size, chunk_overlap=settings.chunk_overlap)