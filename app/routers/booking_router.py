from datetime import datetime, date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from app.db.database import SessionLocal
from app.models.booking_model import Reservation
from app.schemas.booking_schemas import ReservationCreate,GetReservationOut,GetReservation
from app.crud.booking_crud import create_reservation, is_room_available,get_reservations
from app.crud.room_crud import get_room_by_number
from app.utils import auth


router = APIRouter()

# Zorgt voor een verbinding met de database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST: maak een nieuwe reservatie
@router.post("/")
def book_room(reservation: ReservationCreate,
              db: Session = Depends(get_db),
              user=Depends(auth.get_current_user)):
    room=get_room_by_number(reservation.hotel_name,reservation.room_number,db)
    is_room_available(reservation, db)
    create_reservation(db,user.id,room.id,reservation.check_in,reservation.check_out)
    return reservation

# GET: lijst alle reservaties op
@router.post("/get_reservations",response_model=List[GetReservationOut])
def filter_reservations(
    hotel_name: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    room_number: Optional[str] = None,
    user_name: Optional[str] = None,
    db: Session = Depends(get_db)
):
    filters = GetReservation(
        hotel_name=hotel_name,
        start_date=start_date,
        end_date=end_date,
        room_number=room_number,
        user_name=user_name
    )
    return get_reservations(filters, db)

