from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List
from enum import Enum

class Gender(str,Enum):
    male='male'
    female='female'

class Role(str,Enum):
    admin='admin'  
    user='user'
    student='student'
    

class User(BaseModel):
    id:str
    first_name:str
    last_name:str
    gender:Gender
    role:Role
    

class UserUpdate(BaseModel):
    first_name:Optional[str]
    last_name:Optional[str]
    gender:Optional[Gender]
    role:Optional[List[Role]]

    
    

