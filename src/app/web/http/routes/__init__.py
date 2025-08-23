from fastapi import APIRouter

from app.web.http.routes import sentiment

router = APIRouter()

router.include_router(sentiment.router)
