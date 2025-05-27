from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional
from app.models.user_model import User


# Dit model wordt gebruikt bij het aanmaken van een nieuwe reservatie
class ReservationCreate(BaseModel):
    hotel_name:str
    room_number:str
    check_in: datetime
    check_out: datetime

# Dit model toont reservatiegegevens aan de gebruiker
class ReservationOut(BaseModel):
    hotel_name:str
    room_number:str
    check_in: datetime
    check_out: datetime
    user_name:str

    class Config:
        orm_mode = True

class GetReservation(BaseModel):
    hotel_name: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    room_number: Optional[str]
    user_name: Optional[str]

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class HotelOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class RoomOut(BaseModel):
    id: int
    room_number: str
    hotel: HotelOut

    class Config:
        orm_mode = True

class GetReservationOut(BaseModel):
    id: int
    user: UserOut
    room: RoomOut
    check_in: datetime
    check_out: datetime
    created_at: datetime

    class Config:
        orm_mode = True

