# Google Cloud Environment Setup Guide for Expense Agent

This guide outlines the step-by-step process to set up your Google Cloud Environment, enable the required APIs shown in the **Day 5 Codelabs and RK Tech Edge Walkthrough**, and verify their active status.

---

## 🛠️ Step 1: Install & Initialize Google Cloud SDK
If you haven't installed the Google Cloud SDK, download it from [cloud.google.com/sdk](https://cloud.google.com/sdk).

Open your powershell or terminal and initialize the configuration:
```powershell
gcloud init
```
*Follow the browser prompts to log in using your Google Account.*

---

## 🔑 Step 2: Set Your Active Google Cloud Project
Ensure you are operating within the correct GCP project:
```powershell
gcloud config set project kaggle-ai-agents-499912
```
*(Using your active project ID `kaggle-ai-agents-499912`).*

---

## ⚡ Step 3: Enable the Required APIs
Run the following command to enable all four key APIs required for Google Cloud Agent Runtime, Building, and Observability:

```powershell
gcloud services enable agentregistry.googleapis.com `
                       aiplatform.googleapis.com `
                       cloudbuild.googleapis.com `
                       cloudtrace.googleapis.com
```

### 📋 API Breakdown:
*   **`agentregistry.googleapis.com` (Agent Registry API):** Registers and manages metadata for your deployed agents.
*   **`aiplatform.googleapis.com` (Agent Platform API):** Exposes Vertex AI infrastructure to power your agent loops.
*   **`cloudbuild.googleapis.com` (Cloud Build API):** Automates containerizing and building agent code.
*   **`cloudtrace.googleapis.com` (Cloud Trace API):** Collects and displays latency and trace telemetry data for debugging.

---

## 🔍 Step 4: Verification Check
To verify that all four APIs are active and operating correctly (matching the verification screen in the walkthrough), run:

```powershell
gcloud services list --enabled --filter="name:(agentregistry.googleapis.com aiplatform.googleapis.com cloudbuild.googleapis.com cloudtrace.googleapis.com)"
```

### Expected Console Output:
```text
NAME                         TITLE
agentregistry.googleapis.com Agent Registry API
aiplatform.googleapis.com    Agent Platform API
cloudbuild.googleapis.com    Cloud Build API
cloudtrace.googleapis.com    Cloud Trace API
```

---

## 📦 Step 5: Ready to Deploy?
Once verified, you are ready to build and submit your containerized agent using:
```powershell
gcloud builds submit --config cloud_deploy_manifest.yaml .
```
