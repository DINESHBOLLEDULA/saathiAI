from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'
@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form.get('Body')
    resp = MessagingResponse()
    resp.message(f"Farmer query received: {incoming_msg}")
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
