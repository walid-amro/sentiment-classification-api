from typing import Self

from pydantic import BaseModel

from app.core.model import Sentiment


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    label: Sentiment

    @classmethod
    def from_sentiment(cls, sentiment: Sentiment) -> Self:
        return cls(label=sentiment)
