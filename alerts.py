# Module that defines a SMTP client session object
import smtplib

# Class that makes it easy to set headers and content
from email.message import EmailMessage

def send_alert(result):

    # Defines an empty email message object
    msg = EmailMessage()

    # Sets the content of the email
    msg.set_content(f"Site DOWN: {result['url']}\nError: {result.get('error')}")

    # Defines the email subject header
    msg["Subject"] = "Website Alert"

    # Sender email address
    msg["From"] = "monitor@example.com"

    # Recipient of the email
    msg["To"] = "you@example.com"

    try:
        # 465 is the standard port for SMTP, 587 for STARTTLS
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("user", "password")
            server.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

result = {
    "url": "https://google.com",
    "status": "down",
    "status_code": "404",
    "latency": "5"
}

send_alert(result)