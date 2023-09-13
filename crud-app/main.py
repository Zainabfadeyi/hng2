# # main.py
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Person(BaseModel):
#     name: str
#     age: int
#     email: str

# # In-memory database (for demonstration purposes)
# db = []

# @app.post("/api/person")
# async def create_person(person: Person):
#     db.append(person)
#     return {"message": "Person created successfully"}

# @app.get("/api/person/{person_id}")
# async def read_person(person_id: int):
#     if person_id < len(db):
#         return db[person_id]
#     else:
#         return {"error": "Person not found"}

# @app.put("/api/person/{person_id}")
# async def update_person(person_id: int, updated_person: Person):
#     if person_id < len(db):
#         db[person_id] = updated_person
#         return {"message": "Person updated successfully"}
#     else:
#         return {"error": "Person not found"}

# @app.delete("/api/person/{person_id}")
# async def delete_person(person_id: int):
#     if person_id < len(db):
#         db.pop(person_id)
#         return {"message": "Person deleted successfully"}
#     else:
#         return {"error": "Person not found"}    
# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create a FastAPI instance
app = FastAPI()

# Define Pydantic models for request and response
class PersonBase(BaseModel):
    name: str
    age: int
    email: str

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    id: int

# Define CRUD operations using SQLAlchemy and FastAPI
@app.post("/api/person", response_model=Person)
def create_person(person: PersonCreate):
    # Implement your create logic here
    pass

@app.get("/api/person/{person_id}", response_model=Person)
def read_person(person_id: int):
    # Implement your read logic here
    pass

@app.put("/api/person/{person_id}", response_model=Person)
def update_person(person_id: int, updated_person: PersonBase):
    # Implement your update logic here
    pass

@app.delete("/api/person/{person_id}", response_model=Person)
def delete_person(person_id: int):
    # Implement your delete logic here
    pass