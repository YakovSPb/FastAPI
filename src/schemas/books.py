from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    title: str
    author: str

class BookGetSchema(BaseModel):
    id: int
    title: str
    author: str