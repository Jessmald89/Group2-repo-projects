from constant_values import BANANA_PRICE, APPLE_PRICE, ORANGE_PRICE

class Cart(object):
    def __init__(self):
        self.item_names = []
        self.subtotal = 0.0
        self.discount = 0.0
        self.purchase_message = ""
        self.discount_applied = False 
        self.total = 0.0

    def add(self, item):
        self.purchase_message = ""
        self.item_names.append(item)
        self.subtotal += item.price
        self.update_total()

    def remove(self, item):
        for i in self.item_names:
            if item.name == i.name:
                self.item_names.remove(i)
                self.subtotal -= item.price
                self.update_total()
                return "Item removed successfully."
            else:
                error_message = "Item not found in the cart!"
                return error_message
        return ""
        
    def sort(self, mode):
        if mode == "asc":
            self.item_names.sort(key=lambda fruit: fruit.price, reverse=False)
        if mode == "desc":
            self.item_names.sort(key=lambda fruit: fruit.price, reverse=True)

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
        print(f"Your cart: {self.item_names}")
        print(f"Your subtotal: ${self.subtotal:.2f}")

    def purchase(self):
        self.item_names.clear()
        self.subtotal = 0.0
        self.discount = 0.0
        self.discount_applied = False # Resets total and discount code
        self.purchase_message = "Thank you for purchasing!"
