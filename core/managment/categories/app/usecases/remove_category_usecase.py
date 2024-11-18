from sqlalchemy.orm import Session
from core.managment.categories.domain.category_model import Category

def execute(session: Session, category_id: int):
    category = session.query(Category).filter(Category.id == category_id).first()
    if category is None:
        return None
    session.delete(category)
    session.commit()
    return category.__dict__