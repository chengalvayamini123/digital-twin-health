import random
import time
import requests

URL = "http://localhost:1880/health-data"

while True:
    data = {
        "temperature": round(random.uniform(35, 40), 1),
        "heart_rate": random.randint(60, 120),
        "spo2": random.randint(90, 100),
        "bp": f"{random.randint(110,130)}/{random.randint(70,90)}"
    }

    try:
        requests.post(URL, json=data)
        print("Sent:", data)
    except:
        print("Node-RED not running")

    time.sleep(3)
