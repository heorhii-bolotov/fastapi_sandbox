from enum import Enum
from fastapi import FastAPI, Request, status, Response
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import HTTPException
from typing import Dict, Optional
from db import models
from db.database import engine
from exceptions.base import StoryException

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


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT, content={"detail": exc.name}
    )


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: HTTPException):
#     return PlainTextResponse(str(exc), status_code=status.HTTP_400_BAD_REQUEST)


@app.get("/")
def index() -> Dict[str, str]:
    return {"message": "Hello World"}
