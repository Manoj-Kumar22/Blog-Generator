from typing import TypedDict
from pydantic import BaseModel,Field

class Blog(BaseModel):
    title:str=Field(description="The Title of the Blog post")
    content:str=Field(description="The main content of the Blog post")

class BlogState(TypedDict):
    topic:str
    blog:Blog
    current_language:str
