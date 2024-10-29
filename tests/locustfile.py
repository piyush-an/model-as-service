import os
import random
from locust import HttpUser, between, task

# Sample sentences and labels
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
    Load test client for Locust.
    """

    @task
    def classify(self):
        text = random.choice(SAMPLE_SENTENCES)
        self.client.post("/classify", json={"text": text, "labels": LABELS})

    wait_time = between(0.01, 2)

# Determine which API to test against based on an environment variable
# API_HOST = os.getenv("API_HOST", "http://fastapi_classifier:8000")

# class MultiApiUser(HttpUser):
#     """
#     Load test for multiple APIs.
#     """
    
#     @task
#     def classify(self):
#         text = random.choice(SAMPLE_SENTENCES)
#         self.client.post(f"{API_HOST}/classify", json={"text": text, "labels": LABELS})

#     wait_time = between(0.01, 2)
