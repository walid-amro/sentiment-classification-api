from enum import Enum, StrEnum, auto


class Script(Enum):
    MIXED = auto()
    ARABIC = auto()
    LATIN = auto()


class Sentiment(StrEnum):
    POSITIVE = auto()
    NEGATIVE = auto()
    NEUTRAL = auto()
