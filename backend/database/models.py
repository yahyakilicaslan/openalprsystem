from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class Site(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    block_count: int
    block_names: List[str]
    apartments_per_block: int

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Plate(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    plate_number: str
    owner_name: str
    site_id: str
    block_name: str
    apartment_number: int
    valid_until: Optional[datetime]
    status: str  # "allowed", "banned", "guest"

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Door(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    nodemcu_ip: str
    endpoint: str  # "/kapiac", "/kapiac1", etc.

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Camera(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    camera_type: str  # "webcam", "rtsp", "http", "onvif"
    url_or_index: str
    associated_door_id: str
    fps: int
    onvif_settings: Optional[dict]  # For zoom, brightness, etc.

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
