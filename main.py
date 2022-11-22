from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.get('/blog/{id}')
def show_blog(id):
    return {'data': f'show blog with id - {id}'}


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}