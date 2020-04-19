import smtplib
from email.message import EmailMessage
import time

rec = ['youflox@gmail.com', 'ratna.roy999@gmail.com']
h = (time.strftime('%d %b, %H:%M'))


def send(text):
    sender = 'nanda.tr4@gmail.com'
    password = 'Nanda@@12'

    msg = EmailMessage()
    msg['Subject'] = f"Stock Price {h}"
    msg['From'] = sender
    msg['To'] = rec
    msg.set_content(text)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server :
        server.login(sender, password)

        server.send_message(msg)
    print(f'Email sent to {rec} at {time.strftime("%x %X")}')
