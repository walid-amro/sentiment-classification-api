from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.sentiment_service import SentimentAnalyzer
from app.web.http.dependencies import sentiment_analyzer
from app.web.http.model import SentimentRequest, SentimentResponse

router = APIRouter(prefix="/sentiment", tags=["Sentiment"])


@router.post("")
def sentiment_post(
    request: SentimentRequest,
    sentiment_analyzer: Annotated[SentimentAnalyzer, Depends(sentiment_analyzer)],
) -> SentimentResponse:
    sentiment = sentiment_analyzer.analyze(request.text)
    return SentimentResponse.from_sentiment(sentiment)
