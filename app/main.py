from fastapi import FastAPI,Request
from starlette.responses import HTMLResponse

from app.routers import user_router, hotel_router, booking_router, review_router, room_router
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
app.include_router(user_router.router, prefix="/users", tags=["Gebruikers"])
app.include_router(hotel_router.router, prefix="/hotels", tags=["Hotels"])
app.include_router(room_router.router, prefix="/rooms", tags=["Rooms"])
app.include_router(booking_router.router, prefix="/reservations", tags=["Reservaties"])
app.include_router(review_router.router, prefix="/reviews", tags=["Reviews"])
