import re
from re import Pattern

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')


class TextMetricConfig:
    SENTENCE_SPLIT_REGEX: Pattern = re.compile(r"[.!?]+")
    PUNCTUATION_REGEX: Pattern = re.compile(r"[.,!?;:()\[\]{}\"']")
    EXCLAMATION_REGEX: Pattern = re.compile(r"[!]")
    QUESTION_REGEX: Pattern = re.compile(r"[?]")
    STOP_WORDS: set[str] = set(stopwords.words("english"))

class DatasetAnalyzeConfig:
    MIN_TEXT_LENGTH: int = 300
    MAX_TEXT_LENGTH: int = 350
    AI_GENERATED_DATASET_SIZE: int = 35000
    HUMAN_WRITTEN_DATASET_SIZE: int = 35000

    AI_GENERATED_TEST_DATASET_SIZE: int = 1500
    HUMAN_WRITTEN_TEST_DATASET_SIZE: int = 1500

class Config:
    text_metric: TextMetricConfig = TextMetricConfig()
    dataset_analyze: DatasetAnalyzeConfig = DatasetAnalyzeConfig()

config = Config()

__all__ = [
    "config"
]