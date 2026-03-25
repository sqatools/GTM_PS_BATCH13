import requests
import time
from config import RAG_API_URL

def get_rag_response(query):
    try:
        start_time = time.time()

        response = requests.post(
            RAG_API_URL,
            json={"query": query}
        )

        latency = time.time() - start_time

        if response.status_code == 200:
            return response.json(), latency
        else:
            return {"answer": "API Error", "escalation": "L2"}, latency

    except Exception as e:
        return {"answer": str(e), "escalation": "L2"}, 0

#python -m tests.test_rag_responses--> scripts to run     