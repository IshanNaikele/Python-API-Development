from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from fastapi import HTTPException
import random
import psycopg2 
from psycopg2.extras import RealDictCursor
import time
app=FastAPI()

class Post(BaseModel):
    Title:str
    Content:str
    id:int
while True:
    try :
        conn = psycopg2.connect(
        dbname="FastAPI",
        user="postgres",
        password="23062004#Ishan",
        host="localhost",
        port="5432",
        cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("DataBase Connected")
        break
    except Exception as error :
        print("DataBaase Failed to Connect")
        print(error)
        time.sleep(3)



 
my_posts=[{"Title":"Title of Post 1","Content":"Content of  Post 1","id":1},
          {"Title":"My Favourite Food","Content":"My Favourite Food is Idli","id":2}]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def login():
    return {"Data":my_posts}


@app.post('/posts')
async def func(new_post:Post):
    post_dict=new_post.dict()
    print(post_dict)
    print(new_post)
    id_no=random.randint(1,100000000)
    post_dict['id']=id_no
    my_posts.append(post_dict)
    return  my_posts
 

@app.get("/retrieve_post/{id}")
async def get_requested_post(id):
     
    return {"data":f"Here is Post :{id}"}

@app.get('/find_posts/{id}')
async def find_posts(id :int ):
    print(id)
    for p in my_posts:
        if p["id"]==id:
            return p
        
    raise HTTPException(status_code=404, detail=f"Post with id {id} not found")

@app.delete('/posts/{id}')
async def delete_post(id: int):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            my_posts.pop(i)
            return {"message": f"Post with id {id} deleted successfully", "data": my_posts}
    
    # Post not found
    raise HTTPException(status_code=404, detail=f"Post with id {id} not found")


@app.put('/posts/{id}')
async def update_post(id:int,new_post:Post):
    print(new_post)
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            post_dict=new_post.dict()
            post_dict['id']=id
            my_posts[i]=post_dict
            return {"Data":my_posts}
    
    # Post not found
    raise HTTPException(status_code=404, detail=f"Post with id {id} not found")