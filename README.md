---
title: USB Security RL Environment
emoji: 🔐
colorFrom: blue
colorTo: purple
sdk: gradio
app_file: app.py
pinned: false
---

# 🔐 AI USB Intrusion Detection System

## 📌 Problem Statement

USB devices are widely used for data transfer, but they pose serious security risks when lost or accessed by unauthorized users. There is no intelligent system to detect and prevent misuse of such devices.

---

## 💡 Solution

This project introduces an **AI-based USB Security System** that simulates intelligent decision-making using Reinforcement Learning concepts.

The system identifies different types of users and takes appropriate actions to ensure data security.

---

## ⚙️ How It Works

1. The system generates a **User Type**:
   - Owner
   - Unknown
   - Suspicious

2. Based on the user type, the system takes an action:
   - Allow ✅
   - Alert ⚠️
   - Block ❌

3. A reward system evaluates whether the decision is correct.

---

## 🤖 AI Decision Logic

| User Type    | Correct Action | Reward |
|--------------|--------------|--------|
| Owner        | Allow        | +15    |
| Unknown      | Alert        | +10    |
| Suspicious   | Block        | +20    |
| Wrong Action | Any          | -20    |

---

## 🚀 Features

- 🔐 Intelligent USB access control
- 🤖 AI-based decision system
- 🛡️ Unauthorized access prevention
- 📊 Reward-based learning simulation
- 🌐 API-based environment for evaluation

---

## 🔌 API Endpoints

### 1. Reset Environment
