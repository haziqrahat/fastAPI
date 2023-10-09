from fastapi import FastAPI
import random

app=FastAPI()

def fact(n):
    n=int(n)
    if n<2:
        return 1
    else:
        return n*fact(n-1)

@app.get('/')
async def root():
    return {'example':'fastapi','data':100}

@app.get('/random')
async def get_number():
    num=random.randint(1,100)
    return {'example': 'fastapi', 'data': num}

@app.get('/random')
async def get_number():
    num = random.randint(1, 100)
    return {'example': 'fastapi', 'data': num}

@app.get('/factorial/{num}')
async def get_number(num):
    result=fact(num)
    return {'method': 'factorial recursion', 'number': num,'result':result}


