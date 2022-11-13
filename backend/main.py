from fastapi import FastAPI
from db import models
from db.database import engine
from routers import users, post


app = FastAPI()
app.include_router(users.router)
app.include_router(post.router)

@app.get("/")
def root():
    return "Hello world!"

models.Base.metadata.create_all(engine)
