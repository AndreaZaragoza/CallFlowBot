# CallFlowBot
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
