from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Dit model wordt gebruikt bij het aanmaken van een nieuwe review
class ReviewCreate(BaseModel):
    hotel_id: int
    guest_name: str
    rating: Optional[int] = None     # optioneel: score van 1 tot 5
    comment: str

# Dit model toont reviewgegevens aan de gebruiker
class ReviewOut(BaseModel):
    id: int
    hotel_id: int
    guest_name: str
    rating: Optional[int] = None
    comment: str
    created_at: datetime

    class Config:
        from_attributes = True  # voor ORM-integratie met SQLAlchemy
