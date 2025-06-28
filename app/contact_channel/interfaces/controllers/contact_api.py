from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.contact_channel.application.commands.contact_lead import ContactLeadCommand
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
