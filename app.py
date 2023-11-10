from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()

client = MongoClient("mongodb+srv://somadnachirou:<Passw0rde>@cluster0.thwi2yv.mongodb.net/")
db = client["nachirou"]
collection = db["restapi"]

class Item(BaseModel):
    def __init__(self, name:str, description: str) -> None:
        self.name = name
        self.description = description
        
# post item
@app.post("/item")
def create_item (item:Item):
    item_dict = {"name":item.name, "description":item.description}
    result = collection.insert_one(item_dict) 
    return {"item_id":str(result.inserted_id)}

# retrieve by id
@app.get("item/{item_id}")
def read_item (item_id:str):
    item = collection.find_one("_id", item_id)
    if item is not None:
        return item
    raise HTTPException(status_code=404, detail="Item doesn't exist")


