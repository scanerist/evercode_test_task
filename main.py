from fastapi import FastAPI
from app.random_number.router import router as random_number_router

app = FastAPI(title="Random Number API")
@app.get("/")
async def root():
    return {"message": "Welcome to the Random Number API"}
app.include_router(random_number_router)

