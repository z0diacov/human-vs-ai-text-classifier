from dataclasses import dataclass
from typing import Type

from src.model_impl.combined_model import WCMSLModel
from src.model_impl.metrics_model import MSModel
from src.model_impl.word_character import WCLModel


@dataclass
class ModelConfig:
    name: str
    model_cls: Type
    init_kwargs: dict


MODEL_CONFIGS = [

    # WCMSL Base
    # Full combined model using word-level TF-IDF, character-level TF-IDF,
    # and numerical stylometric features.
    # Serves as the main reference model.
    ModelConfig(
        name="wcmsl_base",
        model_cls=WCMSLModel,
        init_kwargs={}
    ),

    # WCMSL More Words
    # Increases the capacity of word-level features to capture richer
    # lexical information.
    ModelConfig(
        name="wcmsl_more_words",
        model_cls=WCMSLModel,
        init_kwargs={
            "word_max_features": 40_000
        }
    ),

    # WCMSL More Characters
    # Expands character-level feature space to better capture
    # stylistic and subword patterns.
    ModelConfig(
        name="wcmsl_more_chars",
        model_cls=WCMSLModel,
        init_kwargs={
            "char_max_features": 60_000
        }
    ),

    # WCL Base
    # Text-only baseline combining word-level and character-level TF-IDF
    # without explicit stylometric metrics.
    ModelConfig(
        name="wcl_base",
        model_cls=WCLModel,
        init_kwargs={}
    ),

    # WCL Larger Character N-grams
    # Uses longer character n-grams to emphasize stylistic structure
    # over lexical semantics.
    ModelConfig(
        name="wcl_big_ngrams",
        model_cls=WCLModel,
        init_kwargs={
            "char_ngram_range": (3, 7)
        }
    ),

    # MS Base
    # Metrics-only model based exclusively on numerical stylometric features.
    # Provides an interpretable lower-bound baseline.
    ModelConfig(
        name="ms_base",
        model_cls=MSModel,
        init_kwargs={}
    ),

    # MS Extended Training
    # Same metrics-only model with extended optimization budget
    # to ensure convergence.
    ModelConfig(
        name="ms_strong_reg",
        model_cls=MSModel,
        init_kwargs={
            "max_iter": 2000
        }
    ),
]

