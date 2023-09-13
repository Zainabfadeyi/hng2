from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, Person
from crud import create_person, get_person, update_person, delete_person

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/api")
def create_new_person(name: str, age: int, db: Session = Depends(get_db)):
    # Add validation for string fields here
    if not isinstance(name, str) or not isinstance(age, int):
        raise HTTPException(status_code=400, detail="Name and age must be strings and integers, respectively.")
    
    person = create_person(db, name, age)
    return person

@app.get("/api/{user_id}")
def read_person(user_id: int, db: Session = Depends(get_db)):
    person = get_person(db, user_id)
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person
@app.put("/api/{user_id}")
def update_person_details(user_id: int, name: str, age: int, db: Session = Depends(get_db)):
    # Add validation for string fields here
    if not isinstance(name, str) or not isinstance(age, int):
        raise HTTPException(status_code=400, detail="Name and age must be strings and integers, respectively.")
    
    person = update_person(db, user_id, name, age)
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@app.delete("/api/{user_id}")
def delete_person_record(user_id: int, db: Session = Depends(get_db)):
    delete_person(db, user_id)
    return {"message": "Person deleted"}