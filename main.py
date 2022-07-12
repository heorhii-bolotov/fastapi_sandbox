from enum import Enum
from fastapi import FastAPI, status, Response
from typing import Dict, Optional


app = FastAPI()


class BlogType(str, Enum):
    short: str = "short"
    story: str = "story"
    howto: str = "howto"


@app.get("/")
def index() -> Dict[str, str]:
    return {"message": "Hello World"}


@app.get(
    "/blog/all",
    tags=["blog"],
    summary="Retrieve all blogs",
    description="This api call simulates fetching all blogs.",
    response_description="This list of available blogs"
)
def get_all_blogs(page: int = 1, page_size: Optional[int] = None) -> Dict[str, str]:
    return {"message": f"All {page_size} blogs on page {page}"}


@app.get("/blog/{id}/comments/{comment_id}", tags=["blog", "comment"])
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
) -> Dict[str, str]:
    """
    Simulates retrieving a comment of a blog

    Args:
    - id (int): _description_
    - comment_id (int): _description_
    - valid (bool, optional): _description_. Defaults to True.
    - username (Optional[str], optional): _description_. Defaults to None.

    Returns:
        Dict[str, str]: _description_
    """
    
    return {
        "message": f"blog id {id}, comment id {comment_id}, valid {valid}, username {username}"
    }


@app.get("/blog/type/{type}", tags=["blog"])
def get_blog_type(type: BlogType) -> Dict[str, str]:
    return {"message": f"Blog type is {type}"}


@app.get("/blog/{id}", status_code=status.HTTP_200_OK, tags=["blog"])
def get_blog(id: int, response: Response) -> Dict[str, str]:
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found"}
    return {"message": f"Blog id is {id}"}
