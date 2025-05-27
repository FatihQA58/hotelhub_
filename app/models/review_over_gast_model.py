from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base 

class ReviewOverGast(Base):
    __tablename__ = "review_over_gast"

    id = Column(Integer, primary_key=True, index=True)
    reviewer_id = Column(Integer, ForeignKey("users.id")) 
    guest_id = Column(Integer, ForeignKey("users.id"))       
    rating = Column(Integer, nullable=False)
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

   
    reviewer = relationship("User", foreign_keys=[reviewer_id], backref="guest_reviews_given")
    guest = relationship("User", foreign_keys=[guest_id], backref="guest_reviews_received")
