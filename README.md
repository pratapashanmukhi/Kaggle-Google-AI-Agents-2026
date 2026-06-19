# Kaggle × Google: 5-Day AI Agents Intensive (2026)

Welcome to my learning journey repository for the **Kaggle × Google 5-Day AI Agents Intensive Course (June 2026)**. This repository documents my exploration, notes, hands-on codelabs, and custom agent implementations developed throughout this program.

The goal of this repository is to demonstrate a production-ready, spec-driven understanding of autonomous AI agents, tool interoperability, context engineering, evaluation, and security—ideal for internships and placement portfolios.

---

## 📋 Course Overview
This intensive course, co-developed by Kaggle and Google, focuses on shifting from simple chatbots to autonomous, tool-enabled AI agents. It details how to design, test, secure, and deploy agentic systems at scale using state-of-the-art architectures and technologies.

| Day | Focus Area | Key Technologies & Concepts |
|---|---|---|
| **[Day 1](./day-1/README.md)** | Introduction to Agents & Vibe Coding | Agentic Taxonomies, Vibe Coding, Agent Ops, Gemini Pro |
| **[Day 2](./day-2/README.md)** | Agent Tools & Interoperability | Model Context Protocol (MCP), Tool Calling, Custom API Integration |
| **[Day 3](./day-3/README.md)** | Agent Skills & Context Engineering | Context Window Management, Memory Architectures, `SKILL.md` Specs |
| **[Day 4](./day-4/README.md)** | Agent Quality, Security & Evaluation | Evals (LLM-as-a-judge), Prompt Guardrails, Sandboxing, Human-in-the-Loop |
| **[Day 5](./day-5/README.md)** | Production Grade Dev & Capstone | Spec-Driven Dev, Observability, Multi-Agent Simulation |

---

## 🗂️ Repository Structure

This repository is structured systematically to separate core learnings, code implementations, and visual execution traces:

```text
kaggle-ai-agents-intensive/
├── README.md                   # Main repository overview (this file)
├── day-1/
│   ├── README.md               # Intro to Agents, Vibe Coding, & Agent Ops
│   ├── code/                   # Codelabs & starter scripts
│   ├── notes/                  # Detailed conceptual study notes
│   └── screenshots/            # Console outputs and execution traces
├── day-2/
│   ├── README.md               # Model Context Protocol (MCP) & Tools
│   ├── code/                   # Custom MCP Server & tool calling scripts
│   ├── notes/                  # MCP protocol specs & design patterns
│   └── screenshots/            # MCP tool discovery & invocation logs
├── day-3/
│   ├── README.md               # Context Engineering & Agent Skills
│   ├── code/                   # Skills definitions and memory store setup
│   ├── notes/                  # Context rot & memory management strategies
│   └── screenshots/            # Context flow & skill matching traces
├── day-4/
│   ├── README.md               # Quality, Security & Evals
│   ├── code/                   # Assertions, eval test cases, & sandboxing scripts
│   ├── notes/                  # Prompt injection mitigation & LLM-as-a-judge
│   └── screenshots/            # Eval reports & security block logs
└── day-5/
    ├── README.md               # Spec-Driven Production & Capstone
    ├── code/                   # Capstone simulation / Multi-agent setup
    ├── notes/                  # Production observability & governance
    └── screenshots/            # Multi-agent simulation logs & completion badge
```

---

## 🛠️ Tech Stack & Key Frameworks
*   **LLMs:** Google Gemini 1.5 Pro / 1.5 Flash (via Vertex AI & Google AI Studio)
*   **Protocol:** Model Context Protocol (MCP) by Anthropic/Google
*   **Frameworks:** Agent Development Kit (ADK), LangChain/LlamaIndex (conceptual)
*   **Observability:** OpenTelemetry, Arize Phoenix / Langfuse (conceptual tracing)
*   **Testing & Evals:** Python `unittest`/`pytest`, custom LLM-as-a-judge prompts

---

## 🚀 Key Takeaways
1.  **Autonomous Agent Architectures:** Transitioned from single-shot prompts to loop-based reasoning (Act-Observe-Plan).
2.  **Tool-Driven Interoperability:** Implemented MCP to decouple agent execution from client applications, creating extensible tool servers.
3.  **Context & Memory Hygiene:** Solved "context rot" by creating sliding window memory and persistent vector search stores.
4.  **Production Evals:** Learned that agents must be evaluated programmatically using programmatic assertions and LLM judges.
5.  **Secure Workflows:** Designed systems with sandboxed code execution environments and strict guardrails to resist prompt injection attacks.

---

## 🎓 Completion
The intensive culminated in a **Capstone Project** simulating a multi-agent ecosystem (representing complex task planning, resource trading, and environment interaction). 

*   *Check out the [Day 5 Capstone Write-up](./day-5/README.md) for details.*
*   *My official course completion badge is located in [day-5/screenshots/](./day-5/screenshots/).*

---
*Created by [Your Name](https://github.com/pratapashanmukhi) as a portfolio highlight for Applied AI & Agentic Software Engineering roles.*
