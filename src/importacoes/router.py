from fastapi import Depends, HTTPException, Request, APIRouter
from src.auth import schemas, crud, exceptions
from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi.security import (
    OAuth2PasswordRequestForm,
)

from src.config import settings
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
