from app.core.config import config as core_config
from app.core.sentiment_service import SentimentAnalyzer

_sentiment_analyzer = SentimentAnalyzer(
    inference_endpoint_for_mixed=core_config.INFERENCE_ENDPOINT_FOR_MIXED,
    inference_endpoint_for_arabic=core_config.INFERENCE_ENDPOINT_FOR_ARABIC,
    inference_endpoint_for_latin=core_config.INFERENCE_ENDPOINT_FOR_LATIN,
)


def sentiment_analyzer() -> SentimentAnalyzer:
    return _sentiment_analyzer
