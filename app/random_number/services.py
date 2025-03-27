import random
import uuid
from app.dao.redis_base import redis_client
from loguru import logger
from app.exceptions import RandomNumberGenerationError

def generate_random_number() -> tuple[str, int]:
    logger.info("Generating a unique random number")
    max_attempts = 100
    for attempt in range(max_attempts):
        number = random.randint(1, 1000)
        if not redis_client.sismember("generated_numbers", number):
            unique_id = str(uuid.uuid4())
            redis_client.sadd("generated_numbers", number)
            logger.info(f"Generated unique number: {number} with id={unique_id}")
            return unique_id, number
        logger.debug(f"Number {number} already exists, attempt {attempt + 1}/{max_attempts}")
    logger.error("Failed to generate a unique number after maximum attempts")
    raise RandomNumberGenerationError()