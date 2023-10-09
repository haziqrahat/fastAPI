from fastapi import FastAPI, HTTPException
from models import *
from typing import List

app=FastAPI()

#Setup the data

db: List[User]=[
    User(
        id= '1101',
        first_name="John",
        last_name='Kirby',
        gender=Gender.male,
        role=Role.admin
    ),
    User(
        id= '1102',
        first_name="John",
        last_name='Karen',
        gender=Gender.female,
        role=Role.admin
    )
    ]

#define the root method
@app.get('/')
def root():
    return {"testing":"db"}

#define the get method
@app.get('/api/v1/users')
async def getUsers():
    return db

#define the post method
@app.post('/api/v1/users')
async def addUsers(user:User):
    db.append(user)
    return {"id":user.id}

#define the delete method
@app.delete('/api/v1/users/{user_id}')
async def deleteUsers(user_id):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            
    return {"item deleted"}
            
#define the put method
@app.put('/api/v1/users/{user_id}')
async def updateUsers(body:UserUpdate,user_id:str):
    for user in db:
        if user.id==user_id:
            if body.first_name is not None:
                user.first_name=body.first_name
            if body.last_name is not None:
                user.last_name=body.last_name    
            if body.gender is not None:
                user.gender=body.gender
            if body.role is not None:
                user.role=body.role
                    
    return {"updated"}

    