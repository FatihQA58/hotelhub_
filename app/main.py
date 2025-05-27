from fastapi import FastAPI
from app.routers import user_router, hotel_router, booking_router, review_router, review_over_gast_router
from app.db.database import Base, engine

# Maak de database-tabellen aan (indien nog niet aangemaakt)
Base.metadata.create_all(bind=engine)

# Initieer de FastAPI-applicatie
app = FastAPI(
    title="HotelHub API",
    version="0.1.0",
    description="Een API voor gebruikersregistratie, hotelbeheer en reserveringen."
)

# Verbind routers met het hoofdprogramma
app.include_router(user_router.router)
app.include_router(hotel_router.router)
app.include_router(booking_router.router)
app.include_router(review_router.router)
app.include_router(review_over_gast_router.router)
