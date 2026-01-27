from .base import ModelWrapperProtocol

from .mixin import BaseModelMixin

class ModelWrapper(BaseModelMixin):
    """Only for loading and prediction"""

    def __init__(self) -> None:
        super().__init__()
    
    def save(self, *args, **kwargs) -> None:
        raise RuntimeError(
            "ModelWrapper is inference-only: saving is disabled"
        )

    def train(self, *args, **kwargs) -> None:
        raise RuntimeError(
            "ModelWrapper is inference-only: training is disabled"
        )


