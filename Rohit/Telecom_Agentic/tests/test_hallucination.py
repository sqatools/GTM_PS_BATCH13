from ..validations.hallucination_validator import HallucinationValidator


def test_hallucination():

    validator = HallucinationValidator()

    response = "This is correct response"

    assert validator.validate(response)
