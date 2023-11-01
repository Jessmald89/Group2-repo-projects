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
    remove_message = ""  
    quantity_message = ""
    # Provides instructions for a form whose method is "POST"
    if request.method == "POST":
        # Adds item to cart
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

        # Removes item from cart
        elif "form2_submit" in request.form:
            remove_operation = request.form["remove_operation"]
            
            # Check if the cart is not empty before attempting removal
            if remove_operation == "banana":
                banana = Food("Banana", BANANA_PRICE)
                remove_message = user_cart.remove(banana)
            elif remove_operation == "apple":
                apple = Food("Apple", APPLE_PRICE)
                remove_message = user_cart.remove(apple)
            elif remove_operation == "orange":
                orange = Food("Orange", ORANGE_PRICE)
                remove_message = user_cart.remove(orange)

        #Clears the list and resets the subtotal. Confirms Purchase.
        elif "form3_submit" in request.form: 
            user_cart.purchase()
        
        #Applies a discount code. Updates subtotal into Total.
        elif "form4_submit" in request.form: 
            discount_code = request.form.get("discount_code")
            if discount_code == DISCOUNT_CODE:
                user_cart.apply_discount(DISCOUNT)

        # Sorts the items in the cart by price in descending order
        elif "form5_submit" in request.form and request.form['form5_submit'] == 'High-to-Low': 
            user_cart.sort("desc")

        # Sorts the items in the cart by price in ascending order
        elif "form5_submit" in request.form and request.form['form5_submit'] == 'Low-to-High': 
            user_cart.sort("asc")
        
        # Displays the quantity of items
        elif "form6_submit" in request.form:
            check_quantity = request.form["check_quantity"]
            
            # Check if the cart is not empty before attempting removal
            if check_quantity == "banana":
                quantity_message = f"Number of bananas in stock: {user_cart.quantity['banana']}"
            elif check_quantity == "apple":
                quantity_message = f"Number of apples in stock: {user_cart.quantity['apple']}" 
            elif check_quantity == "orange":
                quantity_message = f"Number of oranges in stock: {user_cart.quantity['orange']}" 
    return render_template("index.html", cart=user_cart, item_list=user_cart.item_names, subtotal=user_cart.subtotal, 
                           total=user_cart.total, purchase_message=user_cart.purchase_message, remove_message=remove_message,
                           BANANA_PRICE = BANANA_PRICE, APPLE_PRICE = APPLE_PRICE, ORANGE_PRICE = ORANGE_PRICE, quantity_message = quantity_message)# Rendering templates is how Flask interfaces with html.

if __name__ == "__main__":
    app.run(debug=True) # Runs app in debug mode, change debug=False for production version
