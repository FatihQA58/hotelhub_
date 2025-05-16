from pydantic import BaseModel
from typing import Optional

# Dit model toont hotelgegevens aan de gebruiker
class HotelOut(BaseModel):
    id: int
    name: str
    city: str
    description: Optional[str]
    has_wifi: bool
    has_parking: bool
    has_breakfast: bool
    pet_friendly: bool
    price_per_night: float

    class Config:
        from_attributes = True  # zorgt voor goede conversie vanuit SQLAlchemy

# Dit model wordt gebruikt bij het aanmaken van een nieuw hotel
class HotelCreate(BaseModel):
    name: str
    city: str
    description: Optional[str]
    has_wifi: bool = False
    has_parking: bool = False
    has_breakfast: bool = False
    pet_friendly: bool = False
    price_per_night: float

# (Optioneel) Voor toekomstige uitbreidingen met query-modellen
class HotelSearchQuery(BaseModel):
    city: Optional[str]
    check_in: Optional[str]
    check_out: Optional[str]
    features: Optional[str]
