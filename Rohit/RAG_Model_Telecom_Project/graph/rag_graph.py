from langgraph.graph import StateGraph
from typing_extensions import TypedDict, Optional
from rag.loader import load_documents
from rag.splitter import split_docs
from rag.embeddings import get_embeddings
from rag.vector_store import create_vector_store
from rag.retriever import get_retriever
from rag.generator import generate_response

class State(TypedDict, total=False):
    query: str
    retriever: object
    docs: list
    response: str

def retrieve(state):
    query = state.get("query", "")
    retriever = state.get("retriever")
    if not retriever or not query:
        docs = []
    else:
        docs = retriever.get_relevant_documents(query)
    return {"docs": docs}

def generate(state):
    query = state.get("query", "")
    docs = state.get("docs", [])
    response = generate_response(query, docs)
    return {"response": response}

def build_graph():
    docs = load_documents()
    split = split_docs(docs)
    emb = get_embeddings()
    vs = create_vector_store(split, emb)
    retriever = get_retriever(vs)

    graph = StateGraph(State)

    graph.add_node("retrieve", retrieve)
    graph.add_node("generate", generate)

    graph.set_entry_point("retrieve")

    graph.add_edge("retrieve", "generate")

    app = graph.compile()

    return app, retriever