from pydantic import BaseModel
from typing import List, Optional


class GetProductsDto(BaseModel):
    range_price: List[int] = []
    color: str = None
    size: str = None
    category_name: str = None
    name: str = None
    
 
    #PAGINATION
    limit: int = 10
    page: int = 1