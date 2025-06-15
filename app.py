from flask import Flask, request, jsonify
from agent_logic import generate_response
from flask import render_template
from logger import log_interaction
import os

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

# Update to use the Render assigned port

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))  # fallback to 5001 for local dev
    app.run(host="0.0.0.0", port=port, debug=True)

'''
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Adding port 5001 here because my previous request to localhost:5000, is going to AirPlay, not my Flask app
                                    # Apple's AirPlay service uses port 5000 by default on macOS
'''
