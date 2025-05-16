from sqlalchemy import Column, Integer, Date, ForeignKey, String, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

# Dit is de Reservatie (Booking) tabel
class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)  # gekoppeld aan hotel
    guest_name = Column(String, nullable=False)     # naam van de gast
    guest_email = Column(String, nullable=False)    # e-mail van de gast
    check_in = Column(Date, nullable=False)         # incheckdatum
    check_out = Column(Date, nullable=False)        # uitcheckdatum
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # aanmaakdatum
