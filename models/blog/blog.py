from enum import Enum
from typing import Dict, List, Optional

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
    tags: List[str] = []
    metadata: Dict[str, str] = {"key1": "value1"}


class Image(BaseModel):
    url: str
    alias: str
