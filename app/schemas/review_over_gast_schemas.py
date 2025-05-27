from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ReviewOverGastBase(BaseModel):
    guest_id: int
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None

class ReviewOverGastCreate(ReviewOverGastBase):
    pass

class ReviewOverGastOut(ReviewOverGastBase):
    id: int
    reviewer_id: int
    created_at: datetime

    class Config:
        orm_mode = True 
