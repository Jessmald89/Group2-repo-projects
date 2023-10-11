class Cart(object):
    def __init__(self):
        self.items = []
        self.subtotal = 0.0
        self.discount = 0.0
        self.discount_applied = False 

    def add(self, item):
        self.items.append(item.name)
        self.subtotal += item.price

    def remove(self, item):
        if item.name in self.items:
            self.items.remove(item.name)
            self.subtotal -= item.price
        else:
            raise ValueError(item.name + " not in cart")

    def apply_discount(self, discount_percentage): # Discount function
        if not self.discount_applied:
            if 0 <= discount_percentage <= 1:
                self.discount = discount_percentage
                self.discount_applied = True # Discount can only be applied once
            else:
                raise ValueError("Discount percentage must be between 0 and 1.")
        else:
            print("Discount has already been applied.") #Debugging for discount feature

    def calculate_total(self):
        discounted_total = self.subtotal * (1 - self.discount)
        return round(discounted_total, 2)

    def display(self):
        print(f"Your cart: {self.items}")
        print(f"Your subtotal: ${self.subtotal:.2f}")

    def clear(self):
        self.items.clear()
        self.subtotal = 0.0
        self.discount = 0.0
        self.discount_applied = False # Resets total and discount code
        print("Thank you for purchasing!")
