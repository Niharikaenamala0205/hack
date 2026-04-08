import gradio as gr
from fastapi import FastAPI
from env import USBEnv

# 🔹 Create environment
env = USBEnv()

# 🔹 FastAPI (for OpenEnv checks)
api = FastAPI()

# ✅ RESET API
@api.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

# ✅ STEP API
@api.post("/step")
def step(data: dict):
    action = data.get("action")
    next_state, reward, done = env.step(action)
    return {"state": next_state, "reward": reward, "done": done}


# -----------------------------
# 🔹 Gradio UI
# -----------------------------

current_state = None

# Step 1: Generate User
def generate_user():
    global current_state
    current_state = env.reset()
    return f"🔍 User Type: {current_state}"

# Step 2: Take Action
def take_action(action):
    global current_state
    
    if current_state is None:
        return "⚠️ First generate user!"

    if current_state == "owner" and action == "allow":
        reward = 15
        decision = "✅ Correct Decision"
    elif current_state == "unknown" and action == "alert":
        reward = 10
        decision = "✅ Correct Decision"
    elif current_state == "suspicious" and action == "block":
        reward = 20
        decision = "✅ Correct Decision"
    else:
        reward = -20
        decision = "❌ Wrong Decision"

    return f"""
🔍 User Type: {current_state}
⚙️ Action Taken: {action}
🏆 Reward: {reward}
📊 Result: {decision}
"""

# UI
with gr.Blocks() as demo:
    gr.Markdown("# 🔐 AI USB Intrusion Detection System")

    gr.Markdown("### Step 1: Click below to generate user type")
    
    state_output = gr.Textbox(label="User Info")
    generate_btn = gr.Button("Step 1: Generate User Type")

    gr.Markdown("### Step 2: Choose Action and Click Submit")

    action_input = gr.Radio(["allow", "block", "alert"], label="Choose Action")
    submit_btn = gr.Button("Submit Action")

    result_output = gr.Textbox(label="Result")

    generate_btn.click(fn=generate_user, outputs=state_output)
    submit_btn.click(fn=take_action, inputs=action_input, outputs=result_output)

# 🔥 IMPORTANT (Gradio launch)
demo.launch()
