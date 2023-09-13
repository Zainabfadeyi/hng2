from sqlalchemy.orm import Session
from models import Person

def create_person(db: Session, name: str, age: int):
    db_person = Person(name=name, age=age)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def get_person(db: Session, user_id: int):
    return db.query(Person).filter(Person.id == user_id).first()

def update_person(db: Session, user_id: int, name: str, age: int):
    db_person = db.query(Person).filter(Person.id == user_id).first()
    if db_person:
        db_person.name = name
        db_person.age = age
        db.commit()
        db.refresh(db_person)
        return db_person

def delete_person(db: Session, user_id: int):
    db_person = db.query(Person).filter(Person.id == user_id).first()
    if db_person:
        db.delete(db_person)
        db.commit()