Feature: Fill questionnaires and finish


  Scenario Outline: Select <answers> for Shares
    When Select one of "<answers>" from Shares
    Then One of the Shares dropdown "<answers>" will be visible

    Examples:
      | answers    |
      | Frequently |
      | Sometimes  |
      | No         |

  Scenario Outline: Select <answers> for Forex
    When Select one of "<answers>" from Forex
    Then One of the Forex dropdown "<answers>" will be visible

    Examples:
      | answers    |
      | Frequently |
      | Sometimes  |
      | No         |

  Scenario Outline: Select <answers> for CDFs
    When Select one of "<answers>" from CDFs
    Then One of the CDFs dropdown "<answers>" will be visible

    Examples:
      | answers    |
      | Frequently |
      | Sometimes  |
      | No         |

  Scenario: Select trading platform
    When Select "MT5" from Trading Platform
    Then Selected "MT5" will be visible



  Scenario Outline:  Select <answers> for Income
    When Select one of "<answers>" from Income
    Then One of the Income dropdown "<answers>" will be visible


    Examples:
      | answers           |
      | Over $100,000     |
      | $50,000 - $99,999 |
      | $15,000 - $49,999 |
      | Less than $15,000 |

  Scenario Outline: Select <answers> from Employment status
    When Select one of "<answers>" from Employment
    Then One of the Employment dropdown "<answers>" will be visible

    Examples:
      | answers       |
      | Employed      |
      | Self Employed |
      | Retired       |
      | Student       |
      | Unemployed    |

  Scenario Outline:  Select <answers> for Savings
    When Select one of "<answers>" from Savings
    Then One of the Savings dropdown "<answers>" will be visible


    Examples:
      | answers           |
      | Over $100,000     |
      | $50,000 - $99,999 |
      | $5,000 - $49,999  |
      | Less than $5,000  |

  Scenario: Success submit - profile created
    When Check read terms
    And Click Finish
    Then Portal account page will open