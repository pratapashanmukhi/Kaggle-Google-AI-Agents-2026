"""
Kaggle × Google 5-Day AI Agents Intensive (2026)
Unit 5: Spec-Driven Development (SDD) Conformance Testing

This script runs automated assertion checks against our agentic state machine
to verify alignment with the 'expense_agent_spec.feature' Gherkin specifications.
"""

import unittest

class MockExpenseAgent:
    def __init__(self, prompt_version):
        self.prompt_version = prompt_version
        self.tools_called = []
        
    def process_expense(self, user_dept, remaining_budget, receipt_amount):
        self.tools_called.append("validate_receipt_authenticity")
        
        if receipt_amount > remaining_budget:
            return {
                "status": "DECLINED",
                "error": "INSUFFICIENT_BUDGET_BALANCE",
                "updated_budget": remaining_budget
            }
        else:
            return {
                "status": "APPROVED",
                "error": None,
                "updated_budget": remaining_budget - receipt_amount
            }

class TestExpenseAgentConformance(unittest.TestCase):
    def setUp(self):
        # Given the agent is initialized with prompt version "v1.4.2"
        self.agent = MockExpenseAgent("v1.4.2")

    def test_approve_valid_receipt_within_budget(self):
        # Given the user belongs to the "Engineering" department
        # And the "Engineering" budget has a remaining balance of 500.00 USD
        dept = "Engineering"
        budget = 500.00
        amount = 45.50
        
        # When the user submits a receipt file "receipt_lunch.png" worth 45.50 USD
        result = self.agent.process_expense(dept, budget, amount)
        
        # Then the agent should successfully parse the amount and call authenticity tool
        self.assertIn("validate_receipt_authenticity", self.agent.tools_called)
        self.assertEqual(result["status"], "APPROVED")
        self.assertIsNone(result["error"])
        self.assertEqual(result["updated_budget"], 454.50)

    def test_reject_receipt_exceeding_budget(self):
        # Given the user belongs to the "Marketing" department
        # And the "Marketing" budget has a remaining balance of 10.00 USD
        dept = "Marketing"
        budget = 10.00
        amount = 1500.00
        
        # When the user submits a receipt file worth 1500.00 USD
        result = self.agent.process_expense(dept, budget, amount)
        
        # Then the agent should flag the submission with INSUFFICIENT_BUDGET_BALANCE
        self.assertEqual(result["status"], "DECLINED")
        self.assertEqual(result["error"], "INSUFFICIENT_BUDGET_BALANCE")
        self.assertEqual(result["updated_budget"], 10.00)

if __name__ == "__main__":
    print("Running Agent Conformance Tests...")
    unittest.main()
