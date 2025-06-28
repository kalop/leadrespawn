
class ContactLeadCommand:
    def __init__(self, queue):
        self.queue = queue

    def execute(self, channel: str, to: str, message: str):
        job = {"channel": channel, "to": to, "message": message}
        self.queue.enqueue(job)
        return {"status": "enqueued"}