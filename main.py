from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Inventory Management API")

# Mock Database
inventory = [
    {"id": 1, "item_name": "Bread", "quantity": 50, "price": 40.0},
    {"id": 2, "item_name": "Cake", "quantity": 10, "price": 500.0}
]

class Item(BaseModel):
    id: int
    item_name: str
    quantity: int
    price: float

@app.get("/items", response_model=List[Item])
def get_inventory():
    return inventory

@app.post("/items")
def add_item(item: Item):
    inventory.append(item.dict())
    return {"message": "Item added successfully", "data": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global inventory
    inventory = [item for item in inventory if item['id'] != item_id]
    return {"message": "Item deleted"}
@app.get("/items/search")
def search_item(name: str):
    # Logic to filter items by name
    results = [item for item in inventory if name.lower() in item['item_name'].lower()]
    if not results:
        return {"message": "No items found matching that name"}
    return results