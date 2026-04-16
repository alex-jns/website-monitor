# Imports the Simple Mail Transfer Protocol (SMTP) client to send emails
import smtplib

# Imports the class used to manage email structure like header and body
from email.message import EmailMessage

# Import operating system library
import os

# Imports the loader for .env files
from dotenv import load_dotenv

load_dotenv()

# Defines a function that takes the result of a website query as an argument
def send_alert(result):

    # Creates a new email message object
    msg = EmailMessage()

    # Sets the body of the email to the results of the query (alert)
    msg.set_content(f"Site DOWN: {result['url']}\nError: {result.get('error')}")

    # Sets the header of the email
    msg["Subject"] = "Website Alert"

    # Sets the sender address
    msg["From"] = os.getenv("EMAIL_SENDER")

    # Sets the recipient address
    msg["To"] = os.getenv("EMAIL_RECIPIENT")

    # Establishes a connection to the Gmail SMTP server on port 587
    with smtplib.SMTP("smtp.gmail.com", 587) as server:

        # Puts SMTP connection in Transport Layer Security (TLS) to encrypt
        server.starttls()

        # Authenticates using credentials 
        server.login(os.getenv("EMAIL_SENDER"), os.getenv("EMAIL_PASS"))

        # Sends the email
        server.send_message(msg)
