from ..main import ask
from ..utils.validator import validate_response

def test_response():
    query = "Internet not working"
    response = ask(query)

    print("\n================ FINAL RESPONSE VALIDATION ================")
    print(f"🔹 Customer Query  : {query}")
    print(f"🔹 Model Response  : {response}")

    result = validate_response(query, response)

    print("\n🔍 Validation Results:")
    for key, value in result.items():
        print(f"   {key.upper()} : {'✅ PASS' if value else '❌ FAIL'}")

    assert result["correctness"]
    assert result["relevance"]
    assert result["completeness"]