from sqlalchemy.orm import Session
from core.managment.products.domain.product_model import Product

def execute(session: Session, product_id: int):
    product = session.query(Product).filter(Product.id == product_id).one()
    session.delete(product)
    session.commit()
    return product.__dict__