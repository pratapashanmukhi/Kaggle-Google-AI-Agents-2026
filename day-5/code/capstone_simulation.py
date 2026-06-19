"""
Kaggle × Google 5-Day AI Agents Intensive (2026)
Capstone Project: Kaggriculture Simulation

This script simulates a multi-agent farming system (Kaggriculture) where autonomous 
agents coordinate to manage crop planting, resource allocation, and harvesting.
It runs a multi-agent loop demonstrating:
1. Act-Observe-Plan cycles
2. Agent-to-agent communication
3. Tool execution (using a simulated Model Context Protocol)
4. State management and environmental updates
"""

import time
import random
import json

class MockLLM:
    """Simulates Gemini 1.5 Pro / Flash reasoning and response generation based on role and context."""
    @staticmethod
    def generate(prompt, role):
        prompt_lower = prompt.lower()
        
        if role == "weather":
            return {
                "Thought": "The farm needs to know the weather for the next few days to optimize seed planting. I will check the weather status.",
                "Action": "get_weather_forecast",
                "Parameters": {"days": 3},
                "Response": "Based on satellite models, Day 1: Sunny (28°C), Day 2: Impending Rain (90% probability), Day 3: Sunny (30°C). Recommendation: Plant water-intensive crops before Day 2."
            }
            
        elif role == "supply":
            return {
                "Thought": "The FarmerAgent has requested resource verification. I need to check current warehouse stocks for Seeds, Water, and Fertilizer.",
                "Action": "check_inventory",
                "Parameters": {},
                "Response": "Current Inventory -> Seeds: 50 units (Wheat & Corn), Water: 120 Liters, Fertilizer: 30kg. Status: Sufficient for immediate planting."
            }
            
        elif role == "farmer":
            if "plan" in prompt_lower or "strategy" in prompt_lower:
                return {
                    "Thought": "Weather predicts rain on Day 2. Inventory has sufficient seeds and water. I should coordinate immediate planting of Wheat so it can benefit from natural rain on Day 2.",
                    "Action": "execute_planting",
                    "Parameters": {"crop": "Wheat", "quantity": 20},
                    "Response": "Planting completed. 20 units of Wheat successfully sown in Sector A. Soil moisture monitored."
                }
            elif "harvest" in prompt_lower or "mature" in prompt_lower:
                return {
                    "Thought": "Crops have reached maturity stage on Day 3. Soil moisture is optimal. I will trigger the harvest tool to secure our yield.",
                    "Action": "execute_harvest",
                    "Parameters": {"crop": "Wheat"},
                    "Response": "Harvest complete. Yield: 45 units of high-grade Wheat. Storage updated."
                }
        
        return {
            "Thought": "Continuing standard operations.",
            "Action": "log_status",
            "Parameters": {},
            "Response": "System operating normally."
        }

class SimulationEnvironment:
    """Tracks the state of the Kaggriculture farming simulation."""
    def __init__(self):
        self.day = 1
        self.weather = "Sunny"
        self.soil_moisture = 40  # Percentage
        self.crop_status = "None"
        self.inventory = {
            "seeds": 50,
            "water": 120,
            "fertilizer": 30,
            "harvested_yield": 0
        }

    def update_environment(self, action, params):
        if action == "execute_planting":
            crop = params.get("crop", "Wheat")
            qty = params.get("quantity", 10)
            self.inventory["seeds"] -= qty
            self.inventory["water"] -= (qty * 2)
            self.crop_status = f"Planted {qty} units of {crop} (Seedling Stage)"
            self.soil_moisture += 10
            return f"Success: {qty} units of {crop} planted. Moisture increased to {self.soil_moisture}%."
        
        elif action == "execute_harvest":
            if "Mature" in self.crop_status:
                self.crop_status = "Harvested"
                self.inventory["harvested_yield"] += 45
                return "Success: Harvested 45 units of Wheat."
            return f"Failure: Crops not ready. Status: {self.crop_status}"
        
        return "Action completed with no state changes."

    def advance_day(self):
        self.day += 1
        if self.day == 2:
            self.weather = "Rainy"
            self.soil_moisture = 85
            if "Planted" in self.crop_status:
                self.crop_status = "Wheat (Growing Stage - Fast Growth due to rain)"
        elif self.day == 3:
            self.weather = "Sunny"
            self.soil_moisture = 60
            if "Growing" in self.crop_status:
                self.crop_status = "Wheat (Mature Stage - Ready for harvest)"
        
        print(f"\n--- ADVANCING TO DAY {self.day} ---")
        print(f"[Environment Update] Weather: {self.weather} | Soil Moisture: {self.soil_moisture}% | Crop Status: {self.crop_status}")

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def reason_and_act(self, prompt):
        print(f"\n[{self.name} - Reasoning]")
        decision = MockLLM.generate(prompt, self.role)
        print(f" > Thought: {decision['Thought']}")
        print(f" > Decided Action: {decision['Action']} with parameters {decision['Parameters']}")
        return decision

