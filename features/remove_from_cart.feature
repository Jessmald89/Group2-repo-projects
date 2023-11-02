Feature: Removing an object from the store cart

  Scenario: Removing an object from the cart
    Given the user has items in the cart
    When the user removes an object from the cart
    Then the object will be removed from the cart
