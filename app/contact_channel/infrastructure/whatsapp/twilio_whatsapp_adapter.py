from app.contact_channel.domain.services.dispatcher import Dispatcher
from twilio.rest import Client
from config import settings
import json

class TwilioWhatsAppDispatcher(Dispatcher):
    def dispatch(self, channel: str, to: str, message: str) -> bool:
        if channel != 'whatsapp':
            raise ValueError('Unsupported channel for this dispatcher')
        # Here you would integrate with Twilio's API
        print(f"[MOCK] Sending WhatsApp to {to}: {message}")
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        variables = {'1': message}
        
        message = client.messages.create(
        from_=settings.WHATSAPP_FROM,
        content_sid='HXe3549040d79d202d3b3beed5ab4a73f9', #template
        content_variables = json.dumps(variables),
        to=f'whatsapp:{to}'
        )
    

        print(message.sid)
        return True 