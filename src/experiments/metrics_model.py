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

    
class MSModel(BaseModelMixin):
    """Metrics-StandardScaler-LogisticRegression Model"""

    
    def __init__(self):
        super().__init__()

    def init_model(
        self, 
        model: Pipeline | None = None, 
        max_iter: int = 1000,
        n_jobs: int = -1,
        random_state: int = 42
    ) -> Pipeline | None:
        if model is not None:
            self.model = model
        else:
            preprocessor = Pipeline([
                ("metrics", TextMetricsTransformer()),
                ("scaler", StandardScaler())
            ])

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