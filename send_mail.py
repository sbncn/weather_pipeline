import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
from os import getenv


load_dotenv()


def send_email(subject, body):
    # information for e-mail
    from_email = getenv("sender_mail")
    email_key = getenv("email_key")
    to_email = getenv("to_mail")

    # creating e-mail
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # body
    msg.attach(MIMEText(body, 'plain'))

    # connect SMTP
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, email_key)

        # send e-mail
        server.sendmail(from_email, to_email, msg.as_string())