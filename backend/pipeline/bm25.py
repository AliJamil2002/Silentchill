from langchain_community.retrievers import BM25Retriever
from langchain_core.documents import Document


def bm25_retriever(chunks: list[Document]) -> BM25Retriever:
    bm25 = BM25Retriever.from_documents(chunks, k=5)
    return bm25