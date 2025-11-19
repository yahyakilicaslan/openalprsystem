from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes import site as site_router
from routes import plate as plate_router
from routes import door as door_router
from routes import camera as camera_router

app = FastAPI(title="Evo Teknoloji Plaka Tanıma Sistemi", version="1.0.0")

# CORS middleware configuration
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(site_router.router, tags=["Sites"], prefix="/api/sites")
app.include_router(plate_router.router, tags=["Plates"], prefix="/api/plates")
app.include_router(door_router.router, tags=["Doors"], prefix="/api/doors")
app.include_router(camera_router.router, tags=["Cameras"], prefix="/api/cameras")

@app.get("/")
def read_root():
    return {"message": "Evo Teknoloji ANPR API'sine hoş geldiniz!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
