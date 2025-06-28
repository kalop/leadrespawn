from fastapi import APIRouter, Depends
from pydantic import BaseModel
from redis import Redis
from app.contact_channel.application.commands.abandoned_cart_whatsapp import AbandonedCartWhatsappCommand
from app.contact_channel.infrastructure.redis.queue import RedisQueue, get_redis
from app.contact_channel.schemas.abandoned_cart import AbandonedCartRequest

router = APIRouter(prefix="/webhook", tags=["webhook"])



@router.post("/whatsapp/abandoned-cart")
def receive_cart(request: AbandonedCartRequest, redis: Redis = Depends(get_redis)):
    queue = RedisQueue(redis)
    abandoned_cart_whatsapp = AbandonedCartWhatsappCommand(queue)
    result = abandoned_cart_whatsapp.execute(request)
    return result
 