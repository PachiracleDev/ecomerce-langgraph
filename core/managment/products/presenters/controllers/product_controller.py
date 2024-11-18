from fastapi import APIRouter, Path, Depends, Query
from core.managment.products.app.usecases import create_product_usecase, delete_product_usecase, get_products_usecase, update_product_usecase
from core.managment.products.presenters.dtos.create_product_dto import CreateProductDto
from core.managment.products.presenters.dtos.update_product_dto import UpdateProductDto
from core.managment.products.presenters.dtos.get_products_dto import GetProductsDto
from sqlalchemy.orm import Session
from shared.db.database import get_db

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/create")
def create_product(body: CreateProductDto, db: Session = Depends(get_db)):
    return create_product_usecase.execute(db, body)

@router.put("/update/{product_id}")
def update_product(
    body: UpdateProductDto,
    product_id: int = Path(..., title="The ID of the product to update", ge=1),
    db: Session = Depends(get_db)
):
    return update_product_usecase.execute(db, product_id, body)


@router.delete("/remove/{product_id}")
def remove_product(product_id: int = Path(..., title="The ID of the product to remove", ge=1), db: Session = Depends(get_db)):
    return delete_product_usecase.execute(db, product_id)


@router.get("/list")
def list_products(filters: GetProductsDto, db: Session = Depends(get_db)):
    return get_products_usecase.execute(db, filters)