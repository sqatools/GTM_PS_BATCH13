"""
Safety Validator Module
Validates LLM responses for safety concerns
"""

UNSAFE_KEYWORDS = [
    "hack", "crash", "error", "bug", "attack", "malicious",
    "exploit", "vulnerability", "injection", "overflow"
]

def check_response_safety(response):
    """
    Check if response contains any unsafe content
    
    Args:
        response (str): The LLM response to validate
        
    Returns:
        tuple: (bool: is_safe, str: message)
    """
    if not response:
        return False, "Empty response - Safety check failed"
    
    response_lower = response.lower()
    
    # Check for unsafe keywords
    unsafe_found = []
    for keyword in UNSAFE_KEYWORDS:
        if keyword in response_lower:
            unsafe_found.append(keyword)
    
    if unsafe_found:
        return False, f"Unsafe content detected: {', '.join(unsafe_found)}"
    
    # Check for reasonable length (not too short)
    if len(response) < 20:
        return False, "Response too brief - may be incomplete"
    
    # Check for proper ending (not truncated)
    if response.strip()[-1] not in ".!?":
        return False, "Response appears to be truncated"
    
    return True, "Safe response - No concerns detected"


def get_response_safety_score(response):
    """
    Get a safety score (0-100) for the response
    
    Args:
        response (str): The LLM response to evaluate
        
    Returns:
        int: Safety score from 0-100
    """
    score = 100
    
    response_lower = response.lower()
    
    # Deduct points for unsafe keywords
    for keyword in UNSAFE_KEYWORDS:
        if keyword in response_lower:
            score -= 20
    
    # Deduct points for suspiciously short responses
    if len(response) < 50:
        score -= 15
    
    # Deduct points if response looks incomplete
    if response.strip()[-1] not in ".!?":
        score -= 10
    
    return max(0, score)
