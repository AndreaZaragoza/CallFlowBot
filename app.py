import json
from flask import Flask, request, jsonify
from agent_logic import generate_response
from flask import render_template
from logger import log_interaction
import os
from collections import Counter

app = Flask(__name__)

import logging

logging.basicConfig(filename='callflowbot.log', level=logging.INFO)

@app.route("/twilio-webhook", methods=["POST"])
def twilio_webhook():
    data = request.get_json()
    user_message = data.get("transcript", "")

    if not user_message:
        return jsonify({"error": "Missing 'transcript' in request."}), 400

    print(f"Received: {user_message}")

    logging.info(f"User said: {user_message}")  # basic logging to capture user input

    response = generate_response(user_message)
    log_interaction(user_message, response)  # Phase 3 logging system to track user inputs and bot replies
    print(f"Response: {response}")  # debugging / troubleshooting not getting output when run curl command
    return jsonify({"response": response})

@app.route("/")
def home():
    return "CallFlowBot is running."

@app.route("/chat")
def chat_ui():
    return render_template("index.html")

@app.route("/logs")
def show_logs():
    try:
        with open("interaction_log.json", "r") as f:
            lines = f.readlines()[-10:]  # show last 10
            logs = [json.loads(line.strip()) for line in lines]
    except FileNotFoundError:
        logs = []

    return render_template("logs.html", logs=logs)


@app.route("/dashboard")
def dashboard():
    try:
        with open("interaction_log.json", "r") as f:
            logs = [json.loads(line.strip()) for line in f.readlines()]
    except FileNotFoundError:
        logs = []

    total = len(logs)
    fallback = sum(1 for log in logs if "fallback" in log["bot_response"].lower())
    fallback_pct = round((fallback / total * 100), 1) if total else 0

    user_inputs = [log["user_input"].strip().lower() for log in logs]
    top_questions = Counter(user_inputs).most_common(3)

    return render_template("dashboard.html", total=total, fallback=fallback, fallback_pct=fallback_pct, top_questions=top_questions)

# Update to use the Render assigned port

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))  # fallback to 5001 for local dev
    app.run(host="0.0.0.0", port=port, debug=True)

'''
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Adding port 5001 here because my previous request to localhost:5000, is going to AirPlay, not my Flask app
                                    # Apple's AirPlay service uses port 5000 by default on macOS
'''
