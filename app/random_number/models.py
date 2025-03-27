from pydantic import BaseModel, ConfigDict, Field

class RandomNumber(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str = Field(description="Unique ID of random number")
    number: int = Field(description="Random number")