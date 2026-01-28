from pathlib import Path

from fastapi import APIRouter

from server.schemas.classifier import (
    ClassificationIn, 
    ClassificationOut
)

from src.model_impl.wrapper import ModelWrapper

model = ModelWrapper()
model.load(
    Path("src") / "models" / "wcmsl_more_words_finetuned.pkl"
)

router = APIRouter()

@router.post("/classify")
async def classify_text(payload: ClassificationIn) -> ClassificationOut:
    text = payload.text
    prediction = model.predict(text)

    return ClassificationOut(
        result=prediction.result,
        probability_ai=prediction.probability_ai,
        probability_human=prediction.probability_human
    )
