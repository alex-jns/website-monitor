import smtplib
from email.message import EmailMessage

def send_alert(result):
    msg = EmailMessage()
    msg.set_content(f"Site DOWN: {result['url']}\nError: {result.get('error')}")

    msg["Subject"] = "Website Alert"
    msg["From"] = "monitor@example.com"
    msg["To"] = "you@example.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("user", "password")
        server.send_message(msg)