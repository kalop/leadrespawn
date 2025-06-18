from abc import ABC, abstractmethod

class Dispatcher(ABC):
    @abstractmethod
    def dispatch(self, channel: str, to: str, message: str) -> bool:
        """Send a message via the specified channel (e.g., whatsapp, sms, email)."""
        pass 