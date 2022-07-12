from enum import Enum
from fastapi import FastAPI, status, Response
from typing import Dict, Optional

from routers.blog import blog_post
from routers.blog import blog_get

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/")
def index() -> Dict[str, str]:
    return {"message": "Hello World"}
