from fastapi import FastAPI
from db import models
from db.database import engine
from routers import users, post, comment
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from auth import authentication


app = FastAPI()
app.include_router(users.router)
app.include_router(post.router)
app.include_router(authentication.router)
app.include_router(comment.router)


@app.get("/")
def root():
    return "Hello world!"

origins = [
    'http://localhost:3000',
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

models.Base.metadata.create_all(engine)
app.mount('/images', StaticFiles(directory='images'), name='images')
