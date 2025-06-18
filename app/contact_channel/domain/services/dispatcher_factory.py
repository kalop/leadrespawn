from app.contact_channel.infrastructure.whatsapp.twilio_adapter import TwilioWhatsAppDispatcher

class DispatcherFactory:
    def __init__(self):
        self.dispatchers = {
            'whatsapp': TwilioWhatsAppDispatcher(),
            # 'sms': TwilioSMSDispatcher(),
            # 'email': EmailDispatcher(),
        }

    def get(self, channel: str):
        return self.dispatchers.get(channel)

    @staticmethod
    def get_dispatcher(channel: str):
        dispatcher_factory = DispatcherFactory()
        return dispatcher_factory.get(channel)