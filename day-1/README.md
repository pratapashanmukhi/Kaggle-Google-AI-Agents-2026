# Day 1: Introduction to Agents & Vibe Coding

## 🎯 Focus & Objective
The first day focused on shifting mindsets from **chatbots (prompt-and-response)** to **autonomous agents (sense-think-act loops)**. We explored how agents reason, plan, and self-correct, and introduced the concept of **"Vibe Coding"**—writing and orchestrating software through natural language interfaces.

---

## 🧠 Key Concepts Learned

### 1. The Agentic Loop (Act-Observe-Plan)
Traditional LLM calls are linear: a user prompts, and the model outputs. Agentic workflows loop continuously:
*   **Plan:** The agent breaks down a complex goal into smaller steps.
*   **Act:** The agent executes an action (e.g., calling a tool, writing code).
*   **Observe:** The agent parses the environment's feedback (e.g., console output, API response).
*   **Re-plan:** If errors occur, the agent self-corrects and adapts its strategy.

### 2. Taxonomy of Agent Capabilities
We defined the components that make an LLM an agent:
*   **Core Model:** The reasoning engine (Gemini 1.5 Pro/Flash).
*   **Planning:** Task decomposition, reflection, and self-correction.
*   **Memory:** Keeping track of past actions and environment state.
*   **Tools:** Capabilities to read and write to the external world.

### 3. Vibe Coding & Agent Ops
*   **Vibe Coding:** Shifting the developer's role from writing syntax to guiding the agent's intent, goals, and rules using declarative specifications.
*   **Agent Ops:** The tooling and infrastructure needed to trace agent decision trees, debug agent loops, and monitor tokens/latency.

---

## 💻 Code & Implementation
In the [`code/`](./code) folder, you will find:
*   `simple_agent.py`: A basic Python implementation of an agent loop utilizing the Gemini API to search a mock file system, handle failures, and self-correct based on error messages.

---

## 📸 Suggested Screenshots to Include
When customizing this repo, upload the following screenshots to the `screenshots/` directory:
1.  **`agent_reasoning_trace.png`**: A screenshot of your Kaggle notebook or terminal showing the agent's step-by-step reasoning steps (e.g., "Thought:", "Action:", "Observation:").
2.  **`vibe_coding_prompt.png`**: An image showing your prompt structure where you defined constraints and watched the agent generate code autonomously.

---
*Next: [Day 2: Agent Tools & Interoperability](../day-2/README.md)*
