from typing import TypeVar, Type
from loguru import logger
from app.dao.redis_base import redis_client

T = TypeVar("T")

class BaseDAO:
    model: Type[T] = None

    def __init__(self):
        if self.model is None:
            raise ValueError("Model must be set in child class")
        self._redis = redis_client

    async def add(self, key: str, value: int) -> None:
        logger.info(f"Adding {self.model.__name__} with key: {key}, value: {value}")
        try:
            self._redis.set(key, value)
            logger.info(f"{self.model.__name__} added successfully.")
        except Exception as e:
            logger.error(f"Error while adding: {e}")
            raise

    async def find_one_or_none_by_id(self, data_id: str) -> int | None:
        try:
            value = self._redis.get(data_id)
            log_message = f"Record {self.model.__name__} with ID {data_id} {'found' if value else 'not found'}."
            logger.info(log_message)
            return int(value) if value is not None else None
        except Exception as e:
            logger.error(f"Error while finding record with ID {data_id}: {e}")
            raise