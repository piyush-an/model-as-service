from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

classifier = pipeline("zero-shot-classification", model="MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")

class ClassificationRequest(BaseModel):
    text: str  = Field(default="The economic impact of the new policy is significant.", description="The text to classify")
    labels: List[str] = Field(default=["politics", "economy", "entertainment", "environment"], description="List of candidate labels")
    multi_label: bool = Field(default=False, description="Whether to allow multiple labels")

class ClassificationResponse(BaseModel):
    labels: list[str]
    scores: list[float]

@app.post("/classify", response_model=ClassificationResponse)
async def classify_text(request: ClassificationRequest):
    try:
        result = classifier(request.text, request.labels, multi_label=request.multi_label)
        return ClassificationResponse(labels=result["labels"], scores=result["scores"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# uvicorn main:app --reload --port 8001
