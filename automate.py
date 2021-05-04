import os
from twilio.rest import Client

account_sid = 'ACd5b0197532b5170656ff145fe4f411d0'
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
my_whatsapp = os.environ.get('TWILIO_MY_WHATSAPP_NUMBER')

client = Client(account_sid, auth_token)


def send():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Krishna Kant Hati ✔️\nR⭕LLACUBE ❤️',
        to='whatsapp:' + my_whatsapp
    )
    print(message.sid)
