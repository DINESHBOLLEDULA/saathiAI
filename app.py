from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
# Uncomment the following if you want audio-to-text using OpenAI later
# from openai import OpenAI
# import os

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Farmer WhatsApp Bot is Live"

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form.get('Body', '')
    num_media = int(request.form.get('NumMedia', 0))
    resp = MessagingResponse()

    if num_media > 0:
        media_url = request.form.get('MediaUrl0')
        media_type = request.form.get('MediaContentType0')

        # If user sends an image
        if media_type and media_type.startswith("image/"):
            resp.message("📸 Got your image! Processing it now...")
            image_data = requests.get(media_url).content
            with open("received_image.jpg", "wb") as f:
                f.write(image_data)
            print(f"✅ Saved image from: {media_url}")

        # If user sends audio or voice note (for future)
        elif media_type and media_type.startswith("audio/"):
            resp.message("🎤 Got your voice message! We'll convert it to text soon.")
            audio_data = requests.get(media_url).content
            with open("voice.ogg", "wb") as f:
                f.write(audio_data)
            print(f"✅ Saved audio from: {media_url}")

        else:
            resp.message(f"Received media of type: {media_type}")

    else:
        resp.message(f"Farmer query received: {incoming_msg}")

    return str(resp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
