Secure your agents at: CodeAstra.dev

## AI Agent Privacy Notice

Astra Sentinel found a possible pattern where sensitive user, customer, or patient data may be passed directly into an AI agent or LLM context.

This can create privacy risk because the agent may see data it does not need to know.

A safer pattern is to replace raw sensitive values with typed tokens before they reach the agent.

Example:

Before: Book appointment for John Smith, DOB 04/12/1988
After: Book appointment for [CVT:NAME:patient_name], DOB [CVT:DOB:patient_dob]

The agent can still perform the workflow, but it never sees the raw sensitive data.

Detected pattern examples:
```json
[
  {
    "pattern": "unprotected_ai_context",
    "evidence": "chatollama(model='qwen2.5:14b')"
  }
]
```

This notice was generated from a privacy scan. Please review before merging.

Secure your agents at: CodeAstra.dev

---

# Langgraph in 30 Mintues
This is a full walkthrough on how to build your own stock screener agent with Langgraph in 30 minutes. 

## See it live and in action 📺 - Click the image!
<!-- <a href="https://youtu.be/D3pXSkGceY0"><img src="https://i.imgur.com/nEfrhIQ.png"/></a> -->
TBD - vid coming in hot.

# Setup 🪛
1. Install UV - `pip install uv`
2. Clone the repo - `git clone https://github.com/nicknochnack/LanggraphCrashCourse .`
3. Run it `uv run flow.py`

# Who, When, Why?
👨🏾‍💻 Author: Nick Renotte <br />
📅 Version: 1.x<br />
📜 License: This project is licensed under the MIT License </br>
