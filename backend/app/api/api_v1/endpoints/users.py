from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException, status
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings


router = APIRouter()


@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(
    *, 
    db: Session = Depends(deps.get_db),
    password: str = Body(...),  # TODO add minimal password requirements
    email: EmailStr = Body(...),
    full_name: str = Body(None)
) -> Any:
    # check if user with this email already exists
    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="This email address is already in use"  # TODO 
        )
    # create user in database
    user_in = schemas.UserCreate(password=password, email=email, full_name=full_name)
    user = crud.user.create(db, obj_in=user_in)
    return user