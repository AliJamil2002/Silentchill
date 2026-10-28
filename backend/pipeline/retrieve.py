from pipeline.loader import load_doc
from pipeline.spliter import get_splitter
from pipeline.vectore import create_vector_store
from pipeline.bm25 import bm25_retriever
from langchain_classic.retrievers import EnsembleRetriever


def get_retriever():

    # Step 1: Load PDFs
    documents = load_doc("data")

    # Step 2: Split documents into chunks
    splitter = get_splitter()
    chunks = splitter.split_documents(documents)

    # Step 3: Create vector store
    vector_store = create_vector_store(chunks)

    # Step 4: Create vector retriever
    vector_retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    # Step 5: Create BM25 retriever
    keyword_retriever = bm25_retriever(chunks)

    # Step 6: Combine retrievers
    ensemble_retriever = EnsembleRetriever(
        retrievers=[vector_retriever, keyword_retriever],
        weights=[0.5, 0.5]
    )

    return ensemble_retriever