Feature: Attempt to create account with invalid credentials

  Scenario: 1. Failed submit - empty placeholders
    Given Go to Tradecore
    When Click Next
    Then This field is required error