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
    # # ===== WCMSL =====
    # ModelConfig(
    #     name="wcmsl_base",
    #     model_cls=WCMSLModel,
    #     init_kwargs={}
    # ),
    # ModelConfig(
    #     name="wcmsl_more_words",
    #     model_cls=WCMSLModel,
    #     init_kwargs={"word_max_features": 40_000}
    # ),
    # ModelConfig(
    #     name="wcmsl_more_chars",
    #     model_cls=WCMSLModel,
    #     init_kwargs={"char_max_features": 60_000}
    # ),

    # # ===== WCL =====
    # ModelConfig(
    #     name="wcl_base",
    #     model_cls=WCLModel,
    #     init_kwargs={}
    # ),
    # ModelConfig(
    #     name="wcl_big_ngrams",
    #     model_cls=WCLModel,
    #     init_kwargs={"char_ngram_range": (3, 7)}
    # ),

    # ===== MS =====
    ModelConfig(
        name="ms_base",
        model_cls=MSModel,
        init_kwargs={}
    ),
    ModelConfig(
        name="ms_strong_reg",
        model_cls=MSModel,
        init_kwargs={"max_iter": 2000}
    ),
]
