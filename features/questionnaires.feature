Feature: Fill questionnaires and finish

  Scenario: Fill Answers for Shares
    When Select one of "Frequently" from Shares
    Then One of the Shares dropdown "Frequently" will be visible

    Scenario: Failed submit - empty placeholders
    When Click Finish
    Then Error appears: "THIS FIELD IS REQUIRED"