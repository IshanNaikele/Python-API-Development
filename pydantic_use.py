from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body

app=FastAPI()

class info(BaseModel):
    Name:str
     
    Roll_No:int
    CGPA:float  

@app.post('/checkInfo')
async def checkInfo(student:info):
    print(student)
    print(student.dict())
    return student
       

