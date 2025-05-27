from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import SessionLocal
from app.schemas.booking_schemas import ReservationCreate, ReservationOut
from app.crud.booking_crud import create_reservation, get_all_reservations

router = APIRouter(
    prefix="/reservations",
      tags=["Reservaties"]
)

# Zorgt voor een verbinding met de database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST: maak een nieuwe reservatie
@router.post("/", response_model=ReservationOut)
def book_room(reservation: ReservationCreate, db: Session = Depends(get_db)):
    try:
        return create_reservation(db=db, reservation=reservation)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# GET: lijst alle reservaties op
@router.get("/", response_model=List[ReservationOut])
def list_reservations(db: Session = Depends(get_db)):
    return get_all_reservations(db=db)
