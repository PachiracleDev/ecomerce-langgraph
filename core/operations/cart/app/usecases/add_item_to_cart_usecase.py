from core.operations.cart.presenters.dtos.add_item_to_cart_dto import AddItemToCartDto
from sqlalchemy.orm import Session
from core.operations.cart.domain.cart_schema import CartSchema
from core.operations.cart.domain.cart_item_schema import CartItemSchema

def execute(session: Session, user_id: int, dto: AddItemToCartDto):
    cart = session.query(CartSchema).filter(CartSchema.user_id == user_id).first()

    cart_item = CartItemSchema(
        cart_id=cart.id,
        product_id=dto.product_id,
        quantity=dto.quantity,
        sizes=dto.sizes
    )
    
    session.add(cart_item)
    
    session.commit()
    
    return cart_item
  