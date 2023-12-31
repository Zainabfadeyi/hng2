# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import declarative_base
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "sqlite:///mydatabase.db"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
# class Person(Base):
#     __tablename__ = "people"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     age = Column(Integer)

# Base.metadata.create_all(bind=engine)

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL#, connect_args = {"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)


Base = declarative_base()
class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)

Base.metadata.create_all(bind=engine)