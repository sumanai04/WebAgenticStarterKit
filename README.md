---
# ⚡ Agentic Web Starter Kit

<p align="center">
  <em>A highly optimized, dual-agent starter kit for building full-stack web apps autonomously.</em><br>
  Stop wasting millions of API tokens on AI file-searching. <strong>Use free local models for reading, and DeepSeek for reasoning.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-000?style=flat&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/DeepSeek_V4_Pro-4D6FFF?style=flat&logo=deepseek&logoColor=white" alt="DeepSeek">
  <img src="https://img.shields.io/badge/Ollama_(Gemma)-000000?style=flat&logo=ollama&logoColor=white" alt="Ollama">
  <img src="https://img.shields.io/badge/Next.js-000000?style=flat&logo=next.js&logoColor=white" alt="Next.js">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/LiteLLM-FF6C37?style=flat" alt="LiteLLM">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT">
</p>

---

## 📖 What Is This?

This is a boilerplate template designed specifically to be manipulated by **AI Coding Agents** (like Claude Code). 

By default, agentic CLIs are incredibly expensive. If you ask an agent to "find the bug in the auth flow," it will often read thousands of lines of irrelevant code to build context, burning through your API credits. 

This starter kit solves that using a **Dual-Agent Proxy Architecture**. It uses a local `LiteLLM` traffic cop to intercept the agent's requests:
1. **The Thinker (Coding & Logic):** All code generation is routed to **DeepSeek V4 Pro** (via Anthropic-compatible endpoints).
2. **The Reader (File Searching):** All background tasks (grepping, searching directories, reading docs) are routed to a free, local **Gemma 3 4B** model running on your GPU via Ollama. 

You get the architectural genius of DeepSeek without paying for the brute-force file scanning.

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Dual-Agent Routing** | Built-in LiteLLM config routes `claude-sonnet` to DeepSeek and `claude-haiku` to local Ollama. |
| **Progressive Disclosure** | `CLAUDE.md` is optimized under 50 lines to strictly gatekeep the context window. |
| **Decoupled Stack** | Next.js (App Router) for the frontend, Python FastAPI + SQLModel for the backend. |
| **Token-Protected** | Aggressive `.gitignore` rules prevent agents from hallucinating on `node_modules` or Python `.venv` folders. |
| **Pre-configured DB** | Ready-to-go `docker-compose.yml` for instant PostgreSQL provisioning. |

---

## 🏗️ Architecture Flowchart

```text
You type: "Add a user authentication schema"
        │
        ▼
┌──────────────────────┐
│ Claude Code CLI      │ (Thinks it's talking to Anthropic)
└───────┬──────────────┘
        │
┌───────▼──────────────┐
│ LiteLLM Proxy (:4000)│ (The Traffic Cop)
└───────┬───────┬──────┘
        │       │
    If Reading  If Coding
        │       │
┌───────▼─┐   ┌─▼──────────────────┐
│ Ollama  │   │ DeepSeek API       │
│ Gemma 3 │   │ V4 Pro             │
│ (Local) │   │ (Cloud)            │
└─────────┘   └────────────────────┘

```

---

## 📂 Project Structure

```text
agentic-web-starter/
├── docs/
│   ├── architecture.md         # Explains the decoupled Next.js/FastAPI stack
│   └── api_specs.md            # The API contract between frontend and backend
├── src/
│   ├── frontend/               # Next.js app (React, Tailwind)
│   │   ├── package.json
│   │   └── ...
│   └── backend/                # FastAPI app (Python, SQLModel, ML pipelines)
│       ├── requirements.txt
│       ├── main.py
│       └── models/             
├── ops/
│   └── docker-compose.yml      # Local PostgreSQL database setup
├── .env.example                # Safe environment variables template
├── .gitignore                  # Token saver (Ignores JS and Python build files)
├── CLAUDE.md                   # Global rules for Claude Code
└── litellm_config.yaml         # The proxy router configuration

```

---

## 🛠️ Prerequisites

Ensure you have the following installed on your machine before starting:

