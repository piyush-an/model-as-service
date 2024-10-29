# model-as-service

`
docker run -d -p 9411:9411 openzipkin/zipkin
`
```bash
# Build Bento
bentoml containerize --opt platform=linux/amd64 zero_shot_classifier_service:latest --backend podman

podman commit 93fde5cacf6f images.paas.redhat.com/pianand/bento_classifier && 

podman tag a3d668345370 images.paas.redhat.com/pianand/bento_classifier
podman push images.paas.redhat.com/pianand/bento_classifier

# Run Bento
bentoml serve service:ZeroShotClassificationService --reload --port 3003


transformers = "*"
torch = "*"
bentoml = {extras = ["tracing-zipkin"], version = "*"}

[dev-packages]
ipykernel = "*"
locust = "*"
ruff = "*"


```