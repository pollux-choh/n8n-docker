# app.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(root_path="/fastapi-app")

# In-memory 데이터 저장소
items = {}

class Item(BaseModel):
    name: str
    description: str = None
    price: float

@app.post("/item")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"item_id": item_id, "item": item}

@app.get("/items")
def list_items():
    return {"items": items}

@app.delete("/item/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": f"Item {item_id} deleted successfully"}
    return {"error": f"Item {item_id} not found"}
