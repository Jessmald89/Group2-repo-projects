from flask import Flask, render_template, request
from cart import Cart
from food import Food
from constant_values import BANANA_PRICE, APPLE_PRICE, ORANGE_PRICE, DISCOUNT, DISCOUNT_CODE

app = Flask(__name__)   # Instantiates the Flask app
user_cart = Cart()

'''
@app.route("/", methods=["GET", "POST"]) is a python decorator used by Flask to associate a function with a specific URL, which in this case is simply "/". 
This just tells Flask that the function "def index()"" should be executed whenever a user accesses the root url of the app ("/"). 
It also specifies "GET" and "POST" as methods that the route can handle.
'''
@app.route("/", methods=["GET", "POST"])  
def index():

    if request.method == "POST":       # Provides instructions for a form whose method is "POST"
        if "form1_submit" in request.form:
            add_operation = request.form["add_operation"]   # Finds element in html template where name="add_operation"

            if add_operation == "banana":
                banana = Food("Banana", BANANA_PRICE)
                user_cart.add(banana)
            elif add_operation == "apple":
                apple = Food("Apple", APPLE_PRICE)
                user_cart.add(apple)
            elif add_operation == "orange":
                orange = Food("Orange", ORANGE_PRICE)
                user_cart.add(orange)

        elif "form2_submit" in request.form:
            remove_operation = request.form["remove_operation"] # Finds element in html template where name="remove_operation"
            if remove_operation == "banana":
                banana = Food("Banana", BANANA_PRICE)
                user_cart.remove(banana)
            elif remove_operation == "apple":
                apple = Food("Apple", APPLE_PRICE)
                user_cart.remove(apple)
            elif remove_operation == "orange":
                orange = Food("Orange", ORANGE_PRICE)
                user_cart.remove(orange)

        elif "form3_submit" in request.form: #Clears the list and resets the subtotal. Confirms Purchase.
            user_cart.purchase()
            
        elif "form4_submit" in request.form: #Applies a discount code. Updates subtotal into Total.
            discount_code = request.form.get("discount_code")
            if discount_code == DISCOUNT_CODE:
                user_cart.apply_discount(DISCOUNT)

    return render_template("index.html", cart=user_cart, inventory=user_cart.items, subtotal=user_cart.subtotal, total=user_cart.total, purchase_message=user_cart.purchase_message)# Rendering templates is how Flask interfaces with html.

if __name__ == "__main__":
    app.run(debug=True) # Runs app in debug mode, change debug=False for production version (e.g. for the labs most likely?)
