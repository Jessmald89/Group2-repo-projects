from flask import Flask, render_template, request
from cart import Cart
from food import Food
from constant_values import BANANA_PRICE, APPLE_PRICE, ORANGE_PRICE, DISCOUNT, DISCOUNT_CODE

app = Flask(__name__)
user_cart = Cart()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        add_operation = request.form["add_operation"]

        if add_operation == "banana":
            banana = Food("Banana", BANANA_PRICE)
            user_cart.add(banana)
        elif add_operation == "apple":
            apple = Food("Apple", APPLE_PRICE)
            user_cart.add(apple)
        elif add_operation == "orange":
            orange = Food("Orange", ORANGE_PRICE)
            user_cart.add(orange)

        # Check for Discount Code
        discount_code = request.form.get("discount_code")
        if discount_code == DISCOUNT_CODE:
            # Apply a discount if the provided code matches
            user_cart.apply_discount(DISCOUNT)  # e.x. 20% discount

    return render_template("index.html", inventory=user_cart.items, subtotal=user_cart.subtotal)

if __name__ == "__main__":
    app.run(debug=True)
