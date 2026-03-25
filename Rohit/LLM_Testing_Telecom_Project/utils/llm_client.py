def ask_llm(prompt, context=None):
    prompt = prompt.lower()

    # ✅ Context-based handling
    if context == "internet_issue" and "still" in prompt:
        return "Since the issue persists, I will escalate this to technical team."

    # ✅ WiFi / Internet issues
    if "internet" in prompt or "wifi" in prompt:
        return "Please restart your router. If issue persists, we will escalate your issue to technical team."

    # ✅ Recharge issues
    elif "recharge" in prompt:
        return "Please check your payment status. If not resolved, we will raise a ticket."

    # ✅ TV issues
    elif "tv" in prompt or "see" in prompt:
        return "Please check cable connection and restart setup box."

    # ✅ Fallback (Negative Testing)
    else:
        return "Sorry, I didn't understand. Let me connect you to support."

