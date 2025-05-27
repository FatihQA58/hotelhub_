from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base

# Dit is de User tabel
class User(Base):
    __tablename__ = "users"  # tabelnaam in de database

    id = Column(Integer, primary_key=True, index=True)          # unieke ID voor elke gebruiker
    name = Column(String, nullable=False)                       # naam van de gebruiker
    email = Column(String, unique=True, index=True, nullable=False)  # e-mailadres moet uniek zijn
    hashed_password = Column(String, nullable=False)

    role_id = Column(Integer, ForeignKey('Roles.id'),nullable=False)
    role = relationship("Role", back_populates="users")
    reservations = relationship("Reservation", back_populates="user")

# Dit is de Role tabel
class Role(Base):
    __tablename__="Roles"

    id = Column(Integer, primary_key=True, index=True)  # unieke ID voor elke role
    role_name = Column(String, nullable=False)

    users = relationship("User", back_populates="role")