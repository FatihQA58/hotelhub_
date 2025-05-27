from fastapi import HTTPException
from sqlalchemy.orm import Session,joinedload
from typing import List, Optional

from app import models
from app.models.hotel_model import Hotel, Room
from app.schemas.hotel_schemas import HotelCreate, HotelOut, HotelUpdate
from app.utils.auth import get_current_user


# Voeg een nieuw hotel toe aan de database
def create_hotel(db: Session, hotel: HotelCreate) -> Hotel:
    db_hotel = Hotel(**hotel.dict())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

# Update het hotel met naam
def update_hotel(db:Session,hotel_name:str,hotel_update:HotelUpdate):
    hotel=db.query(Hotel).filter(Hotel.name==hotel_name).first()
    if not hotel:
        raise HTTPException(status_code=404,detail='Hotel not found')
    update_data=hotel_update.dict(exclude_unset=True)
    for key,value in update_data.items():
        setattr(hotel,key,value)
    db.commit()
    db.refresh(hotel)
    return hotel


# Zoek hotels op basis van stad en kenmerken
def search_hotels(
    db: Session,
    city: Optional[str] = None,
    features: Optional[List[str]] = None
) -> List[Hotel]:
    query = db.query(Hotel).join(Room)

    # Filter op stad (city)
    if city:
        query = query.filter(Hotel.city.ilike(f"%{city}%"),Room.available==True)

    # Filter op kenmerken (features)
    if features:
        if "wifi" in features:
            query = query.filter(Hotel.has_wifi == True,Room.available==True)
        if "parking" in features:
            query = query.filter(Hotel.has_parking == True,Room.available==True)
        if "breakfast" in features:
            query = query.filter(Hotel.has_breakfast == True,Room.available==True)
        if "pets" in features:
            query = query.filter(Hotel.pet_friendly == True,Room.available==True)

    return query.all()

# Haal een hotel op via zijn naam
def get_hotel_by_name(db: Session, hotel_name: str):
    return db.query(Hotel).filter(Hotel.name == hotel_name).first()

# Delete een hotel op via zijn naam
def delete_hotel_by_name(db: Session, hotel_name: str):
    hotel = db.query(Hotel).filter(Hotel.name == hotel_name).first()

    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")

    db.delete(hotel)
    db.commit()
    return {"detail": f"Hotel '{hotel_name}' deleted"}
