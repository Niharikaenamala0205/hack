from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

current_state = {"value": None}

class ActionInput(BaseModel):
    action: str

@app.post("/reset")
def reset():
    state = random.choice(["owner", "unknown", "suspicious"])
    current_state["value"] = state
    return {"state": state}

@app.post("/step")
def step(input: ActionInput):
    state = current_state["value"]

    if state == "owner" and input.action == "allow":
        reward = 15
    elif state == "unknown" and input.action == "alert":
        reward = 10
    elif state == "suspicious" and input.action == "block":
        reward = 20
    else:
        reward = -20

    return {"state": state, "reward": reward, "done": True}
