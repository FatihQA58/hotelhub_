from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session, joinedload, join
from sqlalchemy import and_
from typing import List
from datetime import date, datetime
from app.models import user_model
from app.models import hotel_model

from app.models.booking_model import Reservation
from app.models.hotel_model import Hotel, Room
from app.crud import room_crud
from app.models.user_model import User
from app.schemas.booking_schemas import ReservationCreate, GetReservation
from app.utils.auth import get_db


# Controleer of de kamer beschikbaar is voor de opgegeven data
def is_room_available(
    reservation: ReservationCreate,
    db: Session = Depends(get_db)
):
    # 1. find the room
    room = room_crud.get_room_by_number(reservation.hotel_name,reservation.room_number,db)


    # 2. is_room_available
    available = db.query(Reservation).filter(
        Reservation.room_id == room.id,
        Reservation.check_out > reservation.check_in,
        Reservation.check_in < reservation.check_out
    ).count()
    if reservation.check_in >= reservation.check_out:
        raise HTTPException(status_code=400, detail="Check-in must be before check-out.")
    if available > 0:
        raise HTTPException(status_code=400, detail="The room is not available.")
    return True


# Maak een nieuwe reservatie aan
def create_reservation(
    db: Session,
    user_id: int,
    room_id: int,
    check_in: datetime,
    check_out: datetime
) -> Reservation:
    new_reservation = Reservation(
        user_id=user_id,
        room_id=room_id,
        check_in=check_in,
        check_out=check_out,
        created_at=datetime.utcnow()
    )
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation


# Haal alle reservaties op uit de database
def get_reservations(filters: GetReservation, db: Session):
    query = db.query(Reservation).options(
        joinedload(Reservation.user),joinedload(Reservation.room).joinedload(Room.hotel)
    )

    if filters.hotel_name:
        query = query.join(Reservation.room).join(Room.hotel)
        query = query.filter(Hotel.name == filters.hotel_name)
    if filters.start_date:
        query = query.filter(Reservation.check_in >= filters.start_date)
    if filters.end_date:
        query = query.filter(Reservation.check_out <= filters.end_date)
    if filters.room_number:
        query = query.join(Reservation.room)
        query = query.filter(Room.room_number == filters.room_number)
    if filters.user_name:
        query = query.join(Reservation.user)
        query = query.filter(User.name == filters.user_name)

    return query.all()

