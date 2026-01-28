from pandas import DataFrame
import pandas as pd

from pathlib import Path

import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import GridSearchCV

from src.features.text_metrics import TextMetricCalculator

from src.model_impl.base import ModelNotDefinedError
from src.model_impl.base import ModelPredictionDataclassProtocol
from src.model_impl.base import ModelPerformance
from src.model_impl.base import ModelPredictionCounter


class BaseModelMixin:

    
    def __init__(self) -> None:
        self.model = None

    def load(self, model_path: Path) -> None:
        obj = joblib.load(model_path)

        self.model = obj["model"]

    def save(self, path: Path) -> None:
        if self.model is None:
            raise ModelNotDefinedError
        
        joblib.dump({
            "model": self.model
        }, path)

    def predict(self, text: str, result_ai_ge=0.5) -> ModelPredictionDataclassProtocol:
        if self.model is None:
            raise ModelNotDefinedError
        
        style_metrics = vars(TextMetricCalculator(text).all_metrics)
        sample_df = pd.DataFrame(
            [{**{"text": text}, **style_metrics}]
        )

        proba = self.model.predict_proba(sample_df)[0]
        
        probability_ai = proba[1]
        return ModelPredictionCounter(probability_ai, result_ai_ge).prediction

    def train(
        self,
        dataset: Path | DataFrame,
        text_col: str = "text",
        generated_col: str = "generated",
        test_size: float = 0.25,
        random_state: int | None = 42,
        stratify: bool = True
    ) -> ModelPerformance:
        if isinstance(dataset, Path):
            df = pd.read_csv(dataset)
            df = df.dropna(subset=[text_col, generated_col])

            df[generated_col] = df[generated_col].astype(int)
        
        if isinstance(dataset, DataFrame):
            df = dataset
        
        style_df = TextMetricCalculator.build_metrics_dataframe(df, text_col=text_col)

        full_df = pd.concat(
            [
                df[[text_col, generated_col]].reset_index(drop=True),
                style_df.reset_index(drop=True),
            ],
            axis=1,
        )

        X = full_df.drop(columns=[generated_col])
        y = full_df[generated_col]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=random_state,
            stratify=y if stratify else None,
        )

        print("Training the model...")
        self.model.fit(X_train, y_train)
        print("Evaluating the model...")

        y_pred = self.model.predict(X_test)

        return ModelPerformance(
            accuracy=accuracy_score(y_test, y_pred),
            precision=precision_score(y_test, y_pred),
            recall=recall_score(y_test, y_pred),
            f1=f1_score(y_test, y_pred),
            classification_report=classification_report(y_test, y_pred, target_names=["Human", "AI"]),
            confusion_matrix=confusion_matrix(y_test, y_pred),
        )
    
    def finetune(
        self,
        dataset: Path | DataFrame,
        text_col: str = "text",
        generated_col: str = "generated",
        test_size: float = 0.25,
        random_state: int | None = 42,
        stratify: bool = True
    ) -> ModelPerformance:
        if self.model is None:
            raise ModelNotDefinedError

        if isinstance(dataset, Path):
            df = pd.read_csv(dataset)
            df = df.dropna(subset=[text_col, generated_col])

            df[generated_col] = df[generated_col].astype(int)
        
        if isinstance(dataset, DataFrame):
            df = dataset
        
        style_df = TextMetricCalculator.build_metrics_dataframe(df, text_col=text_col)

        full_df = pd.concat(
            [
                df[[text_col, generated_col]].reset_index(drop=True),
                style_df.reset_index(drop=True),
            ],
            axis=1,
        )

        X = full_df.drop(columns=[generated_col])
        y = full_df[generated_col]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=random_state,
            stratify=y if stratify else None,
        )

        print("Fine-tuning the model...")
        self.model.fit(X_train, y_train)
        print("Evaluating the fine-tuned model...")

        y_pred = self.model.predict(X_test)

        return ModelPerformance(
            accuracy=accuracy_score(y_test, y_pred),
            precision=precision_score(y_test, y_pred),
            recall=recall_score(y_test, y_pred),
            f1=f1_score(y_test, y_pred),
            classification_report=classification_report(y_test, y_pred, target_names=["Human", "AI"]),
            confusion_matrix=confusion_matrix(y_test, y_pred),
        )


