from langchain_openai import ChatOpenAI
from utils.prompt import get_prompt

_llm = None

def _get_llm():
    global _llm
    if _llm is None:
        _llm = ChatOpenAI(temperature=0)
    return _llm

def generate_response(query, docs):
    # ✅ Edge Case Handling (Empty Context)
    if not docs:
        return "Sorry, I don't have enough information. Please contact support."

    # ✅ Build Context
    context = "\n".join([doc.page_content for doc in docs])

    # ✅ Prompt Creation
    prompt = get_prompt(context, query)

    # ✅ Generate Response
    llm = _get_llm()
    response = llm.predict(prompt)

    return response