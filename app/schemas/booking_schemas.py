from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Dit model wordt gebruikt bij het aanmaken van een nieuwe reservatie
class ReservationCreate(BaseModel):
    hotel_id: int
    guest_name: str
    guest_email: EmailStr
    check_in: datetime
    check_out: datetime

# Dit model toont reservatiegegevens aan de gebruiker
class ReservationOut(BaseModel):
    id: int
    hotel_id: int
    guest_name: str
    guest_email: EmailStr
    check_in: datetime
    check_out: datetime
    created_at: Optional[datetime]

    class Config:
        from_attributes = True  # voor goede ORM-integratie
