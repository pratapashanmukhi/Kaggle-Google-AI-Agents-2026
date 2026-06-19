# Day 3: Agent Skills & Context Engineering

## 🎯 Focus & Objective
Day 3 focused on the "brain" of the agent: managing context windows, implementing persistent memory architectures, and bundling capabilities into reusable, self-documenting **"Agent Skills"** using standardized formats like `SKILL.md`.

---

## 🧠 Key Concepts Learned

### 1. Memory Architectures
Agents require memory to handle long-running, multi-turn tasks without losing context or hallucinating:
*   **Short-Term Memory (In-Context):** The active conversation history passed inside the context window.
*   **Long-Term Memory (Semantic/Vector DBs):** Persisting past interactions, rules, and facts in a database (like ChromaDB or pgvector) and retrieving them using embedding similarity search.
*   **Procedural Memory (Agent Skills):** Bundled instruction sets that tell the agent *how* to perform a workflow (e.g., how to debug a unit test).

### 2. Context Window Engineering & Context Rot
*   **Context Rot:** As conversation history grows, noise increases, leading to diluted reasoning, lost instructions (middle-of-the-prompt effect), and high latency/cost.
*   **Pruning & Summarization:** Implementing sliding windows, summaries of older history, and metadata pruning to keep context windows lean and highly relevant.

### 3. Declarative "Agent Skills" (`SKILL.md`)
We explored how to structure specialized tasks into files called `SKILL.md` containing frontmatter metadata and clear markdown instructions. This format allows agents to discover and dynamically load custom instructions at runtime.

```markdown
---
name: database-debugger
description: Guides the agent through analyzing and resolving SQL latency and indexing issues.
---
# Instructions
1. Inspect the slow query logs...
2. Run EXPLAIN ANALYZE...
```

---

## 💻 Code & Implementation
In the [`code/`](./code) folder, you will find:
*   `skills/`: A folder containing custom `.md` skills (e.g., `data_cleansing_skill.md`).
*   `memory_manager.py`: A wrapper using vector-based storage to read and write key learnings across multiple separate conversations.
*   `context_pruner.py`: A Python script that checks token counts and automatically summarizes older dialogue history when reaching limit thresholds.

---

## 📸 Suggested Screenshots to Include
When customizing this repo, upload the following screenshots to the `screenshots/` directory:
1.  **`skill_matching_trace.png`**: A screenshot of the agent output showing it scanning the local skill directory, matching a skill to the user's intent, and importing the instructions.
2.  **`memory_retrieval_log.png`**: A console screenshot demonstrating the agent fetching semantic memory from past runs to answer a new query.

---
*Next: [Day 4: Agent Quality, Security & Evaluation](../day-4/README.md)*