1. **[Node.js](https://nodejs.org/) & npm**
2. **[Python 3.10+](https://www.python.org/) & pip**
3. **[Docker Desktop](https://www.docker.com/)** (for spinning up PostgreSQL)
4. **[Ollama](https://ollama.com/)** (for the local background reader)
5. **[Claude Code CLI](https://www.google.com/search?q=https://docs.anthropic.com/en/docs/agents-and-tools/claude-code)** (Install via: `npm install -g @anthropic-ai/claude-code`)

---

## 🚀 Quick Start Guide

Follow these steps exactly to get the dual-agent environment and split-stack running safely on your machine.

### 1. Clone & Setup Environments

```bash
git clone [https://github.com/yourusername/agentic-web-starter.git](https://github.com/yourusername/agentic-web-starter.git)
cd agentic-web-starter

# Setup Frontend
cd src/frontend
npm install
cd ../..

# Setup Backend (Python Virtual Environment)
cd src/backend
python -m venv .venv
# On Windows: .venv\Scripts\activate
# On Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
cd ../..

```

### 2. Configure API Keys & Environment Variables

Copy the secure environment template. **Never commit your `.env` file to GitHub.**

```bash
cp .env.example .env

```
Open the newly created `.env` file and add your `DEEPSEEK_API_KEY` and your preferred database password.

you could actually skip everything from this point straight to the Claude Setup

### 3. Spin Up the Database

Start the local PostgreSQL container in the background.

```bash
cd ops
docker-compose up -d
cd ..

```

### 4. Initialize the Free Local Reader (Ollama)

Ensure the required Gemma 3 model is downloaded to your machine. Ollama will manage the GPU memory automatically.

```bash
ollama pull gemma3:4b

```

### 5. Start the AI Proxy Traffic Cop (Terminal 1)

Install LiteLLM and run it in the background. This server will route the agent's traffic based on the `litellm_config.yaml` file.

**For Mac/Linux:**

```bash
pip install litellm
export DEEPSEEK_API_KEY="your-api-key-here"
litellm --config litellm_config.yaml --port 4000

```

**For Windows (PowerShell):**

```powershell
pip install litellm
$env:DEEPSEEK_API_KEY="your-api-key-here"
litellm --config litellm_config.yaml --port 4000

```

*(Keep this terminal open and running!)*

### 6. Launch Claude Code (Terminal 2)

Open a new terminal window in the root directory. Point Claude Code to your local LiteLLM proxy and start building.

**For Mac/Linux:**

```bash
export ANTHROPIC_BASE_URL="http://localhost:4000"
export ANTHROPIC_API_KEY="sk-ant-api03-litellmdummykey1234567890"
export CLAUDE_CODE_SUBAGENT_MODEL="claude-haiku-4-5-20251001"
export ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"
claude

```

**For Windows (PowerShell):**

```powershell
$env:ANTHROPIC_BASE_URL="http://localhost:4000"
$env:ANTHROPIC_API_KEY="sk-ant-api03-litellmdummykey1234567890"
$env:CLAUDE_CODE_SUBAGENT_MODEL="claude-haiku-4-5-20251001"
$env:ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"
claude

```

---

## 💻 Usage Example

Because this is a decoupled architecture, you can prompt the AI to build features that span across both languages seamlessly. Try pasting this into the Claude Code CLI:

> *"Create a new FastAPI endpoint in `/src/backend` for uploading medical images for DeepLabV3 segmentation. Then, go to `/src/frontend`, build a Next.js upload form using Tailwind, and connect it to that new Python endpoint. Update `/docs/api_specs.md` with the new route details."*

**What happens next:**

1. Claude Code asks the proxy to read `/docs/api_specs.md`.
2. LiteLLM routes the reading task to your local **Gemma 3 4B** model (cost: $0).
3. Once the context is loaded, LiteLLM routes the Python and React code generation to **DeepSeek V4 Pro**.

---

## ⚠️ Security Warning

**Do not hardcode API keys into `litellm_config.yaml` or commit your `.env` file.** This template is explicitly designed to use local environment variables to keep your credentials secure. If you accidentally commit a live API key to a public repository, revoke it immediately via your AI provider's dashboard.
