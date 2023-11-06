Feature: Shopping Cart

  Scenario: Removing an item not in the cart
    Given the fruit stand application is open and the user has items in the cart
    When the user attempts to remove an incorrect item from the cart
    Then the cart contents should remain the same
