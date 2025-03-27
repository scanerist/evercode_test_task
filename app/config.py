from dotenv import load_dotenv
import os


load_dotenv()

def get_redis_config() -> dict:
    return {
        "host": os.getenv("REDIS_HOST", "localhost"),
        "port": int(os.getenv("REDIS_PORT", 6379)),
        "db": int(os.getenv("REDIS_DB", 0)),
        "decode_responses": True
    }