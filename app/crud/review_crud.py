from sqlalchemy.orm import Session
from typing import List
from app.models.review_model import Review
from app.schemas.review_schemas import ReviewCreate

# Voeg een nieuwe review toe aan de database
def create_review(db: Session, review: ReviewCreate) -> Review:
    db_review = Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

# Haal alle reviews op uit de database
def get_all_reviews(db: Session) -> List[Review]:
    return db.query(Review).all()

# Haal alle reviews voor een specifiek hotel op
def get_reviews_by_hotel(db: Session, hotel_id: int) -> List[Review]:
    return db.query(Review).filter(Review.hotel_id == hotel_id).all()
