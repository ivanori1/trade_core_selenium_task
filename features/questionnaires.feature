Feature: Fill questionnaires and finish

  Scenario: Failed submit - empty placeholders
    When Click Finish
    Then Error appears: "THIS FIELD IS REQUIRED"

  Scenario Outline: Fill <answers> for Shares
    When Select one of "<answers>" from Shares
    Then One of the Shares dropdown "<answers>" will be visible

    Examples:
      | answers    |
      | Frequently |
      | Sometimes  |
      | No         |