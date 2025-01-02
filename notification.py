import os
from twilio.rest import Client
import smtplib

MY_EMAIL = "your_mail"
PASSWORD = "your_password"

account_sid = 'your_sid'
auth_token = 'your_tpken_key'

class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

        def send_sms(self, message_body):

            message = self.client.messages.create(
            from_=os.environ["FROM_TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TO_TWILIO_VIRTUAL_NUMBER"]
        )
        print(message.sid)

    
    def send_mail(self, customer_data, email_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            for customer in customer_data:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=customer,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )

