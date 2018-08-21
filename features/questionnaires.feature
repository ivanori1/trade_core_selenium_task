Feature: Fill questionnaires and finish

  Scenario: Failed submit - empty placeholders

    When Click Finish
    Then Error appears: "THIS FIELD IS REQUIRED"

