def evaluate_quality(response):
    if len(response) > 20:
        return "Good"
    return "Poor"