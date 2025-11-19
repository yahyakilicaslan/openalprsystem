from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List
from backend.database import database
from backend.database.models import Plate

router = APIRouter()

@router.post("/", response_description="Add new plate", response_model=Plate)
async def create_plate(plate: Plate = Body(...)):
    # Bir daireye en fazla 3 plaka eklenebilir kontrolü
    plate_count = await database.plate_collection.count_documents({"site_id": plate.site_id, "block_name": plate.block_name, "apartment_number": plate.apartment_number})
    if plate_count >= 3:
        raise HTTPException(status_code=400, detail="An apartment can have a maximum of 3 plates.")

    plate_dict = plate.dict(by_alias=True)
    plate_dict['_id'] = str(plate_dict['_id']) # Convert ObjectId to string
    db_plate = await database.plate_collection.insert_one(plate_dict)
    new_plate = await database.plate_collection.find_one({"_id": db_plate.inserted_id})
    return new_plate

@router.get("/", response_description="List all plates", response_model=List[Plate])
async def list_plates():
    plates = await database.plate_collection.find().to_list(1000)
    return plates

@router.get("/{id}", response_description="Get a single plate", response_model=Plate)
async def show_plate(id: str):
    if (plate := await database.plate_collection.find_one({"_id": id})) is not None:
        return plate
    raise HTTPException(status_code=404, detail=f"Plate {id} not found")

@router.put("/{id}", response_description="Update a plate", response_model=Plate)
async def update_plate(id: str, plate: Plate = Body(...)):
    plate_dict = {k: v for k, v in plate.dict(by_alias=True).items() if v is not None}
    plate_dict.pop('_id', None) # Don't update the _id

    if len(plate_dict) >= 1:
        update_result = await database.plate_collection.update_one({"_id": id}, {"$set": plate_dict})

        if update_result.modified_count == 1:
            if (
                updated_plate := await database.plate_collection.find_one({"_id": id})
            ) is not None:
                return updated_plate

    if (
        existing_plate := await database.plate_collection.find_one({"_id": id})
    ) is not None:
        return existing_plate

    raise HTTPException(status_code=404, detail=f"Plate {id} not found")

@router.delete("/{id}", response_description="Delete a plate")
async def delete_plate(id: str):
    delete_result = await database.plate_collection.delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Plate {id} not found")
