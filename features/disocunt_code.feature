Feature: Shopping Cart

  Scenario: Applying a discount code to the cart total
    Given the fruit stand application is open and the user has items in their cart
    When the user applies discount code "DISCOUNT20"
    Then the cart total should be updated with a 20% discount
