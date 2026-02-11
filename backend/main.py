#Import Libraries
from fastapi import FastAPI, HTTPException,status

#initialize FASTAPI app
app = FastAPI(title = "Student Management API", version ="1.0.0")

#Routes

#root endpoint to check if the api is running or not
@app.get("/")
def root():
    return {"message":"API is Running"}