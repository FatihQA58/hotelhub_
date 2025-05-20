from pydantic import BaseModel
from typing import Optional,List

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

class RoomOut(BaseModel):
    room_number :str
    description :str
    capacity :int
    has_air_condition :bool=False
    available :bool=True
    price_per_night :float
    class Config:
        from_attributes = True

class HotelOutWithRooms(BaseModel):
    name: str
    city: str
    description: Optional[str]
    rooms:List[RoomOut]


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

# Dit model wordt gebruikt bij het update van een hotel
class HotelUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    description: Optional[str] = None
    has_wifi: bool = False
    has_parking: bool = False
    has_breakfast: bool = False
    pet_friendly: bool = False
    price_per_night: Optional[float] = None
