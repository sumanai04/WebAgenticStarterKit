# ⚡ Agentic Web Starter Kit

<p align="center">
  <strong>Build full‑stack apps autonomously with AI agents – at a fraction of the cost.</strong>
  <br>
  <em>Free local models handle file reading. DeepSeek handles reasoning. You keep the tokens.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Agent-Dual_Layer-blueviolet?style=flat" alt="dual agent" />
  <img src="https://img.shields.io/badge/Claude_Code-000?style=flat&logo=anthropic&logoColor=white" alt="Claude Code" />
  <img src="https://img.shields.io/badge/DeepSeek_V4_Pro-4D6FFF?style=flat&logo=deepseek&logoColor=white" alt="DeepSeek" />
  <img src="https://img.shields.io/badge/Ollama_(Gemma)-000000?style=flat&logo=ollama&logoColor=white" alt="Ollama" />
  <img src="https://img.shields.io/badge/Next.js-000000?style=flat&logo=next.js&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Prisma-2D3748?style=flat&logo=prisma&logoColor=white" alt="Prisma" />
  <img src="https://img.shields.io/badge/LiteLLM-FF6C37?style=flat" alt="LiteLLM" />
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT" />
</p>

---

## 📖 Why this exists

Coding agents like **Claude Code** are incredibly powerful – and incredibly expensive.  
When you ask an agent to "find the bug in the auth flow", it often reads **thousands of lines of irrelevant code** just to build context, burning through your API credits at lightning speed.

This starter kit solves the problem with a **Dual‑Agent Proxy Architecture**:

- **Expensive reasoning** (writing code, planning architecture) → **DeepSeek V4 Pro**
- **Cheap scanning** (grep, file reading, documentation lookups) → **free local Gemma 3 4B via Ollama**

A tiny **LiteLLM proxy** sits in the middle, routing each request to the right model – so you get the full intelligence of a coding agent without paying for brute‑force file searches.

> **Typical savings:** 60‑80% fewer billable tokens for large codebase tasks.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Intelligent Routing** | LiteLLM config automatically routes heavy coding to DeepSeek, light reading to local Ollama |
| **Context Gating** | Ultra‑compact `CLAUDE.md` (under 50 lines) prevents the agent from drowning in unnecessary context |
| **Pre‑configured Database** | `docker-compose.yml` for instant local PostgreSQL with persistent storage |
| **Token Protection** | Aggressive `.gitignore` keeps binaries, datasets, and secrets out of the agent’s view |
| **Modern Stack** | Next.js (App Router) + Tailwind CSS + Prisma ORM, ready for production |
| **Security‑first** | All API keys remain in local environment variables – never committed |

---

## 🏗️ Architecture

```mermaid
graph TD
    CLI[You: "Add a user authentication schema"] -->|Claude Code API call| Proxy[LiteLLM Proxy :4000]
    Proxy -->|"File search / Grep"| Ollama["Ollama<br/>Gemma 3 4B (Local, free)"]
    Proxy -->|"Code generation / Reasoning"| DeepSeek["DeepSeek API<br/>V4 Pro (Cloud)"]
    Ollama -->|Result| Proxy
    DeepSeek -->|Result| Proxy
    Proxy -->|Unified response| CLI
```

**How it works in detail:**

1. Claude Code sends *every* model request to `http://localhost:4000` (the LiteLLM proxy)
2. The proxy inspects the task type using the model name hint:
   - `claude-haiku` → local Ollama (cheap reading)
   - `claude-sonnet` → DeepSeek (expensive coding)
3. DeepSeek and Ollama respond via Anthropic‑compatible API formats
4. Claude Code never knows the difference – it just works™

---

## 📂 Project Structure

```
agentic-web-starter/
├── docs/                  # Agent’s knowledge base (Gemma reads on demand)
│   ├── architecture.md    # Next.js + Prisma conventions
│   └── db_schema.md       # DB tables and relationships
├── src/
│   ├── app/               # Next.js App Router pages & API routes
│   └── components/        # React UI components
├── ops/
│   └── docker-compose.yml # PostgreSQL container
├── .env.example           # Safe environment template
├── .gitignore             # Strict exclusions
├── CLAUDE.md              # Global rules for Claude Code
├── litellm_config.yaml    # Proxy routing configuration
└── package.json
```

