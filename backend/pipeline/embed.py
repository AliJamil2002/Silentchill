from langchain_huggingface import HuggingFaceEmbeddings
from config import settings


def get_embeddings(provider: str):
   
    if provider == settings.embedding_provider:
      return HuggingFaceEmbeddings(model_name=settings.embedding_model)
