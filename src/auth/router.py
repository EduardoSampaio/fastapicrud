from fastapi import Depends, HTTPException, Request, APIRouter
from src.auth import schemas, crud, exceptions
from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi.security import (
    OAuth2PasswordRequestForm,
)

from src.config import settings
from src.auth.utils import (create_refresh_token, get_current_user, create_access_token)
from src.database import SessionLocal

routerUser = APIRouter(
    prefix="/api/v1",
    tags=["users"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@routerUser.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@routerUser.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
               user: dict = Depends(get_current_user)):
    if user is None:
        raise exceptions.get_user_exception()
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@routerUser.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@routerUser.post("/users/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise exceptions.token_exception()
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRES_IN)
    access_token = create_access_token(
        data={"sub": user.email, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token,
            "refresh_token": create_refresh_token(form_data.username),
            "token_type": "bearer"}
