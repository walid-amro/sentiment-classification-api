from pathlib import Path

from pydantic_settings import BaseSettings


class CoreConfig(BaseSettings):
    LOG_FILE_PATH: Path | None = None
    LOG_FILE_MAX_BYTES: int = 10485760

    INFERENCE_ENDPOINT_FOR_MIXED: str = "http://127.0.0.1:8000/classify"
    INFERENCE_ENDPOINT_FOR_ARABIC: str | None = None
    INFERENCE_ENDPOINT_FOR_LATIN: str | None = None


config = CoreConfig()
