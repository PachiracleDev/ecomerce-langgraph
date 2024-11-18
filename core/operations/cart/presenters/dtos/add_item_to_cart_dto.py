from pydantic import BaseModel

class AddItemToCartDto(BaseModel):
    quantity: int
    product_id: int
    sizes: dict