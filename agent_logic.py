def generate_response(user_input):
    """
    Simulate a response from an LLM with a friendly, human-like tone ("Bland tone").
    """
    user_input = user_input.lower()

    if "hours" in user_input:
        return "Sure! Our business hours are 9 AM to 6 PM, Monday through Friday."
    elif "pricing" in user_input or "cost" in user_input:
        return "Great question. Our pricing depends on your needs, but we offer flexible monthly plans starting at $99."
    elif "speak to someone" in user_input:
        return "Absolutely — I’ll connect you with a team member now."
    elif "thank you" in user_input:
        return "You're very welcome! Is there anything else I can help with today?"
    else:
        return "Got it! I’m here to help — could you tell me a bit more so I can better assist you?"
