from app.dao.base import BaseDAO
from app.random_number.models import RandomNumber


class RandomNumberDAO(BaseDAO):
    model = RandomNumber