---

## 🛠️ Prerequisites

- [Node.js & npm](https://nodejs.org/)
- [Docker Desktop](https://www.docker.com/) (for PostgreSQL)
- [Python 3 & pip](https://www.python.org/) (for LiteLLM proxy)
- [Ollama](https://ollama.com/) (local model runtime)
- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code/overview)  
  `npm install -g @anthropic-ai/claude-code`

---

## 🚀 Quick Start

### 1. Clone and install dependencies

```bash
git clone https://github.com/yourusername/agentic-web-starter.git
cd agentic-web-starter
npm install
```

### 2. Set up environment variables

```bash
cp .env.example .env
```

Open `.env` and add your **DeepSeek API key** and a database password.

### 3. Start the database

```bash
cd ops
docker compose up -d
cd ..
```

### 4. Pull the local reader model

```bash
ollama pull gemma3:4b
```

### 5. Launch the AI proxy (Terminal 1)

<details>
<summary><strong>Mac / Linux</strong></summary>

```bash
pip install litellm
export DEEPSEEK_API_KEY="your-api-key-here"
litellm --config litellm_config.yaml --port 4000
```
</details>

<details>
<summary><strong>Windows PowerShell</strong></summary>

```powershell
pip install litellm
$env:DEEPSEEK_API_KEY="your-api-key-here"
litellm --config litellm_config.yaml --port 4000
```
</details>

**Keep this terminal running.**

### 6. Start Claude Code (Terminal 2)

<details>
<summary><strong>Mac / Linux</strong></summary>

```bash
export ANTHROPIC_BASE_URL="http://localhost:4000"
export ANTHROPIC_API_KEY="litellm-dummy-token"
export CLAUDE_CODE_SUBAGENT_MODEL="claude-haiku-4-5-20251001"
claude
```
</details>

<details>
<summary><strong>Windows PowerShell</strong></summary>

```powershell
$env:ANTHROPIC_BASE_URL="http://localhost:4000"
$env:ANTHROPIC_API_KEY="litellm-dummy-token"
$env:CLAUDE_CODE_SUBAGENT_MODEL="claude-haiku-4-5-20251001"
claude
```
</details>

---

## 💻 Usage example

Once the agent is running, try this prompt inside the Claude Code CLI:

> *"Initialize Prisma in the `src` folder, connect it to the PostgreSQL database defined in `.env`, and create a User model with email and password. After that, update `/docs/db_schema.md` with the new schema."*

**What happens behind the scenes:**

1. Claude Code asks the proxy to locate `.env` – routed to **Gemma 3 4B** (free)
2. Claude Code asks the proxy to generate the schema – routed to **DeepSeek V4 Pro**
3. You pay only for the hard part.

---

## ⚠️ Security Warning

- **Never** hardcode API keys in `litellm_config.yaml` or commit your `.env` file.
- The proxy reads `DEEPSEEK_API_KEY` from the environment – keep it there.
- If a live key is accidentally exposed, revoke it immediately in your provider’s dashboard.

---

## 🧯 Troubleshooting

<details>
<summary><strong>LiteLLM says “No models available”</strong></summary>

Make sure the `litellm_config.yaml` points to valid model names and that your `DEEPSEEK_API_KEY` is exported.
</details>

<details>
<summary><strong>Ollama can’t find Gemma 3 4B</strong></summary>

Pull the model first: `ollama pull gemma3:4b`. Check with `ollama list`.
</details>

<details>
<summary><strong>Claude Code ignores the proxy</strong></summary>

Verify that `ANTHROPIC_BASE_URL` is set and points to `http://localhost:4000` **before** launching `claude`.
</details>

---

## 🤝 Contributing

Contributions are welcome!  
If you have ideas to improve the proxy routing, add more examples, or support additional agents, please open an issue or submit a pull request.

---

## ⚖️ License

This project is licensed under the [MIT License](LICENSE) – use it freely, at your own risk.
