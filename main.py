import os
from nntplib import decode_header
from emailer import Emailer
from helper import Helper
import imaplib

# Retrieve environment values
openai_key = os.getenv("API_KEY")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
smtp = os.getenv("SMTP")
email_port = os.getenv("PORT")

# Create Helper and Emailer objects
AI_assistant = Helper(openai_key)
emailer = Emailer(openai_key, email, password, email_port)

# Connect to Email and login.
imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(email, password)

# Get the emails from inbox and then
imap.select("inbox")
status, messages = imap.select(None, "ALL")

# If successful, then get a list of email IDs from inbox
if status == "OK":
    email_id_list = messages[0].split()
    #
    for id in email_id_list:
        status, message = imap.fetch(id, "(RFC822)")
        content = message.get_payload(decode=True).decode()

        # get from
        sender = message.get("From")
        # get subject
        subject = decode_header(message["Subject"])[0]
        response = AI_assistant.respond(content)
        emailer.send_email(sender, "RE: {subject}", response)

