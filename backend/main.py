#Import Libraries
from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel, EmailStr, Field
from typing import List
from threading import Lock

#initialize FASTAPI app
app = FastAPI(title = "Student Management API", version ="1.0.0")

# In-memory storage for students
students = [] # List to store student
next_id = 1 # Auto-increment student ID
lock = Lock()  # Lock for thread safety

#MODELS

#Model for Create A New Student
class StudentCreate(BaseModel):
    name: str = Field(..., min_length = 1, example = "Joyson Peries")
    email: EmailStr = Field(..., example = "joys@gmail.com")
    course: str = Field(..., min_length = 1, example = "Machine Learning")

#Model for return student Data with Id

class StudentOut(StudentCreate):
    id: int

#Routes

#root endpoint to check if the api is running or not
@app.get("/")
def root():
    return {"message":"API is Running"}

#Create A New Student 
@app.post("/students/", response_model = StudentOut, status_code = status.HTTP_201_CREATED)
def add_student(student: StudentCreate):
    global next_id
    
    #check duplicate Emails
    for s in students:
        if s["email"] == student.email:
            raise HTTPException(
                status_code = 400,
                detail="A student with this Email already exists"
            )
    
    #thread safe storage      
    with lock:
        student_dict = student.model_dump()
        student_dict["id"] = next_id
        students.append(student_dict)
        next_id += 1
        
    return student_dict

#List All Students
@app.get("/students/", response_model=list[StudentOut])
def list_students():
    return students

#Delete a student by id
@app.delete("/students/{student_id}",response_model = StudentOut)
def delete_student(student_id: int):
    
    for i, s in enumerate(students):
        if s["id"] == student_id:
            deleted = students.pop(i)
            return deleted
        
    raise HTTPException(
        status_code= 404,
        detail = "Student not Found."
    )
    
