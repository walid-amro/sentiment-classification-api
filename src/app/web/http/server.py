import uvicorn
from fastapi import FastAPI

from app.web.http.config import config as http_config
from app.web.http.routes import router

app = FastAPI(title=http_config.APP_TITLE, version="1.0.0")
app.include_router(router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok"}


def run():
    uvicorn.run(
        app,
        host=http_config.HOST,
        port=http_config.PORT,
        log_level=http_config.UVICORN_LOG_LEVEL,
    )
