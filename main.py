import os
from emailer import Emailer
from helper import Helper
import imaplib

openai_key = os.getenv("API_KEY")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

on = True


AI_assistant = Helper(openai_key)

# imap login
imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(email, password)
imap.select("inbox")
status, messages = imap.select(None, "ALL")
email_id_list = messages[0].split()

for id in email_id_list:
    status, data = imap.fetch(id, "(RFC822)")

    for part in data:
        if isinstance(part, tuple):
            message = email.message_from_bytes(part[1])




