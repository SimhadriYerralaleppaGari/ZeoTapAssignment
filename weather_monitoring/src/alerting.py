import smtplib
from email.message import EmailMessage

class AlertSystem:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send_alert(self, recipient, subject, body):
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = self.email
        msg['To'] = recipient

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.email, self.password)
            smtp.send_message(msg)

    def temperature_alert(self, city, temperature):
        subject = f"High Temperature Alert for {city}"
        body = f"The temperature in {city} has exceeded the threshold. Current temperature: {temperature}°C"
        self.send_alert('recipient@example.com', subject, body) 
