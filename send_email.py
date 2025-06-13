import smtplib, ssl
import os
from email.message import EmailMessage


def send_email(email: EmailMessage):
    host = "smtp.gmail.com"
    port = 465

    """
    enter your own email; make an app password from gmail;
    add it to system environments on windows
    """
    username = "your_own_email" # enter your email
    password = os.getenv("PASSWORD")

    receiver = "your_own_email"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(email)
        # server.sendmail(username, receiver, message)