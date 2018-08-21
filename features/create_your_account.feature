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

  Scenario: Wrong email format
    Given Fill all placeholders
    When Add invalid email credentials "ivan.coric"
    Then Error appears: "THIS FIELD IS NOT VALID"

  Scenario: Select country
    When Choose from country dropdown "Armenia"
    Then Placeholder will change to selected country "Armenia"

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