from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
app =  FastAPI()

userList = []

class AddUser(BaseModel):
    id:int
    name:str
    mobile:str
    gmail:str
    address :Optional[str] = None
    

@app.post("/user")
def add_user(user:AddUser):
    userList.append(user)
    return {
        "message":"User Add Sucessfully",
        "user":user
    }
    
@app.get("/user")
def get_user():
    return userList   

@app.get("/user/{id}")
def get_user_by_id(id:int):
    for item in userList:
        if item.id == id:
            return item
    return {
        "msg":"user not found  "
    }

@app.put('/user/{id}')
def update_user(id:int, user_data:AddUser):
    for index , user in enumerate(userList):
        if user.id ==  id:
            userList[index] = user_data
            return{
                "message":"user Update sucessfully",
                "user": user_data
            }    

@app.delete('/user/{id}')
def delete_user(id:int):
    for user in userList:
        if user.id == id:
            userList.pop(user)
            return user
    return{
        "error":"user not found "
    }                