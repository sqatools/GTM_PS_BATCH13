from ..validations.reasoning_validator import ReasoningValidator


def test_reasoning():

    validator = ReasoningValidator()

    decision = {
        "team": "L1",
        "priority": "HIGH"
    }

    assert validator.validate_reasoning(decision)
