import time
from app.contact_channel.infrastructure.redis.queue import RedisQueue
from app.contact_channel.domain.services.dispatcher_factory import DispatcherFactory

class GenericWorker:
    def __init__(self, redis_client):
        self.queue = RedisQueue(redis_client)

    def process(self):
        print("[GENERIC WORKER] Started. Processing jobs...")
        while True:
            job = self.queue.dequeue()
            if job:
                dispatcher = DispatcherFactory.get_dispatcher(job['channel'])
                if not dispatcher:
                    print(f"No dispatcher for channel: {job['channel']}")
                    continue
                dispatcher.dispatch(job['channel'], job['to'], job['message'])
            time.sleep(1)
