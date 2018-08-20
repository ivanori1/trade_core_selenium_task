Feature: Attempt to create account with invalid credentials

  Scenario: 1. Failed submit - empty placeholders
    Given Go to Tradecore
    When Click Next
    Then Error appears: "THIS FIELD IS REQUIRED"

  Scenario: 2. Wrong password format
    Given Fill all placeholders
    When Add invalid password credentials "12345678"
    And Click Next
    Then Error appears: "PASSWORD MUST BE 6 TO 15 CHARACTERS LONG, CASE SENSITIVE AND CONTAIN BOTH ENGLISH LETTERS AND NUMBERS ONLY"

  Scenario: 3.Wrong email format
    Given Fill all placeholders
    When Add invalid email credentials "ivan.coric"
    Then Error appears: "THIS FIELD IS NOT VALID"
