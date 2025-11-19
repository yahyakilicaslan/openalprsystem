from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List
from backend.database import database
from backend.database.models import Door

router = APIRouter()

@router.post("/", response_description="Add new door", response_model=Door)
async def create_door(door: Door = Body(...)):
    door_dict = door.dict(by_alias=True)
    door_dict['_id'] = str(door_dict['_id']) # Convert ObjectId to string
    db_door = await database.door_collection.insert_one(door_dict)
    new_door = await database.door_collection.find_one({"_id": db_door.inserted_id})
    return new_door

@router.get("/", response_description="List all doors", response_model=List[Door])
async def list_doors():
    doors = await database.door_collection.find().to_list(1000)
    return doors

@router.get("/{id}", response_description="Get a single door", response_model=Door)
async def show_door(id: str):
    if (door := await database.door_collection.find_one({"_id": id})) is not None:
        return door
    raise HTTPException(status_code=404, detail=f"Door {id} not found")

@router.put("/{id}", response_description="Update a door", response_model=Door)
async def update_door(id: str, door: Door = Body(...)):
    door_dict = {k: v for k, v in door.dict(by_alias=True).items() if v is not None}
    door_dict.pop('_id', None) # Don't update the _id

    if len(door_dict) >= 1:
        update_result = await database.door_collection.update_one({"_id": id}, {"$set": door_dict})

        if update_result.modified_count == 1:
            if (
                updated_door := await database.door_collection.find_one({"_id": id})
            ) is not None:
                return updated_door

    if (
        existing_door := await database.door_collection.find_one({"_id": id})
    ) is not None:
        return existing_door

    raise HTTPException(status_code=404, detail=f"Door {id} not found")

@router.delete("/{id}", response_description="Delete a door")
async def delete_door(id: str):
    delete_result = await database.door_collection.delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Door {id} not found")
