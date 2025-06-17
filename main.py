from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app=FastAPI()

class Post(BaseModel):
    Title:str
    Content:str
    id:int


my_posts=[{"Title":"Title of Post 1","Content":"Content of  Post 1","id":1},
          {"Title":"My Favourite Food","Content":"My Favourite Food is Idli"}]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def login():
    return {"Data":my_posts}


@app.post('/posts')
async def func(new_post:Post):
    print(new_post)
    print(new_post.dict())
    return  new_post