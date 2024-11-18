from pydantic import BaseModel
from typing import Optional

class CategorySchema(BaseModel):
    name: str
    parent_id: Optional[int] = None
    