import redis
from app.config import get_redis_config

redis_config = get_redis_config()
redis_client = redis.Redis(**redis_config)