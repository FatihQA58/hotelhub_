from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import SessionLocal
from app.schemas.review_schemas import ReviewCreate, ReviewOut
from app.crud.review_crud import create_review, get_all_reviews, get_reviews_by_hotel

router = APIRouter()

# Zorgt voor een verbinding met de database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST: voeg een nieuwe review toe
@router.post("/", response_model=ReviewOut)
def add_review(review: ReviewCreate, db: Session = Depends(get_db)):
    return create_review(db=db, review=review)

# GET: lijst alle reviews op
@router.get("/", response_model=List[ReviewOut])
def list_reviews(db: Session = Depends(get_db)):
    return get_all_reviews(db=db)

# GET: lijst reviews per hotel
@router.get("/hotel/{hotel_id}", response_model=List[ReviewOut])
def list_reviews_for_hotel(hotel_id: int, db: Session = Depends(get_db)):
    return get_reviews_by_hotel(db=db, hotel_id=hotel_id)
