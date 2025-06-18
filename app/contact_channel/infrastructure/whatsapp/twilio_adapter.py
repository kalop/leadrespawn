from app.contact_channel.domain.services.dispatcher import Dispatcher

class TwilioWhatsAppDispatcher(Dispatcher):
    def dispatch(self, channel: str, to: str, message: str) -> bool:
        if channel != 'whatsapp':
            raise ValueError('Unsupported channel for this dispatcher')
        # Here you would integrate with Twilio's API
        print(f"[MOCK] Sending WhatsApp to {to}: {message}")
        return True 