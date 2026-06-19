def should_escalate(persona, message):

    if persona == "angry":
        return True

    if "legal" in message.lower():
        return True

    if "lawsuit" in message.lower():
        return True

    return False