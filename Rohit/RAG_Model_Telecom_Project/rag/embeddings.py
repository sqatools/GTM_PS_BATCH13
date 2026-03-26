from langchain_openai import OpenAIEmbeddings

_embeddings = None

def get_embeddings():
    global _embeddings
    if _embeddings is None:
        _embeddings = OpenAIEmbeddings()
    return _embeddings