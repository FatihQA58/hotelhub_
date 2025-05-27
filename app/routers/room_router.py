from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.user_model import User

from app.schemas.room_schemas import RoomUpdate, RoomCreate
from app.utils import auth
from app.crud.room_crud import get_room_by_number, update_room, delete_room, create_room
from app.db.database import SessionLocal

router = APIRouter()

# Zorgt voor een verbinding met de database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POST: voeg een nieuw room toe
@router.post("/")
def add_room(room: RoomCreate, db: Session = Depends(get_db),user=Depends(auth.get_current_user)):
    if user.role_id == 2:
        raise HTTPException(status_code=403,detail='Verboden voor u,u moet Hotelbeheerder zijn')
    return create_room(db=db, room=room)




@router.get('/get_room')
def get_room(hotel_name:str,room_number:str,db: Session = Depends(get_db)):
    return get_room_by_number(db,hotel_name, room_number)



# PUT:update een room met nummer en hotelnaam
@router.put("/{hotel_name}/{room_number}")
def update_room_router (hotel_name:str,room_number:str,room_update:RoomUpdate,
                 db: Session = Depends(get_db),current_user:User=Depends(auth.get_current_user)):

    if current_user.role_id == 2:
        raise HTTPException(status_code=403,detail='Verboden voor u,u moet Hotelbeheerder zijn')
    room=update_room(db,hotel_name,room_number,room_update)
    return room


# Delete:delete een room met room_number
@router.delete("/{hotel_name}{room_number}")
def delete_room_router(hotel_name:str,room_number:str
                        ,db:Session=Depends((get_db)),current_user=Depends(auth.get_current_user)):
    if current_user.role_id == 2:
        raise HTTPException(status_code=403,detail='Verboden voor u,u moet Hotelbeheerder zijn')
    return delete_room(db,hotel_name,room_number)