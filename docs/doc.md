author: Piyush
summary: Build
id: bentoml-codelab-userdocument
categories: bentoml, ml
environments: Web
status: Draft
feedback link: https://github.com/piyush-an/model-as-service

# Building a ML Service

## Introduction
Duration: 0:02:00

This is a short introduction to building a service for a ml model

## Tradional way
Duration: 0:02:00

building a api server using `FastAPI` or `Flask`

```python
import FastAPI

app = FastAPI()


def classify(input_text: str, input_labels: list) -> dict:
    classify = call_model(input_text, input_labels)

    return { "classify" : classify, "score" : classify.score()}
```