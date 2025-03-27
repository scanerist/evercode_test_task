from fastapi import HTTPException, status

class RandomNumberGenerationError(Exception):
    def __init__(self, message: str = "Could not generate a unique random number after maximum attempts"):
        self.message = message
        super().__init__(self.message)

class RandomNumberNotFoundError(HTTPException):
    def __init__(self, id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Random number with id={id} not found"
        )

class RandomNumberServiceError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Service error: {detail}"
        )