from sqlalchemy.orm import Session
from core.managment.categories.domain.category_schema import CategorySchema
from core.managment.categories.domain.category_model import Category

def execute(session: Session, category: CategorySchema):
    new_category = Category(**category.model_dump())
    session.add(new_category)
    
    session.commit()
    session.refresh(new_category)
    
    return new_category.__dict__