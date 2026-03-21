# Lang Graph Projects

A small collection of Python scripts and Jupyter notebooks exploring agent patterns and control flow using LangGraph/LangChain with Google Gemini (via `langchain-google-genai`). It includes a simple chat agent, memory logging, and several graph execution examples (sequential, conditional, looping, and multi-agent).

## Features

- Chat agent script powered by Gemini.
- Memory-enabled agent that logs conversations to a text file.
- LangGraph notebooks showcasing:
  - Simple flow
  - Sequential steps
  - Conditional routing
  - Looping graphs
  - Multiple/parallel agents

## Prerequisites

- Python 3.10+ (Windows, macOS, or Linux)
- A Google Generative AI API key

## Quick Start

1. Create and activate a virtual environment (Windows PowerShell):
   ```powershell
   python -m venv env
   .\env\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Set your API key (Windows PowerShell):
   ```powershell
   $env:GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
   ```
   On macOS/Linux (bash/zsh):
   ```bash
   export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
   ```

## Project Structure

- `Agent_bot.py`: Simple chat agent script using Gemini via LangChain.
- `memory_Agent.py`: Chat agent that persists conversation logs to `conversation_log.txt`.
- `check.py`: Minimal sanity-check/example runner.
- `conversation_log.txt`: Output log file for the memory agent.
- Notebooks:
  - `simple.ipynb`: Minimal LangGraph example.
  - `sequential.ipynb`: Sequential graph execution.
  - `conditional_Agent.ipynb`: Conditional routing within a graph.
  - `loop_graph.ipynb`: Looping/retry patterns.
  - `multiple.ipynb`: Multi-agent or parallel flows.

## Running

- Chat agent:
  ```powershell
  python Agent_bot.py
  ```

- Memory agent (writes to `conversation_log.txt`):
  ```powershell
  python memory_Agent.py
  ```

- Quick check:
  ```powershell
  python check.py
  ```

- Notebooks:
  ```powershell
  pip install jupyter ipykernel
  jupyter notebook
  ```
  Open the desired `.ipynb` and run cells.

## Notes & Troubleshooting

- If you see `NameError: ChatGoogleGenerativeAI is not defined`, install and import the provider:
  ```powershell
  pip install langchain-google-genai
  ```
  ```python
  from langchain_google_genai import ChatGoogleGenerativeAI
  llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
  ```
- Ensure `GOOGLE_API_KEY` is set in your environment before running scripts.
- Some notebooks may require additional packages; install as prompted.

## Resume-Worthy Projects

Below is an honest evaluation of each project in this repository and whether it is strong enough to highlight on a resume.

| Project | Resume-Worthy? | Why |
|---|---|---|
| `React_Agent.py` | ✅ **Yes – Highly recommended** | Demonstrates the full **ReAct (Reason + Act) agent pattern**: tool binding, conditional graph edges, streaming output, and proper agent architecture. This shows real-world AI agent design skills. |
| `memory_Agent.py` | ✅ **Yes** | Shows **multi-turn conversation memory** with a persistent message history and automatic conversation logging. Context-aware agents are a practical and in-demand skill. |
| `Drafter.py` | ✅ **Yes** | Showcases a **document-editing agent with custom tools** (`update`, `save`) and system prompts – a practical example of tool-augmented agents for real-world document workflows. |
| `conditional_Agent.ipynb` | ✅ **Yes** | Demonstrates **conditional routing / branching** within a LangGraph – a core pattern for production agent pipelines. |
| `loop_graph.ipynb` | ✅ **Yes** | Shows **looping / retry patterns** in a graph, useful for self-correcting agents. Worth mentioning as a design pattern. |
| `multiple.ipynb` | ✅ **Yes** | Covers **multi-agent or parallel flows** – one of the more advanced LangGraph features and highly relevant to real projects. |
| `sequential.ipynb` | ⚠️ **Optional** | Simple sequential graph; good for learning but not distinctive enough to stand out on its own. Include it only as part of a broader "LangGraph exploration" description. |
| `Agent_bot.py` | ❌ **No (on its own)** | A very basic stateless chat loop with no memory, no tools, and no branching. Too simple to highlight individually; fold it into a general project description if needed. |
| `simple.ipynb` | ❌ **No (on its own)** | Minimal "hello world" style LangGraph example. Useful for learning but not resume-worthy by itself. |

### TL;DR – What to put on your resume

> **"Built a collection of AI agents using LangGraph and Google Gemini, including a ReAct agent with custom math tools and streaming, a multi-turn memory-enabled conversational agent, a document-drafting agent with tool use, and advanced graph patterns (conditional routing, looping, and multi-agent flows)."**

The three strongest individual projects to call out by name are **`React_Agent.py`**, **`memory_Agent.py`**, and **`Drafter.py`**.

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Google Generative AI](https://ai.google.dev/)
