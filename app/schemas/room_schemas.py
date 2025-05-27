from pydantic import BaseModel
from typing import Optional,List


class RoomUpdate(BaseModel):
    room_number : Optional[str]=None
    description : Optional[str]=None  # single,suite exc.
    aantal_bed : Optional[int]=None  # aantal bed van kamer?
    has_air_condition : Optional[bool]=None  # heeft aircondition?
    has_koelkast : Optional[bool]=None  # heeft koelkast
    has_tv : Optional[bool]=None  # heeft tv
    available : Optional[int]=None # beschickbaar?
    price_per_night : Optional[float]=None # prijs per nacht in euro


class RoomCreate(BaseModel):
    room_number :str
    description :str
    aantal_bed :int
    has_air_condition :bool
    has_koelkast :bool
    has_tv :bool
    available :bool
    price_per_night :float
    hotel_id :int