import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Port and  host
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", 8000))

    # Redis URL (or fallback in-memory)
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")

    # Twilio WhatsApp credentials
    TWILIO_ACCOUNT_SID: str = os.getenv("TWILIO_ACCOUNT_SID", "")
    TWILIO_AUTH_TOKEN: str = os.getenv("TWILIO_AUTH_TOKEN", "")
    WHATSAPP_FROM: str = os.getenv("WHATSAPP_FROM", "")
    WHATSAPP_TO: str = os.getenv("WHATSAPP_TO", "")

    # Metta
    WHATSAPP_ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN", "")
    WHATSAPP_PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID ", "")

    QUEUE_KEY = "leadrespawn:queue"

settings = Settings()