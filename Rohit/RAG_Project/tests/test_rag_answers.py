from rag.qa_engine import get_rag_chain


def test_policy_waiting_period():
    rag = get_rag_chain()

    question = "What is the waiting period for health insurance?"
    result = rag(question)

    answer = result["answer"]
    sources = result["context"]

    # 1️⃣ Validate answer content
    assert "waiting period" in answer.lower()

    # 2️⃣ Validate source is not empty
    assert len(sources) > 0

    # 3️⃣ Validate answer is grounded in document
    source_text = sources[0].page_content.lower()
    assert "waiting period" in source_text
