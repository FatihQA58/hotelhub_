from sqlalchemy import Column, Integer, Date, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

# Dit is de Reservatie (Booking) tabel
class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    check_in = Column(Date, nullable=False)         # incheckdatum
    check_out = Column(Date, nullable=False)        # uitcheckdatum
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # aanmaakdatum
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False) # gekoppeld aan room
    room = relationship("Room", back_populates="reservations")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="reservations")
