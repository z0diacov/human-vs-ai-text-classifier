from fastapi import APIRouter

from .classifier import router as classifier_router

api_router = APIRouter()
api_router.include_router(classifier_router, prefix="/api/v1", tags=["classifier"])


__all__ = ["api_router"]