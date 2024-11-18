from pydantic import BaseModel, Field
from typing import Literal

class SignupDto(BaseModel):
    email: str = Field(..., email=True)
    phone: str = Field(..., min_length=9, max_length=9)
    name: str = Field(..., min_length=3, max_length=50)
    
    # Enum: MEN or WOMEN
    gender: str = Literal["MEN", "WOMEN"]
    password: str = Field(..., min_length=8, max_length=50)