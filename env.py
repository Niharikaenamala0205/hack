import random

class USBEnv:
    def __init__(self):
        self.state = None

    def reset(self):
        self.state = random.choice(["owner", "intruder"])
        return self.state

    def step(self, action):
        reward = 0
        
        if self.state == "owner" and action == "allow":
            reward = 10
        elif self.state == "intruder" and action == "block":
            reward = 15
        else:
            reward = -10

        done = True
        next_state = self.reset()

        return next_state, reward, done