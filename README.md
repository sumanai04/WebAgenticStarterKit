\# ⚡ Agentic Web Starter Kit



<p align="center">

&#x20; <em>A highly optimized, dual-agent starter kit for building full-stack web apps autonomously.</em><br>

&#x20; Stop wasting millions of API tokens on AI file-searching. <strong>Use free local models for reading, and DeepSeek for reasoning.</strong>

</p>



<p align="center">

&#x20; <img src="https://img.shields.io/badge/Claude\_Code-000?style=flat\&logo=anthropic\&logoColor=white" alt="Claude Code">
&#x20; <img src="https://img.shields.io/badge/DeepSeek\_V4\_Pro-4D6FFF?style=flat\&logo=deepseek\&logoColor=white" alt="DeepSeek">
&#x20; <img src="https://img.shields.io/badge/Ollama\_(Gemma)-000000?style=flat\&logo=ollama\&logoColor=white" alt="Ollama">
&#x20; <img src="https://img.shields.io/badge/Next.js-000000?style=flat\&logo=next.js\&logoColor=white" alt="Next.js">
&#x20; <img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat\&logo=postgresql\&logoColor=white" alt="PostgreSQL">
&#x20; <img src="https://img.shields.io/badge/Prisma-2D3748?style=flat\&logo=prisma\&logoColor=white" alt="Prisma">
&#x20; <img src="https://img.shields.io/badge/LiteLLM-FF6C37?style=flat" alt="LiteLLM">
&#x20; <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT">
</p>


\📖 What Is This?



This is a boilerplate template designed specifically to be manipulated by \*\*AI Coding Agents\*\* (like Claude Code). 



By default, agentic CLIs are incredibly expensive. If you ask an agent to "find the bug in the auth flow," it will often read thousands of lines of irrelevant code to build context, burning through your API credits. 



This starter kit solves that using a \*\*Dual-Agent Proxy Architecture\*\*. It uses a local `LiteLLM` traffic cop to intercept the agent's requests:

1\. \*\*The Thinker (Coding \& Logic):\*\* All code generation is routed to \*\*DeepSeek V4 Pro\*\* (via Anthropic-compatible endpoints).

2\. \*\*The Reader (File Searching):\*\* All background tasks (grepping, searching directories, reading docs) are routed to a free, local \*\*Gemma 3 4B\*\* model running on your GPU via Ollama. 



You get the architectural genius of DeepSeek without paying for the brute-force file scanning.



\✨ Features



| Feature | Description |

|---------|-------------|

| \*\*Dual-Agent Routing\*\* | Built-in LiteLLM config routes `claude-sonnet` to DeepSeek and `claude-haiku` to local Ollama. |

| \*\*Progressive Disclosure\*\* | `CLAUDE.md` is optimized under 50 lines to strictly gatekeep the context window. |

| \*\*Pre-configured DB\*\* | Ready-to-go `docker-compose.yml` for instant PostgreSQL provisioning. |

| \*\*Token-Protected\*\* | Aggressive `.gitignore` rules prevent agents from hallucinating on heavy binaries or datasets. |

| \*\*Modern Web Stack\*\* | Designed for Next.js (App Router) + Tailwind CSS + Prisma ORM workflows. |



\---



\🏗️ Architecture Flowchart



```text

You type: "Add a user authentication schema"

&#x20;       │

&#x20;       ▼

┌──────────────────────┐

│ Claude Code CLI      │ (Thinks it's talking to Anthropic)

└───────┬──────────────┘

&#x20;       │

┌───────▼──────────────┐

│ LiteLLM Proxy (:4000)│ (The Traffic Cop)

└───────┬───────┬──────┘

&#x20;       │       │

&#x20;   If Reading  If Coding

&#x20;       │       │

┌───────▼─┐   ┌─▼──────────────────┐

│ Ollama  │   │ DeepSeek API       │

│ Gemma 3 │   │ V4 Pro             │

│ (Local) │   │ (Cloud)            │

└─────────┘   └────────────────────┘



```



\---



\📂 Project Structure



```text

agentic-web-starter/

├── docs/                       # The AI's knowledge base (Gemma reads this on-demand)

│   ├── architecture.md         # Explains Next.js + Prisma stack rules

│   └── db\_schema.md            # PostgreSQL tables and relationships tracking

├── src/                        # The actual web application source code

│   ├── app/                    # Next.js frontend/backend routes

│   └── components/             # React UI components

├── ops/                        # Infrastructure

│   └── docker-compose.yml      # Local PostgreSQL database setup

├── .env.example                # Safe environment variables template

├── .gitignore                  # The ultimate token saver

├── CLAUDE.md                   # Global rules for Claude Code

├── litellm\_config.yaml         # The proxy router configuration

└── package.json                # Node dependencies



```



