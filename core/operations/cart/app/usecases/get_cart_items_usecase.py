from sqlalchemy.orm import Session, joinedload
from core.operations.cart.domain.cart_item_schema import CartItemSchema
from core.operations.cart.domain.cart_schema import CartSchema
from core.managment.products.domain.product_model import Product

def execute(session: Session, user_id: int):
    
    cart = session.query(CartSchema).filter(CartSchema.user_id == user_id).first()
    
    cart_items = session.query(CartItemSchema).filter(CartItemSchema.cart_id == cart.id).options(joinedload(CartItemSchema.products)).all()
    return cart_items