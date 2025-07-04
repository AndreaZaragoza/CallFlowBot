import json
from datetime import datetime

def log_interaction(user_input, bot_response, session_id):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "session_id": session_id,
        "user_input": user_input,
        "bot_response": bot_response
    }

    try:
        with open("interaction_log.json", "a") as logfile:
            logfile.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        print(f"Logging error: {e}")
