from pydantic import BaseModel, Field

class SigninDto(BaseModel):
    email: str = Field(..., email=True)
    password: str = Field(..., min_length=8, max_length=50)