\---



\🛠️ Prerequisites



Ensure you have the following installed on your machine before starting:



1\. \*\*\[Node.js](https://nodejs.org/) \& npm\*\*

2\. \*\*\[Docker Desktop](https://www.docker.com/)\*\* (for spinning up PostgreSQL)

3\. \*\*\[Python 3](https://www.python.org/) \& pip\*\* (for running the LiteLLM proxy)

4\. \*\*\[Ollama](https://ollama.com/)\*\* (for the local background reader)

5\. \*\*\[Claude Code CLI](https://www.google.com/search?q=https://docs.anthropic.com/en/docs/agents-and-tools/claude-code)\*\* (Install via: `npm install -g @anthropic-ai/claude-code`)



\---



\🚀 Quick Start Guide



Follow these steps exactly to get the dual-agent environment running safely on your machine.



\### 1. Clone \& Install



```bash

git clone \[https://github.com/yourusername/agentic-web-starter.git](https://github.com/yourusername/agentic-web-starter.git)

cd agentic-web-starter

npm install



```



\### 2. Configure API Keys \& Environment Variables



Copy the secure environment template. \*\*Never commit your `.env` file to GitHub.\*\*



```bash

cp .env.example .env



```



Open the newly created `.env` file and add your `DEEPSEEK\_API\_KEY` and your preferred database password.



\### 3. Spin Up the Database



Start the local PostgreSQL container in the background.



```bash

cd ops

docker-compose up -d

cd ..



```



\### 4. Initialize the Free Local Reader (Ollama)



Ensure the required Gemma 3 model is downloaded to your machine. Ollama will manage the GPU memory automatically.



```bash

ollama pull gemma3:4b



```



\### 5. Start the AI Proxy Traffic Cop (Terminal 1)



Install LiteLLM and run it in the background. This server will route the agent's traffic based on the `litellm\_config.yaml` file.



\*\*For Mac/Linux:\*\*



```bash

pip install litellm

export DEEPSEEK\_API\_KEY="your-api-key-here"

litellm --config litellm\_config.yaml --port 4000



```



\*\*For Windows (PowerShell):\*\*



```powershell

pip install litellm

$env:DEEPSEEK\_API\_KEY="your-api-key-here"

litellm --config litellm\_config.yaml --port 4000



```



\*(Keep this terminal open and running!)\*



\### 6. Launch Claude Code (Terminal 2)



Open a new terminal window in the root directory. Point Claude Code to your local LiteLLM proxy and start building.



\*\*For Mac/Linux:\*\*



```bash

export ANTHROPIC\_BASE\_URL="http://localhost:4000"

export ANTHROPIC\_API\_KEY="litellm-dummy-token"

export CLAUDE\_CODE\_SUBAGENT\_MODEL="claude-haiku-4-5-20251001"

claude



```



\*\*For Windows (PowerShell):\*\*



```powershell

$env:ANTHROPIC\_BASE\_URL="http://localhost:4000"

$env:ANTHROPIC\_API\_KEY="litellm-dummy-token"

$env:CLAUDE\_CODE\_SUBAGENT\_MODEL="claude-haiku-4-5-20251001"

claude



```



\---



\## 💻 Usage Example



Once the agent is running in your terminal, simply tell it what to build. Try pasting this into the Claude Code CLI to test the pipeline:



> \*"Initialize Prisma in the `src` folder, connect it to the PostgreSQL database in the `.env` file, and create a User model with an email and password. Once finished, update `/docs/db\_schema.md` with the new structure."\*



\*\*What happens next:\*\*



1\. Claude Code will ask the proxy how to find the `.env` file.

2\. LiteLLM routes the search task to your local \*\*Gemma 3 4B\*\* model (cost: $0).

3\. Once the files are found, LiteLLM routes the complex Prisma schema generation to \*\*DeepSeek V4 Pro\*\*.



\---



\⚠️ Security Warning



\*\*Do not hardcode API keys into `litellm\_config.yaml` or commit your `.env` file.\*\* This template is explicitly designed to use local environment variables to keep your credentials secure. If you accidentally commit a live API key to a public repository, revoke it immediately via your AI provider's dashboard.



\⚖️ License



This project is open-source and provided under the \[MIT License](https://www.google.com/search?q=LICENSE) "as is", without warranty of any kind.



```



```

