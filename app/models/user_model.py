from sqlalchemy import Column, Integer, String
from app.db.database import Base

# Dit is de User tabel
class User(Base):
    __tablename__ = "users"  # tabelnaam in de database

    id = Column(Integer, primary_key=True, index=True)          # unieke ID voor elke gebruiker
    name = Column(String, nullable=False)                       # naam van de gebruiker
    email = Column(String, unique=True, index=True, nullable=False)  # e-mailadres moet uniek zijn
    hashed_password = Column(String, nullable=False)            # wachtwoord (versleuteld opgeslagen)
