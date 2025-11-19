from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)

database = client.anpr_system

plate_collection = database.get_collection("plates")
site_collection = database.get_collection("sites")
door_collection = database.get_collection("doors")
camera_collection = database.get_collection("cameras")
user_collection = database.get_collection("users")
log_collection = database.get_collection("logs")
