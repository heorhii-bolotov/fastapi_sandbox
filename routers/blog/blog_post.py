from typing import Optional
from fastapi import FastAPI, status, Response, APIRouter, Query, Path, Body
from pydantic import BaseModel
from models.blog.blog import BlogModel

router = APIRouter(prefix="/blog", tags=["blog"])


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1) -> Response:
    return {"id": id, "data": blog, "version": version}


@router.post("/new/{id}/comment")
def create_comment(
    blog: BlogModel,
    id: int,
    comment_id: int = Query(
        None,
        title="Id of the comment",
        description="Some description for comment_id",
        alias="commentId",
        deprecated=True,
    ),
    content: str = Body(..., min_length=10, max_length=50, regex='^[a-z\s]*$')
) -> Response:
    return {"id": id, "blog": blog, "comment_id": comment_id, "content": content}
