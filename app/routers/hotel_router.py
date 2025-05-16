from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.database import SessionLocal
from app.schemas.hotel_schemas import HotelOut, HotelCreate
from app.crud.hotel_crud import (
    search_hotels,
    create_hotel,
    get_hotel_by_id
)

router = APIRouter()

# Zorgt voor een verbinding met de database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET: zoek hotels op basis van stad en kenmerken
@router.get("/search", response_model=List[HotelOut])
def search_hotels_endpoint(
    city: Optional[str] = Query(None, description="Stad of locatie"),
    features: Optional[str] = Query(None, description="Kenmerken gescheiden door komma, bv: wifi,parking"),
    db: Session = Depends(get_db)
):
    feature_list = features.split(",") if features else []
    return search_hotels(db=db, city=city, features=feature_list)

# POST: voeg een nieuw hotel toe
@router.post("/", response_model=HotelOut)
def add_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    return create_hotel(db=db, hotel=hotel)

# GET: haal een specifiek hotel op via ID
@router.get("/{hotel_id}", response_model=HotelOut)
def get_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = get_hotel_by_id(db, hotel_id)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel niet gevonden.")
    return hotel
