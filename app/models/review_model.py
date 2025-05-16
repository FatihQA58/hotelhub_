from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

# Dit is de Review tabel
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)  # bij welk hotel hoort deze review
    guest_name = Column(String, nullable=False)         # naam van de gast die de review schrijft
    rating = Column(Integer, nullable=True)             # optioneel: score van 1 tot 5
    comment = Column(String, nullable=False)            # de eigenlijke tekst van de review
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # automatisch tijdstip van aanmaken
