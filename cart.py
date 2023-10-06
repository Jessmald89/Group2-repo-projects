class Cart(object):
    def __init__(self):
        self.items = []
        self.subtotal = 0.0

    def add(self, item):
        self.items.append(item.name)
        self.subtotal += item.price

    def remove(self, item):
        if not item in self:
            raise KeyError(str(item) + " not in cart")
        self.items.remove(item.name)
        self.subtotal -= item.price

    def display(self):
        print(f"Your cart: {self.items}")
        print(f"Your subtotal: ${self.subtotal:.2f}")
