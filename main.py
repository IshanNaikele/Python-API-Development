from fastapi import FastAPI

app=FastAPI()

@app.get("/simple")
async def root():
    return {"message": "Hsdfghjklellfghjko World"}

@app.get("/")
async def login():
    return {"message":"You have to Sign Up First"}