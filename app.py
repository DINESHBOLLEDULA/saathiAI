from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Farmer Assistant WhatsApp Bot is live!"

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    # Get incoming WhatsApp message
    incoming_msg = request.form.get('Body', '').strip().lower()
    from_number = request.form.get('From', '')

    print(f"Message from {from_number}: {incoming_msg}")

    # Define some simple keyword-based replies (you can expand this or replace with AI)
    responses = {
        "hello": "Hello 👋! I’m your Farmer Assistant. How can I help you today?",
        "hi": "Hi! Tell me your problem in any language.",
        "crop": "Please tell me your crop name and issue (pest, soil, fertilizer, etc).",
        "thanks": "You’re welcome! 🌾"
    }

    # Default fallback reply if keyword not found
    reply_text = responses.get(incoming_msg, f"Farmer query received: {incoming_msg}. We’ll analyze and respond soon.")

    # Create Twilio WhatsApp response
    resp = MessagingResponse()
    msg = resp.message(reply_text)
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
