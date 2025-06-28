from app.contact_channel.domain.services.dispatcher import Dispatcher
from twilio.rest import Client
from config import settings

class TwilioWhatsAppDispatcher(Dispatcher):
    def dispatch(self, channel: str, to: str, message: str) -> bool:
        if channel != 'whatsapp':
            raise ValueError('Unsupported channel for this dispatcher')
        # Here you would integrate with Twilio's API
        print(f"[MOCK] Sending WhatsApp to {to}: {message}")
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_=settings.WHATSAPP_FROM,
        content_sid='HX350d429d32e64a552466cafecbe95f3c', #template
        content_variables='{"1":"12/1","2":"3pm"}',
        to=settings.WHATSAPP_TO
        )

        print(message.sid)
        return True 