from twilio.rest import Client

account_sid = 'ACd5b0197532b5170656ff145fe4f411d0'
auth_token = '567a9a0caf5b348f60ad8215fa4da43f'
client = Client(account_sid, auth_token)


def send():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Krishna Kant Hati\nCoder\nwww.superlikes.herokuapp.com',
        to='whatsapp:+918217243741'
    )

    print(message.sid)
