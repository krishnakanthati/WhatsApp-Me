from twilio.rest import Client

account_sid = 'ACd5b0197532b5170656ff145fe4f411d0'
auth_token = 'adfbe7448f8c5d19dbd860fc9c9ef179'
client = Client(account_sid, auth_token)


def send():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Krishna Kant Hati\nCoder www.google.com',
        to='whatsapp:+918217243741'
    )

    print(message.sid)
