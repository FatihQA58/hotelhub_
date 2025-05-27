from sqlalchemy.orm import Session
from app.models.review_over_gast_model import ReviewOverGast
from app.schemas.review_over_gast_schemas import ReviewOverGastCreate

def create_guest_review(db: Session, review: ReviewOverGastCreate, reviewer_id: int):
    db_review = ReviewOverGast(
        reviewer_id=reviewer_id,
        guest_id=review.guest_id,
        rating=review.rating,
        comment=review.comment
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
