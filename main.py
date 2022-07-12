from enum import Enum
from fastapi import FastAPI, status, Response
from typing import Dict, Optional
from db import models
from db.database import engine

from routers.blog import blog_post
from routers.blog import blog_get
from routers.user import user
from routers.article import article

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)

models.Base.metadata.create_all(engine)


@app.get("/")
def index() -> Dict[str, str]:
    return {"message": "Hello World"}
