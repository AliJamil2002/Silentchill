from langchain_qdrant import QdrantVectorStore
from langchain_core.documents import Document
from pipeline.embed import get_embeddings
from config import settings


def create_vector_store(documents: list[Document]) -> QdrantVectorStore:
    """Store document chunks and embeddings in Qdrant."""
    embeddings = get_embeddings(settings.embedding_provider)

    vector_store = QdrantVectorStore.from_documents(
        documents=documents,
        embedding=embeddings,
        url=settings.qdrant_url,
        api_key=settings.qdrant_api_key,
        collection_name=settings.qdrant_collection,
    )
    return vector_store