def run_simulation():
    print("==================================================")
    print("      KAGGRICULTURE MULTI-AGENT SIMULATION        ")
    print("==================================================")
    
    # Initialize Environment and Agents
    env = SimulationEnvironment()
    weather_agent = Agent("WeatherAgent", "weather")
    supply_agent = Agent("SupplyAgent", "supply")
    farmer_agent = Agent("FarmerAgent", "farmer")
    
    print(f"\n[Environment Setup] Day: {env.day} | Weather: {env.weather} | Soil Moisture: {env.soil_moisture}%")

    # --- DAY 1: PLANNING & PLANTING ---
    # Step 1: Weather Agent forecasts weather
    weather_prompt = f"Forecast weather for the upcoming 3 days. Current moisture: {env.soil_moisture}%."
    weather_action = weather_agent.reason_and_act(weather_prompt)
    forecast = weather_action["Response"]
    print(f"[Observation] Weather forecast generated: {forecast}")

    # Step 2: Farmer Agent coordinates with Supply Agent to check seeds/water
    supply_prompt = "Verify if we have sufficient seeds and water to plant 20 units of Wheat."
    supply_action = supply_agent.reason_and_act(supply_prompt)
    supply_status = supply_action["Response"]
    print(f"[Observation] Supply status check: {supply_status}")

    # Step 3: Farmer Agent plans and executes planting based on weather & supplies
    farmer_prompt = f"Plan crop strategy. Forecast: {forecast}. Supplies: {supply_status}."
    farmer_action = farmer_agent.reason_and_act(farmer_prompt)
    
    # Apply action to environment
    result = env.update_environment(farmer_action["Action"], farmer_action["Parameters"])
    print(f"[Environment Response] {result}")

    # --- DAY 2: ENVIRONMENT GROWTH & RAIN ---
    time.sleep(1)
    env.advance_day()
    print("[Observation] Crops are absorbing natural rainwater. Irrigation system set to standby.")

    # --- DAY 3: MATURITY & HARVEST ---
    time.sleep(1)
    env.advance_day()
    
    # Farmer Agent reasons about harvesting mature crops
    harvest_prompt = f"Current crop status is: {env.crop_status}. Determine if harvest should commence."
    harvest_action = farmer_agent.reason_and_act(harvest_prompt)
    
    # Apply harvest action to environment
    harvest_result = env.update_environment(harvest_action["Action"], harvest_action["Parameters"])
    print(f"[Environment Response] {harvest_result}")

    # Final Report
    print("\n==================================================")
    print("               SIMULATION COMPLETE                ")
    print("==================================================")
    print(f"Final Day: {env.day}")
    print(f"Remaining Seeds: {env.inventory['seeds']}")
    print(f"Remaining Water: {env.inventory['water']} L")
    print(f"Harvested Crop Yield: {env.inventory['harvested_yield']} units")
    print("==================================================")

if __name__ == "__main__":
    run_simulation()
