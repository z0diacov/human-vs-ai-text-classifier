import pandas as pd
from pandas import DataFrame

from sklearn.pipeline import (
    Pipeline, 
    FeatureUnion
)

from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer

from src.model_impl.mixin import BaseModelMixin

from src.features.text_metrics import TextMetricsTransformer

class WCLModel(BaseModelMixin):
    """Word-Character-LogisticRegression Model"""


    def __init__(self):
        super().__init__()

    def init_model(
        self, 
        model: Pipeline | None = None, 
        word_ngram_range: tuple[int] = (1, 2), 
        word_max_features: int = 20_000, 
        min_df: int = 5,
        max_df: float = 0.9,
        char_ngram_range: tuple[int] = (3, 5), 
        char_max_features: int = 30_000,
        max_iter: int = 1000,
        n_jobs: int = -1,
        random_state: int = 42,
        sparse_threshold: float = 0.3) -> Pipeline | None:
        if model is not None:
            self.model = model
        else:
            word_tfidf = TfidfVectorizer(
                analyzer="word",
                ngram_range=word_ngram_range,
                max_features=word_max_features,
                min_df=min_df,
                max_df=max_df,
                lowercase=True,
            )

            char_tfidf = TfidfVectorizer(
                analyzer="char",
                ngram_range=char_ngram_range,
                max_features=char_max_features,
            )

            preprocessor = ColumnTransformer(
                transformers=[
                    ("word_tfidf", word_tfidf, "text"),
                    ("char_tfidf", char_tfidf, "text")
                ],
                sparse_threshold=sparse_threshold
            )


            logistic_regression = LogisticRegression(
                solver="saga",
                max_iter=max_iter,
                n_jobs=n_jobs,
                class_weight="balanced",
                random_state=random_state
            )

            pipeline = Pipeline(
                steps=[
                    ("features", preprocessor),
                    ("clf", logistic_regression)
                ]
            )

            self.model = pipeline
            
        return self.model