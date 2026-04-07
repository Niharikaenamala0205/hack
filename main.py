from env import USBEnv

env = USBEnv()

state = env.reset()
print("Initial State:", state)

action = "allow"  # try allow/block
next_state, reward, done = env.step(action)

print("Next State:", next_state)
print("Reward:", reward)