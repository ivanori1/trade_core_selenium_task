Feature: Attempt to create account

  Scenario: Failed submit - empty placeholders
    Given Go to Tradecore
    When Click Next
    Then Error appears: "THIS FIELD IS REQUIRED"

  Scenario: Wrong password format
    Given Fill all placeholders
    When Add invalid password credentials "12345678"
    And Click Next
    Then Error appears: "PASSWORD MUST BE 6 TO 15 CHARACTERS LONG, CASE SENSITIVE AND CONTAIN BOTH ENGLISH LETTERS AND NUMBERS ONLY"

  Scenario: Used email
    Given Fill all placeholders
    When Add used email credentials "ivan.coric@tradecore.com"
    And Click Next
    Then Error appears: "THIS EMAIL IS ALREADY TAKEN"

  Scenario: Change dial code by typing number
    When Type number "374" to phone
    Then Selected flag is "Armenia"

  Scenario: Change dial code to unknown
    When Type number "9" to phone
    Then Selected flag is "Unknown"

  Scenario: Success submit
    Given Fill all placeholders
    When Click Next
    Then Questionnaire page appears