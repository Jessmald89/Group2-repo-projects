Feature: Adding an object to the cart

  Scenario: Adding an object to the cart
    Given the fruit stand application is available
    When the user adds an object to the cart
    Then the object should be added to the cart
