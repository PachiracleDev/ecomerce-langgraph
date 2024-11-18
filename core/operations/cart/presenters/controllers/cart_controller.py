from fastapi import APIRouter, Depends
from shared.db.database import get_db
from shared.utils.jwt import get_current_user, TokenData
from typing import Annotated
from core.operations.cart.presenters.dtos.add_item_to_cart_dto import AddItemToCartDto
from core.operations.cart.presenters.dtos.update_item_cart_dto import UpdateItemCartDto
from core.operations.cart.presenters.dtos.remove_item_to_cart_dto import RemoveItemToCartDto
from core.operations.cart.app.usecases import add_item_to_cart_usecase, get_cart_items_usecase, clean_cart_usecase, remove_item_to_cart_usecase, update_item_cart_usecase

router = APIRouter(prefix='/cart', tags=['Cart'])

@router.post('/add-item')
def add_item_to_cart(
    dto: AddItemToCartDto,
    current_user: Annotated[TokenData, Depends(get_current_user)],
    db = Depends(get_db)
):
    return add_item_to_cart_usecase.execute(db, current_user.user_id, dto)

@router.put('/update-item')
def update_item_cart(
    dto: UpdateItemCartDto,
    current_user: Annotated[TokenData, Depends(get_current_user)],
    db = Depends(get_db)
):
    return update_item_cart_usecase.execute(db, current_user.user_id, dto)


@router.delete('/remove-item')
def remove_item_to_cart(
    dto: RemoveItemToCartDto,
    current_user: Annotated[TokenData, Depends(get_current_user)],
    db = Depends(get_db)
):
    return remove_item_to_cart_usecase.execute(db, current_user.user_id, dto.item_id)

@router.delete('/clean-cart')
def clean_cart(
    current_user: Annotated[TokenData, Depends(get_current_user)],
    db = Depends(get_db)
):
    return clean_cart_usecase.execute(db, current_user.user_id)

@router.get('/get-items')
def get_cart_items(
    current_user: Annotated[TokenData, Depends(get_current_user)],
    db = Depends(get_db)
):
    return get_cart_items_usecase.execute(db, current_user.user_id)