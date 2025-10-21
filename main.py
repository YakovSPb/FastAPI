from fastapi import FastAPI

from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()

data = {
    "email": 'abc@mail.ru',
    'bio': None,
    'age': 12,
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=1000)
    
    # Правильный способ установки конфигурации модели

users = []
    
@app.post('/users')
def add_user(user: UserSchema):
    users.append(user)
    return {"ok": True, "msg": "Юзер добавлен"}
    
@app.get('/users')
def get_users():
    return users
    

class UserAgeScheme(UserSchema):
    age: int = Field(ge=0, le=130)

# print(repr(UserAgeScheme(**data)))