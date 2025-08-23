from pydantic_settings import BaseSettings


class HttpConfig(BaseSettings):
    APP_TITLE: str = "Call Summary Sentiment Classification API"
    HOST: str = "0.0.0.0"
    PORT: int = 8080
    UVICORN_LOG_LEVEL: str = "debug"


config = HttpConfig()
