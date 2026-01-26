import re

class TextMetricConfig:
    SENTENCE_SPLIT_REGEX: re.Pttern = re.compile(r"[.!?]+")


class Config:
    text_metric = TextMetricConfig()

config = Config()

__all__ = [
    "config"
]