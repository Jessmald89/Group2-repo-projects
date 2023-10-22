class Cart(object):
    def __init__(self):
        self.items = []
        self.subtotal = 0.0
        self.discount = 0.0
        self.purchase_message = ""
        self.discount_applied = False 
        self.total = 0.0

    def add(self, item):
        self.purchase_message = ""
        self.items.append(item.name)
        self.subtotal += item.price
        self.update_total()

    def remove(self, item):
        if item.name in self.items:
            self.items.remove(item.name)
            self.subtotal -= item.price
            self.update_total()
        else:
            raise ValueError("Item not in cart")
    
    def update_total(self): # Updates the total when new items are added 
        discounted_total = self.subtotal * (1 - self.discount)
        self.total = round(discounted_total, 2)

    def apply_discount(self, discount_percentage): # Discount function
        if not self.discount_applied:
            if 0 <= discount_percentage <= 1:
                self.discount = discount_percentage
                self.discount_applied = True # Discount can only be applied once
                self.update_total()  # Updates total when discount is applied
            else:
                raise ValueError("Discount percentage must be between 0 and 1.")
        else:
            print("Discount has already been applied.") # Debugging for discount feature

    def calculate_total(self):
        discounted_total = self.subtotal * (1 - self.discount)
        return round(discounted_total, 2)

    def display(self):
        print(f"Your cart: {self.items}")
        print(f"Your subtotal: ${self.subtotal:.2f}")

    def purchase(self):
        self.items.clear()
        self.subtotal = 0.0
        self.discount = 0.0
        self.discount_applied = False # Resets total and discount code
        self.purchase_message = "Thank you for purchasing!"
