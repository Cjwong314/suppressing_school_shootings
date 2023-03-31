# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure

def text_sender():
    account_sid = "ACa12d9736c34520b6c1abdf0c627de173"
    auth_token = "2eba35dd5d96cf06efdbada2f4a63eb8"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="Hello from Chris",
    from_="+18559373996",
    to="+17207572144"
    )
    print(message.sid)

text_sender()