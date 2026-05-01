import redis
import json
from app.config import settings

# Connect to Redis
redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=6379,
    decode_responses=True
)


def get_cache(key: str):
    """
    Fetch cached moderation result.
    """
    data = redis_client.get(key)
    if data:
        return json.loads(data)
    return None


def set_cache(key: str, value: dict, ttl: int = 300):
    """
    Store moderation result in cache (TTL = 5 mins default)
    """
    redis_client.setex(key, ttl, json.dumps(value))