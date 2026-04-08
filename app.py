import gradio as gr
import random

current_state = {"value": None}

def generate_user():
    state = random.choice(["owner", "unknown", "suspicious"])
    current_state["value"] = state
    return f"User: {state}"

def take_action(action):
    state = current_state["value"]

    if state is None:
        return "⚠️ Generate user first"

    if state == "owner" and action == "allow":
        return "✅ Correct (Reward: 15)"
    elif state == "unknown" and action == "alert":
        return "✅ Correct (Reward: 10)"
    elif state == "suspicious" and action == "block":
        return "✅ Correct (Reward: 20)"
    else:
        return "❌ Wrong (Penalty: -20)"

with gr.Blocks() as demo:
    gr.Markdown("# 🔐 USB Security System")

    state_output = gr.Textbox(label="User Info")
    generate_btn = gr.Button("Generate User")

    action_input = gr.Radio(["allow", "block", "alert"], label="Choose Action")
    submit_btn = gr.Button("Submit")

    result_output = gr.Textbox(label="Result")

    generate_btn.click(generate_user, outputs=state_output)
    submit_btn.click(take_action, inputs=action_input, outputs=result_output)

demo.launch()
