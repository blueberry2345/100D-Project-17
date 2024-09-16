import smtplib


class Emailer:

    def __init__(self, smtp, email, password, port):
        self.email = email

        self.server = smtplib.SMTP(smtp, port)
        self.server.starttls()

        self.server.login(email, password)


    # Function that sends an email
    def send_email(self, recipient, subject, response):
        message = f"Subject: {subject}\n\n{response}"
        self.server.sendmail(self.email, recipient, message)
