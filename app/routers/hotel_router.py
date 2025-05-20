from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.user_model import User
from app.utils import auth

from app.db.database import SessionLocal
from app.schemas.hotel_schemas import HotelOut, HotelCreate, HotelUpdate, HotelOutWithRooms
from app.crud.hotel_crud import (
    search_hotels,
    create_hotel,
    get_hotel_by_name,
    update_hotel, delete_hotel_by_name
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
@router.get("/search", response_model=List[HotelOutWithRooms])
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
@router.get("/{hotel_name}", response_model=HotelOut)
def get_hotel(hotel_name: str, db: Session = Depends(get_db)):
    hotel = get_hotel_by_name(db, hotel_name)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel is niet gevonden.")
    return hotel

# PUT:update een hotel met naam
@router.put("/{hotel_name}",response_model=HotelOut)
def update_hotel_router(hotel_name:str,hotel_update: HotelUpdate, db: Session = Depends(get_db),current_user=Depends(auth.get_current_user)):
    if current_user.role_id == 2:
        raise HTTPException(status_code=403,detail='Verboden voor u,u moet Hotelbeheerder zijn')
    hotel=update_hotel(db,hotel_name,hotel_update)
    return hotel

# Delete:delete een hotel met naam
@router.delete("/{hotel_name}")
def delete_hotel_router(hotel_name:str,db:Session=Depends((get_db)),current_user=Depends(auth.get_current_user)):
    if current_user.role_id == 2:
        raise HTTPException(status_code=403,detail='Verboden voor u,u moet Hotelbeheerder zijn')
    return delete_hotel_by_name(db,hotel_name)
