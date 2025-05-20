from sqlalchemy import Column, Integer, String, Float, Boolean,ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base

# Dit is de Hotel tabel
class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)               # naam van het hotel
    city = Column(String, index=True)                   # stad waar het hotel zich bevindt
    description = Column(String, nullable=True)         # korte beschrijving
    has_wifi = Column(Boolean, default=False)           # heeft wifi?
    has_parking = Column(Boolean, default=False)        # heeft parkeergelegenheid?
    has_breakfast = Column(Boolean, default=False)      # biedt ontbijt aan?
    pet_friendly = Column(Boolean, default=False)       # huisdieren toegestaan?
    price_per_night = Column(Float, nullable=False)     # prijs per nacht in euro
    rooms = relationship("Room", back_populates="hotel")

class Room(Base):
    __tablename__="rooms"

    id = Column(Integer, primary_key=True, index=True)
    room_number= Column(String, nullable=False)
    description = Column(String, nullable=True)  # single,suite exc.
    capacity = Column(Integer, default=1)  # capacity van kamer?
    has_air_condition = Column(Boolean, default=False)  # heeft parkeergelegenheid?
    available = Column(Boolean, default=True)  # beschickbaar?
    price_per_night = Column(Float, nullable=False)  # prijs per nacht in euro

    hotel_id = Column(String, ForeignKey("hotels.id"), nullable=False)  # id van het hotel
    hotel = relationship("Hotel", back_populates="rooms")

