from dataclasses import (
    dataclass
)

from typing import (
    Protocol,
    Literal
)
from pathlib import Path

import numpy as np
from pandas import DataFrame
from sklearn.pipeline import Pipeline


class ModelNotDefinedError(Exception):
    pass

class ModelPredictionDataclassProtocol(Protocol):
    def __repr__(self) -> str: ...
    
    result: Literal["HUMAN", "AI"]
    probability_human: float
    probability_ai: float


@dataclass(frozen=True)
class ModelPrediction:
    result: Literal["HUMAN", "AI"]
    probability_human: float
    probability_ai: float

    def __repr__(self) -> str:
        return f"Result: {self.result},\nProbability HUMAN: {self.probability_human:.4f},\nProbability AI: {self.probability_ai:.4f}"


class ModelPredictionCounter:
    def __init__(self, probability_ai: float, result_ai_ge: float) -> None:
        self.probability_ai = probability_ai
        self.result_ai_ge = result_ai_ge

    @property
    def prediction(self) -> ModelPredictionDataclassProtocol:
        probability_human = 1.0 - self.probability_ai
        if self.probability_ai >= self.result_ai_ge:
            result = "AI"
        else:
            result = "HUMAN"
        
        return ModelPrediction(
            result=result,
            probability_human=probability_human,
            probability_ai=self.probability_ai
        )
    

class ModelPerformanceProtocol(Protocol):
    accuracy: float
    precision: float
    recall: float
    f1: float
    classification_report: str
    confusion_matrix: np.ndarray

    def __repr__(self) -> str: ...
    
@dataclass(frozen=True)
class ModelPerformance:
    accuracy: float
    precision: float
    recall: float
    f1: float
    classification_report: str
    confusion_matrix: np.ndarray

    def __repr__(self) -> str:
        return (
            "===== MODEL PERFORMANCE =====\n"
            f"Accuracy : {self.accuracy:.4f}\n"
            f"Precision: {self.precision:.4f}\n"
            f"Recall   : {self.recall:.4f}\n"
            f"F1-score : {self.f1:.4f}\n\n"
            "Classification report:\n"
            f"{self.classification_report.strip()}\n\n"
            "Confusion matrix:\n"
            f"{self.confusion_matrix}"
        )


class BaseModel(Protocol):
    def init_model(self, model: Pipeline | None) -> Pipeline: ...
    def train(
        self,
        dataset: Path | DataFrame,
        text_col: str,
        generated_col: str,
        test_size: float,
        random_state: int | None,
        stratify: bool
    ) -> ModelPerformance: ...
    def finetune(self, dataset: Path | DataFrame) -> None: ...
    def load(self, model_path: Path) -> None: ...
    def save(self, path: Path) -> None: ...
    def predict(self, text: str) -> ModelPredictionDataclassProtocol: ...
