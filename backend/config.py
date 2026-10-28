from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # LLM
    groq_api_key: str
    llm_model: str 

    # Embedding
    embedding_provider: str 
    embedding_model: str 

    # Vector database
    qdrant_url: str
    qdrant_api_key: str
    qdrant_collection: str

    chunk_size:int
    chunk_overlap:int

  

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()