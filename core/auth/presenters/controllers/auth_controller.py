from fastapi import APIRouter, Depends, HTTPException
from core.auth.presenters.dtos.signin_dto import SigninDto
from core.auth.presenters.dtos.signup_dto import SignupDto
from core.auth.app.usecases import signin_usecase, signup_usecase
from sqlalchemy.orm import Session
from shared.db.database import get_db

router = APIRouter(prefix='/auth', tags=['auth'])

@router.post('/signin')
async def signin(
    dto: SigninDto,
    db: Session = Depends(get_db)
):
    return signin_usecase.execute(db, dto)


@router.post('/signup')
async def signup(
    dto: SignupDto,
    db: Session = Depends(get_db)
):
    return signup_usecase.execute(db, dto)