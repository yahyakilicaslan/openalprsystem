from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List
from ..database import database
from ..database.models import Site

router = APIRouter()

@router.post("/", response_description="Add new site", response_model=Site)
async def create_site(site: Site = Body(...)):
    site = await database.site_collection.insert_one(site.dict(by_alias=True))
    new_site = await database.site_collection.find_one({"_id": site.inserted_id})
    return new_site

@router.get("/", response_description="List all sites", response_model=List[Site])
async def list_sites():
    sites = await database.site_collection.find().to_list(1000)
    return sites

@router.get("/{id}", response_description="Get a single site", response_model=Site)
async def show_site(id: str):
    if (site := await database.site_collection.find_one({"_id": id})) is not None:
        return site
    raise HTTPException(status_code=404, detail=f"Site {id} not found")

@router.put("/{id}", response_description="Update a site", response_model=Site)
async def update_site(id: str, site: Site = Body(...)):
    site = {k: v for k, v in site.dict(by_alias=True).items() if v is not None}

    if len(site) >= 1:
        update_result = await database.site_collection.update_one({"_id": id}, {"$set": site})

        if update_result.modified_count == 1:
            if (
                updated_site := await database.site_collection.find_one({"_id": id})
            ) is not None:
                return updated_site

    if (
        existing_site := await database.site_collection.find_one({"_id": id})
    ) is not None:
        return existing_site

    raise HTTPException(status_code=404, detail=f"Site {id} not found")

@router.delete("/{id}", response_description="Delete a site")
async def delete_site(id: str):
    delete_result = await database.site_collection.delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Site {id} not found")
