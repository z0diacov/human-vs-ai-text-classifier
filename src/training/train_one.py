from pathlib import Path

from src.model_impl.mixin import BaseModelMixin
from src.training.model_configs import ModelConfig


def train_single_model(
    config: ModelConfig,
    dataset_path: Path,
    output_dir: Path,
):
    model: BaseModelMixin = config.model_cls()
    model.init_model(**config.init_kwargs)

    performance = model.train(dataset=dataset_path)

    model_path = output_dir / f"{config.name}.pkl"
    model.save(model_path)

    return {
        "model": config.name,
        "metrics": performance,
        "path": str(model_path),
    }
