from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(user_input):
    # Manual fallback trigger for demo purposes
    if "__trigger_fallback__" in user_input.lower():
        return "Sorry, I'm having trouble responding right now."

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful, human-like AI call assistant named CallFlowBot. Use a warm and conversational tone."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI API error:", e)
        print("Falling back to scripted logic.")
        return fallback_scripted_response(user_input)

# Officially running OpenAI’s live API, yet when ran output was Error code: 429 – insufficient_quota. Although OpenAI API Key is valid
# my account does not have active credits and do not plan to pay for now in order to be able to test this project. Therefore, adding
# the below fallback scripted logic in order to demo AI tone and structure, bot always responds, and have hybrid architecture.

def fallback_scripted_response(user_input):
    user_input = user_input.lower()
    if "hours" in user_input:
        return "Sure! Our business hours are 9 AM to 6 PM, Monday through Friday."
    elif "pricing" in user_input or "cost" in user_input:
        return "Great question. Our pricing depends on your needs, but we offer flexible monthly plans starting at $99."
    elif "speak to someone" in user_input:
        return "Absolutely — I’ll connect you with a team member now."
    elif "thank you" in user_input:
        return "You're very welcome! Is there anything else I can help with today?"
    elif "voice mode enabled" in user_input.lower():
        return "Sure! I’ll speak clearly and slowly now."
    elif "voice mode disabled" in user_input.lower():
        return "Voice mode turned off. I’ll respond normally."
    else:
        return "Got it! I’m here to help — could you tell me a bit more so I can better assist you?"

# V2 In creating second version ran into issue where below code is only compatible with the older version of the openai package, v0.28,
# and my system is running the newer openai package v1.x. The code above should now be compatible and run.

'''
import openai
import os
from dotenv import load_dotenv

load_dotenv()

print("OPENAI KEY LOADED:", openai.api_key[:8])  # Safe to print partial / debugging to see if .env loaded

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(user_input):
    prompt = f"""
You are a friendly and human-like phone assistant named CallFlowBot. Your tone should reflect the "Bland tone": warm, helpful, clear, and human. Respond to the user input conversationally, and keep answers concise unless more detail is needed.

User said: "{user_input}"

How should you respond?
"""
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if you have access
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return completion.choices[0].message["content"].strip()
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Sorry, I'm having trouble responding right now."
'''

# V1 w/ Python logic to process input and return dynamic output

''''
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
'''

