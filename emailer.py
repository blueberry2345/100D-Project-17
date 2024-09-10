import smtplib


class Emailer:

    def __init__(self, smtp, email, password, port):
        self.email = email

        self.server = smtplib.SMTP(smtp, port)
        self.server.starttls()

        self.server.login(email, password)



    def send_email(self, recipient, subject, response):
        message = "Subject: {subject}\n\n{body}"
        self.server.sendmail(self.email, recipient, message)
