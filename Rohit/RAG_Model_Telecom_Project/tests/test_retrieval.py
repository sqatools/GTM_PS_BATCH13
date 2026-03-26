from ..graph.rag_graph import build_graph

def test_retrieval():
    app, retriever = build_graph()

    query = "internet issue"
    docs = retriever.get_relevant_documents(query)

    print("\n================ RETRIEVAL TEST ================")
    print(f"🔹 Query : {query}")

    print("\n📄 Retrieved Documents:")
    for i, doc in enumerate(docs):
        print(f"{i+1}. {doc.page_content}")

    assert len(docs) > 0