
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReviewCreate(BaseModel):
    guest_name: str
    rating: int
    comment: Optional[str] = None

class ReviewOut(ReviewCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
