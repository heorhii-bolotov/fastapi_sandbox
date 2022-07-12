from typing import Dict, List, Optional
from fastapi import FastAPI, status, Response, APIRouter, Query, Path, Body
from pydantic import BaseModel
from models.blog.blog import BlogModel

router = APIRouter(prefix="/blog", tags=["blog"])


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1) -> Response:
    return {"id": id, "data": blog, "version": version}


@router.post("/new/{id}/comment/{comment_id}")
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: int = Query(
        None,
        title="Title of the comment",
        description="Some description for comment_title",
        alias="commentTitle",
        deprecated=True,
    ),
    content: str = Body(..., min_length=10, max_length=50, regex="^[a-z\s]*$"),
    v: Optional[List[str]] = Query(["1.1", "1.2", "1.3"]),
    comment_id: int = Path(None, gt=5, le=10),
) -> Response:
    return {
        "id": id,
        "blog": blog,
        "comment_id": comment_id,
        "comment_title": comment_title,
        "content": content,
        "version": v,
    }


def required_functionality() -> Dict[str, str]:
    return {"message": f"Learning FastAPI is important"}
