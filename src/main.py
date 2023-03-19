from fastapi import Depends, FastAPI, HTTPException, Request, Response
from functools import lru_cache
from src.auth.router import routerUser
from .config import settings
from src.auth import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@lru_cache()
def get_settings():
    return settings


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(routerUser)
