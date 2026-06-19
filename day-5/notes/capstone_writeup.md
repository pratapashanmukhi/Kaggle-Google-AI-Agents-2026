# Capstone Project Writeup: Multi-Agent Kaggriculture Simulation & SDD Conformance Suite

This document serves as the official submission writeup for the **Kaggle × Google 5-Day AI Agents Intensive Course (June 2026)** Capstone Project. It details the design, architecture, and testing of my multi-agent system.

*   **GitHub Repository Code:** [github.com/pratapashanmukhi/Kaggle-Google-AI-Agents-2026](https://github.com/pratapashanmukhi/Kaggle-Google-AI-Agents-2026)
*   **Active Directory:** [day-5/code/](https://github.com/pratapashanmukhi/Kaggle-Google-AI-Agents-2026/tree/main/day-5/code)

---

## 🌾 Project Overview & Rationale
Autonomous agent systems are highly non-deterministic and fragile if not structured correctly. For my capstone project, I built **Kaggriculture**—a multi-agent resource coordination and farming simulation. 

The goal was to demonstrate how multiple specialized AI agents can coordinate actions, make decisions based on dynamic environment feeds (like changing weather), manage finite resources, and execute actions under a **Spec-Driven Development (SDD)** architecture.

---

## 🏗️ Multi-Agent Architecture
The system consists of three distinct agents collaborating inside a step-by-step environment simulation:

1.  **WeatherAgent:** Monitors real-time meteorological conditions and generates multi-day forecasts (e.g., predicting impending rain) to optimize planning.
2.  **SupplyAgent:** Acts as a resource auditor, validating seed inventories, water levels, and fertilizer stocks to ensure operational limits are met.
3.  **FarmerAgent (Orchestrator):** The planning brain. It receives the weather forecast and supply metrics, decomposes the tasks, and decides which crop to plant, when to irrigate, and when to harvest.

```
+------------------+       Forecast       +-------------------+
|   WeatherAgent   | -------------------> |    FarmerAgent    |
+------------------+                      |   (Orchestrator)  |
                                          +-------------------+
+------------------+     Inventory                  |
|   SupplyAgent    | ------------------->           | (Action calls)
+------------------+                                v
                                          +-------------------+
                                          |    Simulation     |
                                          |    Environment    |
                                          +-------------------+
```

---

## 🎯 Spec-Driven Quality & Conformance
To ensure reliability, I implemented **Spec-Driven Development (SDD)**:
*   **Gherkin Feature File (`expense_agent_spec.feature`):** Declarative, behavior-driven specifications defining edge cases (e.g., budget limits, valid receipt approvals).
*   **Assertion Test Suite (`test_agent_conformance.py`):** A custom Python `unittest` class asserting that the agent system strictly adheres to Gherkin specs and state rules.

---

## 📊 Simulation Execution Log
When executed, the system runs through a 3-day cycle:

```text
==================================================
      KAGGRICULTURE MULTI-AGENT SIMULATION        
==================================================

[Environment Setup] Day: 1 | Weather: Sunny | Soil Moisture: 40%

[WeatherAgent - Reasoning]
 > Thought: The farm needs to know the weather for the next few days to optimize seed planting. I will check the weather status.
 > Decided Action: get_weather_forecast with parameters {'days': 3}
[Observation] Weather forecast generated: Based on satellite models, Day 1: Sunny (28°C), Day 2: Impending Rain (90% probability), Day 3: Sunny (30°C). Recommendation: Plant water-intensive crops before Day 2.

[SupplyAgent - Reasoning]
 > Thought: The FarmerAgent has requested resource verification. I need to check current warehouse stocks for Seeds, Water, and Fertilizer.
 > Decided Action: check_inventory with parameters {}
[Observation] Supply status check: Current Inventory -> Seeds: 50 units (Wheat & Corn), Water: 120 Liters, Fertilizer: 30kg. Status: Sufficient for immediate planting.

[FarmerAgent - Reasoning]
 > Thought: Weather predicts rain on Day 2. Inventory has sufficient seeds and water. I should coordinate immediate planting of Wheat so it can benefit from natural rain on Day 2.
 > Decided Action: execute_planting with parameters {'crop': 'Wheat', 'quantity': 20}
[Environment Response] Success: 20 units of Wheat planted. Moisture increased to 50%.

--- ADVANCING TO DAY 2 ---
[Environment Update] Weather: Rainy | Soil Moisture: 85% | Crop Status: Wheat (Growing Stage - Fast Growth due to rain)
[Observation] Crops are absorbing natural rainwater. Irrigation system set to standby.

--- ADVANCING TO DAY 3 ---
[Environment Update] Weather: Sunny | Soil Moisture: 60% | Crop Status: Wheat (Mature Stage - Ready for harvest)

[FarmerAgent - Reasoning]
 > Thought: Crops have reached maturity stage on Day 3. Soil moisture is optimal. I will trigger the harvest tool to secure our yield.
 > Decided Action: execute_harvest with parameters {'crop': 'Wheat'}
[Environment Response] Success: Harvested 45 units of Wheat.

==================================================
               SIMULATION COMPLETE                
==================================================
Final Day: 3
Remaining Seeds: 30
Remaining Water: 80 L
Harvested Crop Yield: 45 units
==================================================
```

---

# Capstone Project: Multi-Agent Kaggriculture Simulation & Conformance Suite

This project serves as my submission for the Kaggle × Google 5-Day AI Agents Intensive Course. It demonstrates a complete multi-agent coordination simulation, spec-driven development using Gherkin syntax, and automated conformance testing.

### 🔗 Code Repository
* Code & Specs: https://github.com/pratapashanmukhi/Kaggle-Google-AI-Agents-2026

---

### 🏗️ Agentic Architecture
My system implements a simulated farming ecosystem (Kaggriculture) consisting of three specialized, coordinating agents:
1. **WeatherAgent:** Evaluates and forecasts multi-day weather conditions (predicting rains, sunny intervals, etc.).
2. **SupplyAgent:** Audits resources, verifying seed inventory and water levels before planting.
3. **FarmerAgent (Orchestrator):** Synthesizes weather reports and resource audits to execute crop planning, irrigation schedules, and harvesting steps.

---

### 🎯 Spec-Driven Development & Testing
To ensure reliability and deterministic outcomes in an agentic loop:
* I wrote Gherkin Specifications defining standard operating rules (e.g., budget bounds and tool usage).
* I implemented a Python `unittest` conformance runner to programmatically assert agent behavior against Gherkin criteria.

---

### 📊 Verified Simulation Console Logs
The simulation successfully processes through a complete cycle:
* Day 1: Weather forecast and inventory verification succeed, trigger-planting 20 units of Wheat.
* Day 2: Environment advances; rainwater increases soil moisture; irrigation is set to standby.
* Day 3: Crops reach maturity, and the FarmerAgent triggers the harvest tool.
* Result: Harvested crop yield of 45 units.

## 💡 Key Learnings & Takeaways
1.  **Modular Tool Design:** Using Model Context Protocol (MCP) design principles keeps tools decoupleable from the core reasoning loop.
2.  **State Safety:** Incorporating strict environmental response returns prevents agents from guessing outcomes or falling into infinite action loops.
3.  **Behavior Tests:** Writing programmatic specifications before agent development provides a safety framework for non-deterministic LLM behaviors.
