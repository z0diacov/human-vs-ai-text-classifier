import math
import re
from collections import Counter
from dataclasses import (
    dataclass,
    fields
)

from typing import (
    Protocol,
    TypeVar,
    Iterator,
    Any
)

import pandas as pd
from tqdm import tqdm

from sklearn.base import BaseEstimator, TransformerMixin

from src.config.config import config


class TextMetricProtocol(Protocol):
    def __iter__(self) -> Iterator[tuple[str, Any]]: ...
    def __repr__(self): ...

@dataclass(frozen=True)
class AllTextMetrics:
    word_count: int
    text_length: int
    sentence_count: int

    avg_sentence_length: float
    avg_word_length: float

    vocab_size: int
    vocab_richness: float
    repetition_ratio: float

    punctuation_ratio: float
    exclamation_ratio: float
    question_ratio: float
    uppercase_word_ratio: float

    entropy: float

    stopwords_ratio: float

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        for f in fields(self):
            yield f.name, getattr(self, f.name)

    def __repr__(self) -> str:
        metrics = vars(self)
        return "\n".join(
            f"{key}: {value:.4f}" if isinstance(value, float) else f"{key}: {value}"
            for key, value in metrics.items()
        )
    

class TextMetricCalculatorProtocol(Protocol):
    def __init__(self, text: str) -> None: ...
    @property
    def all_metrics(self) -> TextMetricProtocol: ...
    @classmethod
    def build_metrics_dataframe(cls, df: pd.DataFrame, *, text_col: str) -> pd.DataFrame: ...


class TextMetricCalculator:


    def __init__(self, text: str) -> None:
        self.text = text.strip()
        self._words = self._tokenize_words(self.text)
        self._sentences = self._text_to_sentences(self.text)

    def _tokenize_words(self, text: str) -> list[str]:
        return re.findall(r"\b\w+\b", text.lower())

    def _text_to_sentences(self, text: str) -> list[str]:
        sentences = config.text_metric.SENTENCE_SPLIT_REGEX.split(text)
        return [s for s in sentences if s.strip()]

    # Basic metrics

    @property
    def word_count(self) -> int:
        return len(self._words)

    @property
    def text_length(self) -> int:
        return len(self.text)

    @property
    def sentence_count(self) -> int:
        return max(len(self._sentences), 1)

    # Average metrics

    @property
    def avg_sentence_length(self) -> float:
        return sum(len(word) for word in self._words) / self.word_count

    @property
    def avg_word_length(self) -> float:
        return self.text_length / self.word_count if self.word_count else 0.0

    # Lexical metrics

    @property
    def vocab_size(self) -> int:
        return len(set(self._words))

    @property
    def vocab_richness(self) -> float:
        return self.vocab_size / self.word_count if self.word_count else 0.0

    @property
    def repetition_ratio(self) -> float:
        return 1.0 - self.vocab_richness

    # Punctuation metrics

    def _regex_count_ratio(self, regex) -> float:
        if self.text_length == 0:
            return 0.0
        return len(regex.findall(self.text)) / self.text_length

    @property
    def punctuation_ratio(self) -> float:
        return self._regex_count_ratio(config.text_metric.PUNCTUATION_REGEX)

    @property
    def exclamation_ratio(self) -> float:
        return self._regex_count_ratio(config.text_metric.EXCLAMATION_REGEX)

    @property
    def question_ratio(self) -> float:
        return self._regex_count_ratio(config.text_metric.QUESTION_REGEX)

    @property
    def uppercase_word_ratio(self) -> float:
        if self.word_count == 0:
            return 0.0
        uppercase_words = sum(word.isupper() for word in self._words)
        return uppercase_words / self.word_count

    # Entropy

    @property
    def entropy(self) -> float:
        
        if self.word_count == 0:
            return 0.0

        counts = Counter(self._words)
        entropy = 0.0

        for count in counts.values():
            p = count / self.word_count
            entropy -= p * math.log2(p)

        return entropy


    # Stopwords
    @property
    def stopwords_ratio(self):
        stopword_count = sum(word in config.text_metric.STOP_WORDS for word in self._words)
        return stopword_count / self.word_count
    
    # All metrics

    @property
    def all_metrics(self) -> AllTextMetrics:
        return AllTextMetrics(
            word_count=self.word_count,
            text_length=self.text_length,
            sentence_count=self.sentence_count,
            avg_sentence_length=self.avg_sentence_length,
            avg_word_length=self.avg_word_length,
            vocab_size=self.vocab_size,
            vocab_richness=self.vocab_richness,
            repetition_ratio=self.repetition_ratio,
            punctuation_ratio=self.punctuation_ratio,
            exclamation_ratio=self.exclamation_ratio,
            question_ratio=self.question_ratio,
            uppercase_word_ratio=self.uppercase_word_ratio,
            entropy=self.entropy,
            stopwords_ratio=self.stopwords_ratio
        )

    @classmethod
    def build_metrics_dataframe(
        cls,
        df: pd.DataFrame,
        text_col: str = "text",
    ) -> pd.DataFrame:
        rows = []

        for text in tqdm(
            df[text_col],
            total=len(df),
            desc="Extracting text metrics"
        ):
            calculator = cls(text)
            metrics = calculator.all_metrics
            rows.append(dict(metrics))

        return pd.DataFrame(rows)

class TextMetricsTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        rows = []
        for text in X:
            metrics = TextMetricCalculator(text).all_metrics
            rows.append(dict(metrics))
        return pd.DataFrame(rows)