# USB Security RL Environment

## Problem
Lost USB devices lead to data theft and unauthorized access.

## Solution
This environment simulates USB usage and trains an agent to detect authorized vs unauthorized users.

## States
- owner
- intruder

## Actions
- allow
- block

## Reward
- Correct decision: positive reward
- Wrong decision: negative reward

## How to Run
python main.py