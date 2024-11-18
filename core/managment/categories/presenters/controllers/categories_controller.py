from fastapi import APIRouter, Depends, Path
from core.managment.categories.presenters.dtos.create_category_dto import CreateCategoryDto
from core.managment.categories.presenters.dtos.update_category_dto import UpdateCategoryDto
from sqlalchemy.orm import Session
from shared.db.database import get_db
from core.managment.categories.app.usecases import create_category_usecase, get_categories_usecase, remove_category_usecase,update_category_usecase

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/create")
def create_category(body: CreateCategoryDto, db: Session = Depends(get_db)):
    
    return create_category_usecase.execute(db, body)

@router.put("/update/{category_id}")
def update_category( 
    body: UpdateCategoryDto,
    category_id: int = Path(..., title="The ID of the category to update", ge=1),
    db: Session = Depends(get_db)
):
    return update_category_usecase.execute(db, category_id, body)


@router.delete("/remove/{category_id}")
def remove_category(category_id: int = Path(..., title="The ID of the category to remove", ge=1), db: Session = Depends(get_db)):
    return remove_category_usecase.execute(db, category_id)


@router.get("/list")
def list_categories(db: Session = Depends(get_db)):
    print(db, "db")
    return get_categories_usecase.execute(db)