from app.contact_channel.domain.services.dispatcher import Dispatcher
from twilio.rest import Client
from config import settings

class TwilioSMSDispatcher(Dispatcher):
    def dispatch(self, channel: str, to: str, message: str) -> bool:
        if channel != 'sms':
            raise ValueError('Unsupported channel for this dispatcher')
        # Here you would integrate with Twilio's API
        print(f"[MOCK] Sending sms to {to}: {message}")
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_=settings.SMS_FROM,
        to=to,
        body= f'Hey! You forgot something in your cart 😊 Need any help to complete your order? You can check your cart here: {message}'
        )

        print(message.sid)
        return True 