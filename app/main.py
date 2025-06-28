from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from app.config import settings
from redis import Redis
from app.contact_channel.interfaces.controllers.contact_api import router as contact_router
from app.contact_channel.interfaces.controllers.webhook_whatsapp_api import router as webhook_whatsapp_router
from typing import Generator


# Init
app = FastAPI(title="LeadRespawn Backend")
templates = Jinja2Templates(directory="templates")

# Include routers
app.include_router(contact_router)
app.include_router(webhook_whatsapp_router)




# @app.get("/dashboard", response_class=HTMLResponse)
# def get_dashboard(request: Request, redis: Redis = Depends(get_redis)):
#     """Dashboard endpoint - will be moved to its own controller when ready"""
#     items = redis.lrange(settings.QUEUE_KEY, 0, -1)
#     queue = [json.loads(i) for i in items]
#     return templates.TemplateResponse("dashboard.html", {"request": request, "queue": queue})