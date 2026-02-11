#Import Libraries
from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel, EmailStr, Field

#initialize FASTAPI app
app = FastAPI(title = "Student Management API", version ="1.0.0")

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
    return 

#List All Students
@app.get("/students/", response_model=list[StudentOut])
def list_students():
    return #students list

#Delete a student by id
@app.delete("/students/{student_id}",response_model=StudentOut)
def delete_student(student_id: int):
    return
