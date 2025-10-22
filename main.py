from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        'id': 1,
        'title': 'Асинхронность в Python',
        'author': 'Пушкин',
    },
    {
        'id': 2,
        'title': 'Backend в Python',
        'author': 'Артем'
    }
]

@app.get('/books', tags=["Книги"], summary="Получить все книги")
def read_books():
    return books

@app.get('/books/{book_id}', tags=["Книги"], summary="Получить книгу")  # ← Исправил параметр
def get_book(book_id: int):  # ← Должно совпадать с {book_id} в пути
    for book in books:
        if book["id"] == book_id: 
            return book
    # ← Убрал отступ, чтобы исключение вызывалось после проверки всех книг
    raise HTTPException(status_code=404, detail="Книга не найдена")

class NewBook(BaseModel):
    title: str
    author: str

@app.post("/books", tags=["Книги"])
def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author
    })
    return {"success": True}

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)