from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.contact_channel.application.commands.contact_lead import ContactLeadCommand
from app.contact_channel.interfaces.schemas.abandoned_cart_event import AbandonedCartEvent
from app.config import settings
import json
from redis import Redis
from app.contact_channel.infrastructure.redis.queue import RedisQueue, get_redis

router = APIRouter(prefix="/contact", tags=["contact"])

class ContactRequest(BaseModel):
    channel: str
    to: str
    message: str



@router.post("/send")
async def send_contact(
    request: ContactRequest,
    redis: Redis = Depends(get_redis)
):
    queue = RedisQueue(redis)
    contact_lead_command = ContactLeadCommand(queue)
    result = contact_lead_command.execute(request.channel, request.to, request.message)
    return result


@router.post("/webhook/abandoned-cart")
def receive_cart(event: AbandonedCartEvent, redis: Redis = Depends(get_redis)):
    # Serialize and queue
    payload = json.dumps(event.model_dump())
    added = redis.rpush(settings.QUEUE_KEY, payload)
    if not added:
        raise HTTPException(status_code=500, detail="No se pudo encolar el evento")
    return {"status": "enqueued", "position": added}