from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, Person
from crud import create_person, get_person, update_person, delete_person
from pydantic import BaseModel

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Person(BaseModel):
    name: str
    age: int

@app.post("/api")
def create_new_person(person: Person, db: Session = Depends(get_db)):
    # Add validation for string fields here
    if not isinstance(person.name, str) or not isinstance(person.age, int):
        raise HTTPException(status_code=400, detail="Name and age must be strings and integers, respectively.")
    
    person_ = create_person(db, person.name, person.age)
    return person_

@app.get("/api/{user_id}")
def read_person(user_id: int, db: Session = Depends(get_db)):
    person = get_person(db, user_id)
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@app.put("/api/{user_id}")
def update_person_details(user_id: int, person: Person, db: Session = Depends(get_db)):
    # Add validation for string fields here
    if not isinstance(person.name, str) or not isinstance(person.age, int):
        raise HTTPException(status_code=400, detail="Name and age must be strings and integers, respectively.")
    
    person_ = update_person(db, user_id, person.name, person.age)
    if person_ is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person_

@app.delete("/api/{user_id}")
def delete_person_record(user_id: int, db: Session = Depends(get_db)):
    delete_person(db, user_id)
    return {"message": "Person deleted"}