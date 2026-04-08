import gradio as gr
from fastapi import FastAPI
from pydantic import BaseModel
import random

# -------------------------
# CREATE FASTAPI APP
# -------------------------
app = FastAPI()

current_state = {"value": None}

class ActionInput(BaseModel):
    action: str

# ✅ OpenEnv RESET
@app.post("/reset")
def reset():
    state = random.choice(["owner", "unknown", "suspicious"])
    current_state["value"] = state
    return {"state": state}

# ✅ OpenEnv STEP
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

# -------------------------
# GRADIO UI
# -------------------------
def generate_user():
    state = random.choice(["owner", "unknown", "suspicious"])
    current_state["value"] = state
    return f"User: {state}"

def take_action(action):
    state = current_state["value"]

    if state is None:
        return "⚠️ Generate user first"

    if state == "owner" and action == "allow":
        return "✅ Correct"
    elif state == "unknown" and action == "alert":
        return "✅ Correct"
    elif state == "suspicious" and action == "block":
        return "✅ Correct"
    else:
        return "❌ Wrong"

with gr.Blocks() as demo:
    gr.Markdown("# 🔐 USB Security System")

    state_output = gr.Textbox()
    generate_btn = gr.Button("Generate User")

    action_input = gr.Radio(["allow", "block", "alert"])
    submit_btn = gr.Button("Submit")

    result_output = gr.Textbox()

    generate_btn.click(generate_user, outputs=state_output)
    submit_btn.click(take_action, inputs=action_input, outputs=result_output)

# ✅ MOUNT GRADIO SAFELY
app = gr.mount_gradio_app(app, demo, path="/")
