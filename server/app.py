from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/reset")
def reset():
    return {"state": random.choice(["owner", "unknown", "suspicious"])}

@app.post("/step")
def step():
    return {"reward": 10, "done": True}
