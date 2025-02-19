Feature: User Login
  Scenario:
    Given I am on SauceDemo login page
    When I enter valid credentials
    Then I should be redirected to the products page