from graph.rag_graph import build_graph

_app = None
_retriever = None

def _initialize():
    global _app, _retriever
    if _app is None:
        _app, _retriever = build_graph()
    return _app, _retriever

def ask(query):
    app, retriever = _initialize()
    result = app.invoke({
        "query": query,
        "retriever": retriever
    })
    return result["response"]

if __name__ == "__main__":
    print(ask("Internet not working"))