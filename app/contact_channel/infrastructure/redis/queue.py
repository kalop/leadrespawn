import json
from typing import Optional
from redis import Redis
from app.config import settings
from typing import Generator

def get_redis() -> Generator[Redis, None, None]:
    redis_client = Redis.from_url(settings.REDIS_URL)
    try:
        yield redis_client
    finally:
        redis_client.close()

        
class RedisQueue:
    def __init__(self, redis_client: Redis, queue_key: Optional[str] = None):
        self.redis = redis_client
        self.queue_key = queue_key or settings.QUEUE_KEY

    def enqueue(self, job_data: dict):
        payload = json.dumps(job_data)
        return self.redis.rpush(self.queue_key, payload)

    def dequeue(self, timeout=5):
        # BLPOP returns (key, value) or None
        result = self.redis.blpop([self.queue_key], timeout=timeout)
        if result:
            _, payload = result # type: ignore
            if isinstance(payload, bytes):
                payload = payload.decode("utf-8")
            return json.loads(payload)
        return None 

