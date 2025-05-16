from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List
from datetime import date

from app.models.booking_model import Reservation
from app.schemas.booking_schemas import ReservationCreate

# Controleer of de kamer beschikbaar is voor de opgegeven data
def is_available(db: Session, hotel_id: int, check_in: date, check_out: date) -> bool:
    overlapping_reservations = db.query(Reservation).filter(
        Reservation.hotel_id == hotel_id,
        Reservation.check_out > check_in,   # bestaand vertrek is NA de gewenste check-in
        Reservation.check_in < check_out    # bestaand aankomst is VOOR de gewenste check-out
    ).all()

    return len(overlapping_reservations) == 0

# Maak een nieuwe reservatie aan
def create_reservation(db: Session, reservation: ReservationCreate) -> Reservation:
    if not is_available(db, reservation.hotel_id, reservation.check_in, reservation.check_out):
        raise ValueError("De kamer is niet beschikbaar voor de geselecteerde data.")

    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

# Haal alle reservaties op uit de database
def get_all_reservations(db: Session) -> List[Reservation]:
    return db.query(Reservation).all()
