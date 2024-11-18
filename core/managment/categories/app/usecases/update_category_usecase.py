from sqlalchemy.orm import Session
from core.managment.categories.domain.category_model import Category
from core.managment.categories.domain.category_schema import CategorySchema


def execute(session: Session, category_id: int, catg: CategorySchema):
    category = session.query(Category).filter(Category.id == category_id).first()
    if category is None:
        return None
    category.name = catg.name
    category.parent_id = catg.parent_id
    session.commit()
    return category.__dict__