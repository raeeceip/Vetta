from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

class Industry(BaseModel):
    industryname: str
