from sqlalchemy.orm import Session
from core.managment.products.presenters.dtos.get_products_dto import GetProductsDto
from core.managment.products.domain.product_model import Product
from core.managment.categories.domain.category_model import Category
from sqlalchemy.dialects.postgresql import VARCHAR

def execute(session: Session, filters: GetProductsDto):
    query = session.query(Product)

    if filters.range_price:
        query = query.filter(Product.price.between(filters.range_price[0], filters.range_price[1]))
    if filters.category_name:
        query = query.filter(Product.category.has(Category.name.ilike(f"{filters.category_name}%")))

    if filters.color:
        query = query.filter(Product.color == filters.color)
        
    if filters.name:
        query = query.filter(Product.name.ilike(f"%{filters.name}%"))
    
  
    if filters.size:
        query = query.filter(Product.sizes.cast(VARCHAR).like(f"%{filters.size.upper()}%"))

    return query.limit(filters.limit).offset((filters.page - 1) * filters.limit).all()