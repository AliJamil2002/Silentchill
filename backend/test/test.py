from pipeline.retrieve import get_retriever


def test_get_retriever():
    retriever = get_retriever()

    query = input("Enter your query: ")

    results = retriever.invoke(query)

    for i, doc in enumerate(results, start=1):
        print(f"\nDocument {i}:")
        print(doc.page_content)

    return results


if __name__ == "__main__":
    test_get_retriever()