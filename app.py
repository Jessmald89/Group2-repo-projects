from flask import Flask, render_template, request
from cart import Cart
from food import Food
from constant_values import BANANA_PRICE, APPLE_PRICE, ORANGE_PRICE

app = Flask(__name__)
user_cart = Cart()

# Discount coupon code
DISCOUNT_CODE = "DISCOUNT20"  # e.x. Discount Code

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        operation = request.form["operation"]

        if operation == "banana":
            banana = Food("Banana", BANANA_PRICE)
            user_cart.add(banana)
        elif operation == "apple":
            apple = Food("Apple", APPLE_PRICE)
            user_cart.add(apple)
        elif operation == "orange":
            orange = Food("Orange", ORANGE_PRICE)
            user_cart.add(orange)

        # Check for Discount Code
        discount_code = request.form.get("discount_code")
        if discount_code and discount_code == DISCOUNT_CODE:
            # Apply a discount if the provided code matches
            user_cart.apply_discount(0.20)  # e.x. 20% discount

    return render_template("index.html", inventory=user_cart.items, subtotal=user_cart.subtotal)

if __name__ == "__main__":
    app.run(debug=True)
