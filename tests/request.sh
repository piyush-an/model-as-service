curl -X 'POST' \
  'http://localhost:3003/classify' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "The economic impact of the new policy is significant.",
  "labels": [
    "politics",
    "economy",
    "entertainment",
    "environment"
  ],
  "multi_label": false
}'