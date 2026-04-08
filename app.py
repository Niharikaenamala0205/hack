from fastapi import FastAPI, Request
from env import USBEnv

app = FastAPI()
env = USBEnv()

@app.post("/reset")
async def reset(request: Request):
    state = env.reset()
    return {"state": state}

@app.post("/step")
async def step(request: Request):
    data = await request.json()
    action = data.get("action")

    next_state, reward, done = env.step(action)

    return {
        "state": next_state,
        "reward": reward,
        "done": done
    }
