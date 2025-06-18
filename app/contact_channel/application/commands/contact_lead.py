from app.contact_channel.domain.services.dispatcher_factory import DispatcherFactory

class ContactLeadCommand:
    def __init__(self, queue):
        self.queue = queue

    def execute(self, channel: str, to: str, message: str):
        job = {"channel": channel, "to": to, "message": message}
        self.queue.enqueue(job)
        return {"status": "enqueued"}

def contact_lead(channel, to, message, queue):
    job = {"channel": channel, "to": to, "message": message}
    queue.enqueue(job)  # This puts the job in Redis
