from enum import Enum
from typing import Optional

from pydantic import BaseModel


class BlogType(str, Enum):
    short: str = "short"
    story: str = "story"
    howto: str = "howto"


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
