from fastapi import Depends, FastAPI, Response, HTTPException
from functools import lru_cache
from fastapi_sso.sso.google import GoogleSSO
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.requests import Request
from src.auth.router import routerUser
from .config import settings
from src.auth import models, schemas, crud
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routers
app.include_router(routerUser)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


app = FastAPI()

app.include_router(routerUser)

google_sso = GoogleSSO(settings.GOOGLE_CLIENT_ID, settings.GOOGLE_CLIENT_SECRET, "http://localhost:8000/google/callback")


@app.get("/google/login")
async def google_login():
    """Generate login url and redirect"""
    return await google_sso.get_login_redirect()


@app.get("/google/callback")
async def google_callback(request: Request):
    """Process login response from Google and return user info"""
    user = await google_sso.verify_and_process(request)
    request.session["user"] = dict(user)
    return {
        "id": user.id,
        "picture": user.picture,
        "display_name": user.display_name,
        "email": user.email,
        "provider": user.provider,
    }


@app.get('/')
async def home(request: Request):
    user = request.session.get("user")
    if user is not None:
        email = user['email']
        html = (
            f'<pre>Email: {email}</pre><br>'
            '<a href="/docs">documentation</a><br>'
            '<a href="/logout">logout</a>'
        )
        return HTMLResponse(html)
    return HTMLResponse('<a href="/google/login">login</a>')


@app.get('/logout', tags=['authentication'])
async def logout(request: Request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')



# Middleware
app.add_middleware(SessionMiddleware, secret_key="some-random-string")