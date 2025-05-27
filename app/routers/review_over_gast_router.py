from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.schemas.review_over_gast_schemas import ReviewOverGastCreate, ReviewOverGastOut
from app.crud import review_over_gast_crud
from app.db.database import get_db
from app.utils.auth import get_current_user
from app.models.user_model import User

router = APIRouter(
    prefix="/guest_reviews",
    tags=["Reviews"] 
)

@router.post("/", response_model=ReviewOverGastOut, status_code=status.HTTP_201_CREATED)
def create_guest_review(
    review: ReviewOverGastCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """ 
    Als hotelbeheerder wil ik een beoordeling geven aan een gast na diens verblijf,  
    zodat andere hotels kunnen inschatten of de gast betrouwbaar is.
    """
    if not current_user.is_beheerder:
        raise HTTPException(status_code=403, detail="Alleen hotelbeheerders mogen gasten beoordelen.")
    
    return review_over_gast_crud.create_guest_review(
        db=db,
        review=review,
        reviewer_id=current_user.id
    )
