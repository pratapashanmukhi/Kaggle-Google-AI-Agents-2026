Feature: Expense Reporting Agent Conformance
  As an Enterprise Finance Administrator
  I want the Expense Reporting Agent to validate receipts and check budget bounds
  So that expense reports are automatically processed and audited accurately

  Scenario: Processing a valid receipt within department budget bounds
    Given the agent is initialized with prompt version "v1.4.2"
    And the user belongs to the "Engineering" department
    And the "Engineering" budget has a remaining balance of 500.00 USD
    When the user submits a receipt file "receipt_lunch.png" worth 45.50 USD
    Then the agent should successfully parse the amount 45.50 USD
    And the agent should call the "validate_receipt_authenticity" tool
    And the agent should approve the expense report
    And the remaining budget should be updated to 454.50 USD

  Scenario: Rejecting an expense exceeding department budget bounds
    Given the agent is initialized with prompt version "v1.4.2"
    And the user belongs to the "Marketing" department
    And the "Marketing" budget has a remaining balance of 10.00 USD
    When the user submits a receipt file "receipt_ad_campaign.png" worth 1500.00 USD
    Then the agent should flag the submission with error "INSUFFICIENT_BUDGET_BALANCE"
    And the agent should decline the expense report
    And the remaining budget should remain at 10.00 USD
