Feature: User can use buttons and links in order to navigate between webpages

  Scenario: User can navigate to 'Button success' webpage by clicking on button that has ID
    Given I am on the "Simple HTML Elements For Automation - Ultimate QA" page
    When I click on the button using ID
    Then I am on the "Button success - Ultimate QA" page

  Scenario: User can navigate by using all 'Xpath' buttons
    Given I am on the "Simple HTML Elements For Automation - Ultimate QA" page
    And I can identify first Xpath button
    When I click on the first one
    Then I am on the "Button success - Ultimate QA" page