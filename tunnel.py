from pyngrok import ngrok

# Start a tunnel on port 5000
public_url = ngrok.connect(5000)
print("Public URL:", public_url)
