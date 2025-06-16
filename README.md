# 📞 CallFlowBot

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Deployment](https://img.shields.io/badge/Deployed-Render-green)

**CallFlowBot** is a simulated AI call agent built with Flask and OpenAI's API. It mimics Twilio-style webhook interactions, provides LLM-style responses with fallback logic, and features a full web UI — now live and deployable.

### 🔗 [Live Demo](https://callflowbot.onrender.com/chat)

---

## 🧠 What It Does

* Accepts user transcripts via a browser UI or direct POST to `/twilio-webhook`
* Responds in a warm, helpful "Bland tone" using OpenAI’s GPT model
* Falls back to scripted logic if the LLM API is unavailable
* Logs every user message + bot response to a `.json` file
* Styled, modular, and cleanly structured with frontend + backend separation

---

## 💻 Tech Stack

* **Flask** for the backend API and routing
* **HTML / JS / CSS** for the frontend
* **OpenAI API** for LLM-style dynamic replies
* **Python logging + JSON** for simple audit tracking

---

## 🚀 Features by Phase

| Phase  | Description                                        |
| ------ | -------------------------------------------------- |
| `v1.0` | Scripted backend logic for basic AI simulation     |
| `v1.1` | Added OpenAI integration with fallback support     |
| `v2.0` | Web UI with live user input and dynamic replies    |
| `v3.0` | Logging system with `.json` output per interaction |
| `v4.0` | **Live deployment to Render** with public link     |

---

## 🌁 Preview

[![Preview](callflowbot-preview.png)](https://callflowbot.onrender.com/chat)

<!-- ![Preview UI](callflowbot-preview.png) -->

---

## 📜 How to Run Locally

```bash
git clone https://github.com/AndreaZaragoza/CallFlowBot.git
cd CallFlowBot

# Create .env file and add your OpenAI key:
echo "OPENAI_API_KEY=sk-..." > .env

pip install -r requirements.txt
python app.py
```

Visit [http://localhost:5001/chat](http://localhost:5001/chat)

---

## 📂 Sample API Call

```bash
curl -X POST http://localhost:5001/twilio-webhook \
-H "Content-Type: application/json" \
-d '{"transcript": "Can you tell me your pricing?"}'
```

---

## 🔮 What’s Next?

* `/logs` route for live log viewer
* Analytics dashboard (most common questions, fallback rate)
* Download `.csv` export of logs
* User sessions or "caller ID" mode

---

<br>
<br>
<br>
<br>


# CallFlowBot (v1.1)
A minimal AI call agent demo built with Flask. It simulates the behavior of a voice assistant that responds with helpful, human-like answers; designed to reflect real-world AI integrations like those used in customer service automation. Built as a sample project to demonstrate my interest in AI deployment, API integrations, and user-centric design.

**CallFlowBot** is a simulated AI call agent demo built with Flask. It mimics the behavior of a voice-based AI assistant by processing a mock Twilio webhook request and generating friendly, human-like responses.

## 🧠 Features
- REST endpoint to simulate voice-to-text interaction
- Hard-coded logic that emulates LLM behavior using a warm, helpful tone
- Mock integration with Twilio-style POST data

## 🚀 How It Works
1. Send a POST request to `/twilio-webhook` with a JSON body containing a `transcript`.
2. The app processes it and returns a helpful response.
3. Try different phrases like "What are your hours?", "How much does it cost?", or "Thank you."

## 📦 Example
Request:
```json
{
  "transcript": "Can you tell me your pricing?"
}
```

## Diagram

```
+--------------+         +-----------------------+
|  User input  | ---->   | /twilio-webhook route |
+--------------+         +-----------------------+
                               |
                               v
                   +----------------------+
                   |  agent_logic.py AI   |
                   |  response simulator  |
                   +----------------------+
                               |
                               v
                        +------------+
                        |  Response  |
                        +------------+
```


## LLM Integration
This version of CallFlowBot attempts to use OpenAI's GPT-3.5 API to generate real-time, human-like responses in a friendly “Bland tone.” If API quota is unavailable or fails, the app gracefully falls back to a scripted response engine.

- Uses `openai` Python SDK v1.x
- Custom prompt injected into `system` role
- Scripted fallback ensures consistent response reliability

🔐 API keys are stored securely in a `.env` file (not included in repo).
