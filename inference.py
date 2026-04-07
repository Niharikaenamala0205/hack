from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Empty request body model (IMPORTANT)
class ResetRequest(BaseModel):
    pass

class ActionRequest(BaseModel):
    action: str

current_state = None

# ✅ FIXED RESET (accepts body)
@app.post("/reset")
def reset(req: ResetRequest):
    global current_state
    current_state = random.choice(["owner", "unknown", "suspicious"])
    return {"state": current_state}

# ✅ STEP API
@app.post("/step")
def step(req: ActionRequest):
    global current_state

    action = req.action

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
