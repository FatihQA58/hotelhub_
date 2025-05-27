from fastapi import HTTPException
from sqlalchemy.orm import Session,joinedload
from typing import List, Optional
from app import models
from app.models.hotel_model import Hotel, Room
from app.schemas.room_schemas import RoomUpdate, RoomCreate


# Voeg een nieuw room toe aan de database
def create_room(db: Session, room: RoomCreate) -> Room:
    db_room = Room(**room.model_dump())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room





def get_room_by_number (db: Session, hotel_name: str,room_number:str):
    room= db.query(Room).join(Hotel).filter(
        Room.room_number == room_number,
        Hotel.name == hotel_name).first()
    if not room:
        raise HTTPException(status_code=404, detail="Kamer bestaat niet.")
    return room



# Update het room met nummer en hotel naam
def update_room(db:Session,hotel_name:str,room_number:str,room_update:RoomUpdate):
    room=get_room_by_number(db,hotel_name, room_number)

    update_data=room_update.dict(exclude_unset=True)
    for key,value in update_data.items():
        setattr(room,key,value)
    db.commit()
    db.refresh(room)
    return room



# Delete een kamer op via hotel naam en room_number
def delete_room(db: Session, hotel_name: str,room_number:str):
    room=get_room_by_number(db,hotel_name,room_number)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    db.delete(room)
    db.commit()
    return {"detail": f"Room '{room_number}' deleted"}


