from pydantic import BaseModel

class User(BaseModel):
    email: str
    phone: str
    name: str
    gender: str
    password: str