
from fastapi import FastAPI
from app.routers import review

app = FastAPI(title="HotelHub Merged Full API")

app.include_router(review.router, prefix="/reviews", tags=["Reviews"])
