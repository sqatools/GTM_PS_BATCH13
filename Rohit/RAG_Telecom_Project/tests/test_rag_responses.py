import json
from utils.api_client import get_rag_response
from utils.validator import validate_response
from utils.metrics import calculate_metrics
from config import MAX_RESPONSE_TIME

def run_tests():
    with open("test_data/telecom_queries.json") as f:
        test_cases = json.load(f)

    results = []

    for test in test_cases:
        print(f"\n🔍 Testing Query: {test['query']}")

        response, latency = get_rag_response(test["query"])

        print(f"Response: {response}")
        print(f"Latency: {latency:.2f} sec")

        validation = validate_response(response, test)

        validation["latency_pass"] = latency < MAX_RESPONSE_TIME

        print(f"Validation: {validation}")

        results.append(validation)

    metrics = calculate_metrics(results)

    print("\n📊 Final Metrics:")
    print(metrics)


if __name__ == "__main__":
    run_tests()