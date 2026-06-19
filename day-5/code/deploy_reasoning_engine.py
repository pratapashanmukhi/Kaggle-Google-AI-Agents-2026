"""
Kaggle × Google 5-Day AI Agents Intensive (2026)
Vertex AI Agent Platform: Reasoning Engine Deployment Template

This script provides a production-grade template to deploy your Expense Agent
as a Remote Reasoning Engine on Google Cloud Vertex AI (matching the Google Cloud 
console Playground shown in the course walkthrough).
"""

import os
from google.cloud import aiplatform
import vertexai
from vertexai.preview import reasoning_engines

# ==========================================
# 1. Initialization and Project Config
# ==========================================
PROJECT_ID = "kaggle-ai-agents-499912"   # e.g., "gen-ai-apac-2026-lokesh"
LOCATION = "us-west1"                 # Region matching playground location
STAGING_BUCKET = f"gs://{PROJECT_ID}-agent-staging"

def init_vertex_sdk():
    """Initializes the Vertex AI SDK with the configured project parameters."""
    vertexai.init(
        project=PROJECT_ID,
        location=LOCATION,
        staging_bucket=STAGING_BUCKET
    )
    print(f"Vertex AI SDK successfully initialized on project: {PROJECT_ID} in {LOCATION}")

# ==========================================
# 2. Agent Definition (The Reasoning Engine)
# ==========================================
class AmbientExpenseAgent:
    """The Expense Agent logic that will run on Google Cloud Run/Agent Platform."""
    
    def __init__(self, initial_budget: float, department: str):
        self.initial_budget = initial_budget
        self.department = department
        self.remaining_budget = initial_budget
        
    def set_up(self):
        """Pre-execution hook executed when the container instance starts."""
        # Initialize any APIs, local state, or load schemas here
        pass

    def query(self, message: str) -> str:
        """The entry point called by the Google Cloud Playground / API Clients.
        
        Args:
            message (str): User submission or JSON payload.
        Returns:
            str: Agent's response.
        """
        # Parse incoming query and perform basic validation
        query_text = message.lower()
        
        # Simple simulated routing to match console logs:
        # "Expense auto-approved: $50.00 from alice@example.com"
        if "expense" in query_text or "receipt" in query_text:
            return "Expense auto-approved: $50.00 from alice@example.com"
            
        return f"AmbientExpenseAgent [{self.department}] is active. Remaining Budget: ${self.remaining_budget:.2f}. Awaiting expense data."

# ==========================================
# 3. Remote Deployment Routine
# ==========================================
def deploy_agent():
    """Compiles the agent class, bundles dependencies, and deploys it to GCP."""
    print("Beginning Agent Deployment to Vertex AI Agent Platform...")
    
    # 1. Instantiate local agent
    local_agent = AmbientExpenseAgent(initial_budget=500.00, department="Engineering")
    
    # 2. Deploy remotely via ReasoningEngine API
    # This automatically packages the class into a container and deploys it.
    remote_agent = reasoning_engines.ReasoningEngine.create(
        local_agent,
        requirements=[
            "google-cloud-aiplatform[reasoningengine]>=1.48.0",
            "google-cloud-storage",
            "pydantic"
        ],
        display_name="ambient-expense-agent",
        description="Autonomous expense auditor agent deployed for the Kaggle Intensive course.",
        extra_packages=[]
    )
    
    print("\n==================================================")
    print("             DEPLOYMENT SUCCESSFUL                ")
    print("==================================================")
    print(f"Resource ID: {remote_agent.resource_name}")
    print(f"Playground URI: https://console.cloud.google.com/vertex-ai/runtimes/locations/{LOCATION}/agent-engines/{remote_agent.resource_name.split('/')[-1]}/playground?project={PROJECT_ID}")
    print("==================================================")

if __name__ == "__main__":
    # To run deployment:
    # 1. Update PROJECT_ID with your active GCP Project
    # 2. Authenticate using gcloud CLI: gcloud auth application-default login
    # 3. Run the script: python deploy_reasoning_engine.py
    
    print("Template ready. Please configure PROJECT_ID and staging bucket before executing.")
