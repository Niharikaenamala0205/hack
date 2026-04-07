from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Request model
class ActionRequest(BaseModel):
    action: str

# Global state
current_state = None

# Reset endpoint
@app.post("/reset")
def reset():
    global current_state
    current_state = random.choice(["owner", "unknown", "suspicious"])
    return {"state": current_state}

# Step endpoint
@app.post("/step")
def step(request: ActionRequest):
    global current_state

    action = request.action

    if current_state == "owner" and action == "allow":
        reward = 15
    elif current_state == "unknown" and action == "alert":
        reward = 10
    elif current_state == "suspicious" and action == "block":
        reward = 20
    else:
        reward = -20

    return {
        "state": current_state,
        "action": action,
        "reward": reward
    }
