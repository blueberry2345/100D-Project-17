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
list_status, messages = imap.select(None, "ALL")

# If successful, then get a list of email IDs from inbox. Otherwise, print error message.
if list_status == "OK":
    email_id_list = messages[0].split()
    # For each email, get the
    for id in email_id_list:
        email_status, message = imap.fetch(id, "(RFC822)")
        if email_status == "OK":
            content = message.get_payload(decode=True).decode()
            sender = message.get("From")
            subject = decode_header(message["Subject"])[0]
            # Generate a response to the message and send email
            response = AI_assistant.respond(content)
            emailer.send_email(sender, "RE: {subject}", response)
        else:
            print(f"ERROR: Email {id} could not be fetched.")


else:
    print("ERROR: Inbox Emails could not be retrieved.")