import bentoml
from transformers import pipeline
from pydantic import BaseModel, Field
import typing
from typing import List

# https://huggingface.co/MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli
MODEL_NAME = "MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli"


class ClassificationInput(BaseModel):
    text: str = Field(default="The economic impact of the new policy is significant.", description="The text to classify")
    labels: List[str] = Field(default=["politics", "economy", "entertainment", "environment"], description="List of candidate labels")
    multi_label: bool = Field(default=False, description="Whether to allow multiple labels")


@bentoml.service(name="zero_shot_classifier_service") #, resources={"cpu": "2"}, workers=2, traffic={"timeout": 30})
class ZeroShotClassificationService:
    def __init__(self) -> None:
        self.classifier = pipeline(task="zero-shot-classification", model=MODEL_NAME)

    @bentoml.api(input_spec=ClassificationInput)
    async def classify(self, **params: typing.Any) -> dict:
        sequence_to_classify = params["text"]
        candidate_labels = params["labels"]
        multi_label = params["multi_label"]

        with bentoml.monitor("text_classification") as mon:
            mon.log(sequence_to_classify, name="input_text", role="original_text", data_type="text")

            output = self.classifier(sequence_to_classify, candidate_labels, multi_label=multi_label)
            max_index = output["scores"].index(max(output["scores"]))
            max_label = output["labels"][max_index]

            mon.log(max_label, name="classification_label", role="target", data_type="categorical")

            return {"label": output["labels"], "score": output["scores"]}
