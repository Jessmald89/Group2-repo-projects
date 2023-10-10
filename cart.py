class Cart(object):
    def __init__(self):
        self.items = []
        self.subtotal = 0.0
        self.discount = 0.0 

    def add(self, item):
        self.items.append(item.name)
        self.subtotal += item.price

    def remove(self, item):
        if item.name in self.items:
            self.items.remove(item.name)
            self.subtotal -= item.price
        else:
            raise ValueError(item.name + " not in cart")
    
    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 1:
            self.discount = discount_percentage
        else: 
            raise ValueError("Discount percentage must be between 0 and 1.")
    
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
        print("Thank you for purchasing!")
