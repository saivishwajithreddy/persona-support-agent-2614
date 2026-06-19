from agents.escalation import should_escalate

result = should_escalate(
    "angry",
    "I am very angry about this service"
)

print(result)