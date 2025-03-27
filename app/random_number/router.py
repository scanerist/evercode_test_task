from fastapi import APIRouter
from app.random_number.dao import RandomNumberDAO
from app.random_number.schemas import SRandomNumber
from app.random_number.services import generate_random_number
from loguru import logger
from app.exceptions import RandomNumberNotFoundError, RandomNumberServiceError, RandomNumberGenerationError

router = APIRouter(prefix="/random_number", tags=["Random Number"])

@router.post("/generate", response_model=SRandomNumber)
async def generate():
    logger.info("Received request to generate random number")
    try:
        unique_id, number = generate_random_number()
        dao = RandomNumberDAO()
        await dao.add(unique_id, number)
        logger.info(f"Generated random number: id={unique_id}, number={number}")
        return {"id": unique_id, "number": number}
    except RandomNumberGenerationError as e:
        logger.error(f"Failed to generate unique number: {e}")
        raise RandomNumberServiceError(detail=str(e))
    except Exception as e:
        logger.error(f"Error generating random number: {e}")
        raise RandomNumberServiceError(detail=str(e))

@router.get("/retrieve/{id}", response_model=SRandomNumber)
async def retrieve(id: str):
    logger.info(f"Received request to retrieve number with id={id}")
    try:
        dao = RandomNumberDAO()
        number = await dao.find_one_or_none_by_id(id)
        if number is None:
            logger.warning(f"Number with id={id} not found")
            raise RandomNumberNotFoundError(id=id)
        logger.info(f"Retrieved number: id={id}, number={number}")
        return {"id": id, "number": number}
    except Exception as e:
        logger.error(f"Error retrieving number with id={id}: {e}")
        raise RandomNumberServiceError(detail=str(e))