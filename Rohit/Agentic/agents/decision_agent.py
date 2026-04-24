def decision_engine(intent: str) -> str:
    mapping = {
        "INSTALL_WIFI": "CHECK_AVAILABILITY",
        "INTERNET_DOWN": "CHECK_OUTAGE"
    }
    return mapping.get(intent, "ESCALATE")