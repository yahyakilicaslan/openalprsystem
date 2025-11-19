from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List
from backend.database import database
from backend.database.models import Camera

router = APIRouter()

@router.post("/", response_description="Add new camera", response_model=Camera)
async def create_camera(camera: Camera = Body(...)):
    camera_dict = camera.dict(by_alias=True)
    camera_dict['_id'] = str(camera_dict['_id']) # Convert ObjectId to string
    db_camera = await database.camera_collection.insert_one(camera_dict)
    new_camera = await database.camera_collection.find_one({"_id": db_camera.inserted_id})
    return new_camera

@router.get("/", response_description="List all cameras", response_model=List[Camera])
async def list_cameras():
    cameras = await database.camera_collection.find().to_list(1000)
    return cameras

@router.get("/{id}", response_description="Get a single camera", response_model=Camera)
async def show_camera(id: str):
    if (camera := await database.camera_collection.find_one({"_id": id})) is not None:
        return camera
    raise HTTPException(status_code=404, detail=f"Camera {id} not found")

@router.put("/{id}", response_description="Update a camera", response_model=Camera)
async def update_camera(id: str, camera: Camera = Body(...)):
    camera_dict = {k: v for k, v in camera.dict(by_alias=True).items() if v is not None}
    camera_dict.pop('_id', None) # Don't update the _id

    if len(camera_dict) >= 1:
        update_result = await database.camera_collection.update_one({"_id": id}, {"$set": camera_dict})

        if update_result.modified_count == 1:
            if (
                updated_camera := await database.camera_collection.find_one({"_id": id})
            ) is not None:
                return updated_camera

    if (
        existing_camera := await database.camera_collection.find_one({"_id": id})
    ) is not None:
        return existing_camera

    raise HTTPException(status_code=404, detail=f"Camera {id} not found")

@router.delete("/{id}", response_description="Delete a camera")
async def delete_camera(id: str):
    delete_result = await database.camera_collection.delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Camera {id} not found")
