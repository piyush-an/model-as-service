import random
from locust import HttpUser, between, task

# FLAG_MULTI_LABELS = False
LABELS = ["politics", "economy", "entertainment", "environment"]
SAMPLE_SENTENCES = [
    # Politics
    "The new policy reform aims to address the systemic issues in healthcare.",
    "The presidential debate sparked discussions on national security and foreign policy.",
    # Economy
    "The stock market surged as the new economic stimulus package was announced.",
    "Rising inflation rates have significantly impacted the cost of living.",
    # Entertainment
    "The latest blockbuster movie broke all box office records on its opening weekend.",
    "The music festival attracted thousands of fans from across the country.",
    # Environment
    "The government launched a new initiative to combat climate change and reduce carbon emissions.",
    "Conservation efforts have led to a significant increase in the population of endangered species.",
]


class BentoHttpUser(HttpUser):
    """
    Start locust load testing client with:

        locust --class-picker -H http://localhost:3003

    Open browser at http://0.0.0.0:8089, adjust desired number of users and spawn rate for the load test from the Web UI and start swarming.
    """

    @task
    def classify(self):
        text = random.choice(SAMPLE_SENTENCES)
        labels = LABELS
        # multi_label = FLAG_MULTI_LABELS

        self.client.post("/classify", json={"text": text, "labels": labels})

    wait_time = between(0.01, 2)
