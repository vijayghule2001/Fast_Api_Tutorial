from typing import List

from fastapi import FastAPI
from pydantic import BaseModel


class userCreate(BaseModel):
    name:str
    mobile:str
    gmail: str
    password:str
    
    
class response_User(BaseModel):
    name:str
    mobile:str
    gmail: str
    
app =  FastAPI()
users = []

@app.post("/user", response_model=response_User)
def add_user(user:userCreate):
    if user:
        users.append(user)
        return  user
    
    
@app.get("/user", response_model= List[response_User])
def get_user():
    return users

    