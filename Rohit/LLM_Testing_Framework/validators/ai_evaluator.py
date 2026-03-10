from clients.llm_client import send_prompt

def evaluate_answer(question, answer):

    prompt = f"""
    Question: {question}
    Answer: {answer}

    Score answer accuracy from 1 to 10.
    """

    score = send_prompt(prompt)

    return score