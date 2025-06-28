
from app.contact_channel.schemas.abandoned_cart import AbandonedCartRequest


class AbandonedCartWhatsappCommand:
    def __init__(self, queue):
        self.queue = queue

    def execute(self, abandonedCart: AbandonedCartRequest):
        job = {"channel": channel, "to": to, "message": message}
        self.queue.enqueue(job)
        return {"status": "enqueued"}


