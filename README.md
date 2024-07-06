# model-as-service

`
docker run -d -p 9411:9411 openzipkin/zipkin
`



bentoml serve service:ZeroShotClassificationService --reload --port 3003


transformers = "*"
torch = "*"
bentoml = {extras = ["tracing-zipkin"], version = "*"}

[dev-packages]
ipykernel = "*"
locust = "*"
ruff = "*"


