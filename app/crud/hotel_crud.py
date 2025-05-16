from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.hotel_model import Hotel
from app.schemas.hotel_schemas import HotelCreate

# Voeg een nieuw hotel toe aan de database
def create_hotel(db: Session, hotel: HotelCreate) -> Hotel:
    db_hotel = Hotel(**hotel.dict())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

# Zoek hotels op basis van stad en kenmerken
def search_hotels(
    db: Session,
    city: Optional[str] = None,
    features: Optional[List[str]] = None
) -> List[Hotel]:
    query = db.query(Hotel)

    # Filter op stad (city)
    if city:
        query = query.filter(Hotel.city.ilike(f"%{city}%"))

    # Filter op kenmerken (features)
    if features:
        if "wifi" in features:
            query = query.filter(Hotel.has_wifi == True)
        if "parking" in features:
            query = query.filter(Hotel.has_parking == True)
        if "breakfast" in features:
            query = query.filter(Hotel.has_breakfast == True)
        if "pets" in features:
            query = query.filter(Hotel.pet_friendly == True)

    return query.all()

# Haal een hotel op via zijn ID
def get_hotel_by_id(db: Session, hotel_id: int) -> Optional[Hotel]:
    return db.query(Hotel).filter(Hotel.id == hotel_id).first()
