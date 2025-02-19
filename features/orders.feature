Feature: Order a Product
  Scenario: Order a product Successfully
    Given I am logged in to SauceDemo
    When I add product to the cart
    And I proceed to checkout
    Then I should see the order confirmation page