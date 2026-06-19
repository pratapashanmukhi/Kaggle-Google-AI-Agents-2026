# Day 4: Agent Quality, Security & Evaluation

## 🎯 Focus & Objective
Day 4 addressed the critical requirements of moving agents from hobby projects to production-grade products: ensuring **reliability (evaluations)** and **safety (security)**. We focused on programmatic evaluation strategies and guardrails to mitigate risks like prompt injections and dangerous tool executions.

---

## 🧠 Key Concepts Learned

### 1. Agent Evaluation (Evals)
Since agent behavior is non-deterministic, traditional unit testing is insufficient. We utilized a multi-layered evaluation strategy:
*   **Assertion-based Testing:** Checking for specific, hardcoded output properties (e.g., "Output must be valid JSON", "Must call the `query_db` tool").
*   **LLM-as-a-judge:** Prompting a separate, highly capable LLM (such as Gemini 1.5 Pro) with a grading rubric to evaluate the agent's reasoning, tone, and accuracy.
*   **Regression Sets:** Running automated test runs over cached inputs to verify that updates to prompts or models do not break existing agent capabilities.

### 2. Security & Vulnerability Mitigation
Autonomous agents can be manipulated if they execute untrusted inputs or write code. We implemented security practices:
*   **Prompt Injection Defense:** Sanitizing user inputs, isolating system instructions, and defining strict system boundaries.
*   **Secure Code Sandboxing:** Executing agent-generated code inside isolated Docker containers or restricted virtual environments to prevent local directory traversal or command execution.
*   **Human-in-the-Loop (HITL):** Implementing approval gates for critical actions (e.g., executing a database write command or making payment API calls).

---

## 💻 Code & Implementation
In the [`code/`](./code) folder, you will find:
*   `eval_suite.py`: An automated test script executing assertion tests and an LLM-as-a-judge prompt to score the agent's outputs.
*   `sandbox_runner.py`: A utility demonstrating how to execute arbitrary agent-generated python scripts inside a safe, subprocess-sandboxed execution environment.
*   `guardrails.py`: A middleware script that inspects user queries for prompt injections and blocks them before hitting the LLM.

---

## 📸 Suggested Screenshots to Include
When customizing this repo, upload the following screenshots to the `screenshots/` directory:
1.  **`eval_results_console.png`**: A screenshot showing your terminal test runner printing passed and failed assertions for your agent.
2.  **`sandbox_block_trace.png`**: An image showcasing the agent attempting to execute a system command (like reading environment files) and getting blocked by the sandbox environment.

---
*Next: [Day 5: Spec-Driven Production & Capstone](../day-5/README.md)*
