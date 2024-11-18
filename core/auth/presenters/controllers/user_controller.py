from fastapi import APIRouter, Depends
from typing import Annotated
from core.auth.presenters.dtos.update_user_billing_dto import UpdateUserBillingDto
from core.auth.app.usecases import update_user_billing_usecase, get_my_profile_usecase, get_my_user_billing_usecase
from shared.utils.jwt import get_current_user, TokenData

from sqlalchemy.orm import Session
from shared.db.database import get_db

router = APIRouter(prefix='/users', tags=['auth'])

@router.get('/get_my_profile')
async def get_my_profile(
    current_user: Annotated[TokenData, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    return get_my_profile_usecase.execute(db, current_user.user_id)

@router.put('/billing')
async def update_billing(
    current_user: Annotated[TokenData, Depends(get_current_user)],
    dto: UpdateUserBillingDto,
    db: Session = Depends(get_db)
):
    return update_user_billing_usecase.execute(db, current_user.user_id, dto)


@router.get('/billing')
async def signup(
    current_user: Annotated[TokenData, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    return get_my_user_billing_usecase.execute(db, current_user.user_id)