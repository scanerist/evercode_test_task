from pydantic import BaseModel, ConfigDict, Field

class SRandomNumber(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: str = Field(alias="id", description="id of random number")
    number: int = Field(alias="number", description="random number")
