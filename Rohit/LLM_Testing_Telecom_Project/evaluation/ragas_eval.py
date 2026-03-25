def evaluate_relevance(question, answer):
    if question.split()[0].lower() in answer.lower():
        return 0.8
    return 0.5