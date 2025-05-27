from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.schemas.review_over_gast_schemas import ReviewOverGastCreate, ReviewOverGastOut
from app.crud import review_over_gast_crud
from app.db.database import get_db
from app.utils.auth import get_current_user
from app.models.user_model import User
from app.models.review_over_gast_model import ReviewOverGast

router = APIRouter(
    prefix="/guest_reviews",
    tags=["Reviews"] 
)

@router.get("/", response_model=list[ReviewOverGastOut])
def get_all_guest_reviews(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user.role_id == 2:
        raise HTTPException(
            status_code=403,
            detail="Alleen hotelbeheerders kunnen beoordelingen bekijken."
        )
    return db.query(ReviewOverGast).all()

@router.get("/{id}", response_model=ReviewOverGastOut)
def get_guest_review_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user.role_id == 2:
        raise HTTPException(status_code=403, detail="Alleen hotelbeheerders mogen beoordelingen opvragen.")
    review = db.query(ReviewOverGast).filter(ReviewOverGast.id == id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Beoordeling niet gevonden.")
    return review

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
    if not current_user.role_id == 2:
        raise HTTPException(status_code=403, detail="Alleen hotelbeheerders mogen gasten beoordelen.")
    
    return review_over_gast_crud.create_guest_review(
        db=db,
        review=review,
        reviewer_id=current_user.id
    )

@router.put("/{id}", response_model=ReviewOverGastOut)
def update_guest_review(
    id: int,
    updated: ReviewOverGastCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user.role_id == 2:
        raise HTTPException(status_code=403, detail="Alleen hotelbeheerders kunnen beoordelingen bewerken.")
    review = db.query(ReviewOverGast).filter(ReviewOverGast.id == id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Beoordeling niet gevonden.")
    review.guest_id = updated.guest_id
    review.rating = updated.rating
    review.comment = updated.comment
    db.commit()
    db.refresh(review)
    return review


@router.delete("/{id}", status_code=204)
def delete_guest_review(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not current_user.role_id == 2:
        raise HTTPException(status_code=403, detail="Alleen hotelbeheerders kunnen beoordelingen verwijderen.")
    review = db.query(ReviewOverGast).filter(ReviewOverGast.id == id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Beoordeling niet gevonden.")
    db.delete(review)
    db.commit()
    return None
