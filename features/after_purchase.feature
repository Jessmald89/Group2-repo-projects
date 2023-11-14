Feature: Cart Purchase Feature

  Scenario: User purchases items from the cart
    Given items found in cart
    When the user clicks the "Purchase" button
    Then the cart should be empty after the purchase
