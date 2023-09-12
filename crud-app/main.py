# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int
    email: str

# In-memory database (for demonstration purposes)
db = []

@app.post("/api/person")
async def create_person(person: Person):
    db.append(person)
    return {"message": "Person created successfully"}

@app.get("/api/person/{person_id}")
async def read_person(person_id: int):
    if person_id < len(db):
        return db[person_id]
    else:
        return {"error": "Person not found"}

@app.put("/api/person/{person_id}")
async def update_person(person_id: int, updated_person: Person):
    if person_id < len(db):
        db[person_id] = updated_person
        return {"message": "Person updated successfully"}
    else:
        return {"error": "Person not found"}

@app.delete("/api/person/{person_id}")
async def delete_person(person_id: int):
    if person_id < len(db):
        db.pop(person_id)
        return {"message": "Person deleted successfully"}
    else:
        return {"error": "Person not found"}    