from sqlalchemy.orm import Session
from core.managment.products.domain.product_schema import ProductSchema
from core.managment.products.domain.product_model import Product
from sqlalchemy.exc import NoResultFound

def execute(session: Session, product_id: int, product: ProductSchema):
    try:
        product_to_update = session.query(Product).filter(Product.id == product_id).one()
        
        
        update_data = {key: value for key, value in product.__dict__.items() if value is not None}

        
        session.query(Product).filter(Product.id == product_id).update(update_data)
        session.commit()
    
        return product_to_update.__dict__
    
    except NoResultFound:
        raise ValueError(f'Product with id {product_id} not found.')
    except Exception as e:
        session.rollback()
        raise e