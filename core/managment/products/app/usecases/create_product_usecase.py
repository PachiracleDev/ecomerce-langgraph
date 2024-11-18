from sqlalchemy.orm import Session
from core.managment.products.domain.product_schema import ProductSchema
from core.managment.products.domain.product_model import Product

def execute(session: Session, product: ProductSchema):
    new_product = Product(
         **product.model_dump()
    )
    session.add(new_product)
    session.commit()
    return new_product.__dict__