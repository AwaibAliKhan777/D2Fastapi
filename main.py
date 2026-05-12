#import fastapi framework

from fastapi import FastAPI , Depends , HTTPException

#sqlalchemy components for DB table execution 
from sqlalchemy import Column, Integer , String

#session is used to interact with DB
from sqlalchemy.orm import Session

#pydantic is used for request validation
from pydantic import BaseModel

#DB connection tools
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#create fastapi app instance
app = FastAPI()

#----------------------Database setup--------------------

#sqlite database file

DATABASE_URL = "sqlite:///./students.db"

#create engine (connection to DB)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread" : False} #needed for sqlite
)

#create session(used to talk with DB)
SessionLocal = sessionmaker(bind=engine)

#Base class for models (tables)
Base = declarative_base()

#----------------DATABASE MODEL--------------

#this class represents the db table
class Student(Base):
    __tablename__ = "students"  #table name in Db

    id = Column(Integer, primary_key=True , index=True) #Primary key
    name = Column(String) #Student name
    age = Column(Integer) #Student age

#----------------------------pydantic schema-------------

#this is used for request body validation(input)
class StudentSchema(BaseModel):
    name : str
    age : int

#-----------------create table-----------------------------------

class StudentSchema(BaseModel):
    name : str
    age : int

#--------------------create table----------------------------------

#This will create table in DB (if not exists)
Base.metadata.create_all(bind = engine)


#-------------------------Dependency (DB session)

#This function provides DB session to routes

def get_db():
    db = SessionLocal() #open DB connection
    try:
        yield db # give db session to api
    finally:
        db.close() # always close connection

#------------------------crud operations

#create student
@app.post("/students")
def create_student(student:StudentSchema , db:Session = Depends(get_db)):

    #create new Student object
    new_student = Student(name=student.name , age= student.age)

    db.add(new_student)  #add to DB
    db.commit() # save changes
    db.refresh(new_student) #get updated data(like ID)

    return new_student

#read one student by id

@app.get("/students/{id}")
def get_student(id:int , db:Session = Depends(get_db)):
    #find student by ID
    
    student = db.query(Student).filter(Student.id == id).first()



    #if not found -> error

    if not student:
        raise HTTPException(status_code=404 , detail="Not found")

    return student

#update student
@app.put("/students/{id}")
def update_student(id:int , updated: StudentSchema , db:Session = Depends(get_db)):

    #find student
    student = db.query(Student).filter(Student.id == id).first()

    if not student : 
        raise HTTPException(status_code=404 , detail = "Not found")

    #update values

    student.name = updated.name
    student.age = updated.age

    db.commit() # save changes

    return student

#delete student
@app.delete("/students/{id}")
def delete_student(id :int , db:Session = Depends(get_db)):
     #find student

     student = db.query(Student).filter(Student.id == id).first()


     if not student:
         raise HTTPException(status_code=404 , detail = "Not found")
     
    #delete student
     db.delete(student)  #delete from db
     db.commit() #save changes

     return {"message" : "Deleted"}