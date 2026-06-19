def detect_persona(message):

    text = message.lower()

    if "angry" in text or "worst" in text:
        return "angry"

    elif "api" in text or "sdk" in text:
        return "technical"

    elif "new" in text or "beginner" in text:
        return "beginner"

    else:
        return "business"