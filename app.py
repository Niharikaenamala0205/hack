import random
import gradio as gr
from fastapi import FastAPI

# -----------------
# Environment
# -----------------

class USBEnv:
    def __init__(self):
        self.users = ["owner", "unknown", "suspicious"]

    def reset(self):
        return random.choice(self.users)

    def step(self, state, action):
        if state == "owner" and action == "allow":
            return state, 15, True
        elif state == "unknown" and action == "alert":
            return state, 10, True
        elif state == "suspicious" and action == "block":
            return state, 20, True
        else:
            return state, -20, True


env = USBEnv()

# -----------------
# API (FOR SUBMISSION)
# -----------------

api = FastAPI()

current_state = {"value": None}

@api.post("/reset")
def reset():
    current_state["value"] = env.reset()
    return {"state": current_state["value"]}

@api.post("/step")
def step(data: dict):
    action = data.get("action")
    state = current_state["value"]
    state, reward, done = env.step(state, action)
    return {"state": state, "reward": reward, "done": done}


# -----------------
# Gradio UI
# -----------------

def generate_user():
    state = env.reset()
    current_state["value"] = state
    return f"User Type: {state}"

def take_action(action):
    state = current_state["value"]
    if state is None:
        return "Generate user first!"

    state, reward, done = env.step(state, action)
    return f"State: {state} | Reward: {reward}"


demo = gr.Interface(
    fn=take_action,
    inputs=gr.Radio(["allow", "block", "alert"], label="Action"),
    outputs="text",
    title="🔐 USB Security System",
    description="Generate user first, then take action."
)

# Add button manually
with gr.Blocks() as app:
    gr.Markdown("# 🔐 USB Security System")
    btn = gr.Button("Generate User")
    out1 = gr.Textbox(label="User")
    action = gr.Radio(["allow", "block", "alert"])
    btn2 = gr.Button("Submit")
    out2 = gr.Textbox()

    btn.click(generate_user, outputs=out1)
    btn2.click(take_action, inputs=action, outputs=out2)


# 🔥 FINAL RUN FIX
if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=7860)
