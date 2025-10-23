
from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy import select

from src.api.dependencies import SessionDep
from src.database import Base, engine
from src.models.books import BookModel
from src.schemas.books import BookGetSchema, BookSchema, BaseModel, Field

router = APIRouter()

@router.post("/setap")    
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"ок": True}

@router.post("/books")
async def add_book(data: BookSchema, session: SessionDep) -> BookSchema:
  new_book = BookModel(
      title=data.title,
      author=data.author,
  )  
  session.add(new_book)
  await session.commit()
  return {"title":data.title, "author":data.author}
    
# @router.get("/books")
# async def get_books(session: SessionDep) -> list[BookGetSchema]:
#     query = select(BookModel)
#     result = await session.execute(query)
#     return result.scalars().all()

class PaginationParams(BaseModel):
    limit: int = Field(5, ge=0, le=100, description="Кол-во элементов на страницу")
    offset: int = Field(0, ge=0, description="Смещение для пагинации")

PaginationDep = Annotated[PaginationParams, Depends(PaginationParams)]

@router.get("/books")
async def get_books(
    session: SessionDep,
    pagination: PaginationDep,
    ) -> list[BookGetSchema]:
    query = (
        select(BookModel)
        .limit(pagination.limit)
        .offset(pagination.offset)
        )
    result = await session.execute(query)
    return result.scalars().all()



# test
# async def test_get_session():
#     async with session() as session:
#         yield session
        
# router.dependency_overrides[get_session] = test_get_session