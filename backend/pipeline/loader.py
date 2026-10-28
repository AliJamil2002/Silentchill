from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


def load_doc(directory_path: str):
    loader = DirectoryLoader(
        directory_path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()
    return documents