from sqlalchemy.orm import Session
from core.managment.categories.domain.category_model import Category
from sqlalchemy.orm import aliased, joinedload

def execute(session: Session):
    Subcategory = aliased(Category)
    results = session.query(Category).outerjoin(Subcategory, Category.subcategories).options(joinedload(Category.subcategories)).all()
    return results