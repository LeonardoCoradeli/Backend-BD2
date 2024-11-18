from app.domain.BaseModel import BaseModel
from pydantic import EmailStr

class User(BaseModel):
    username: str
    email: EmailStr
    password_hash: str

