from flask import Flask, render_template, request, redirect, url_for
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
    add_message = ""
    # Provides instructions for a form whose method is "POST"
    if request.method == "POST":
        # Adds item to cart
        if "add_submit" in request.form:
            add_operation = request.form["add_operation"]   # Finds element in html template where name="add_operation"

            if add_operation == "Banana":
                Banana = Food("Banana", BANANA_PRICE)
                add_message = user_cart.add(Banana)
            elif add_operation == "Apple":
                Apple = Food("Apple", APPLE_PRICE)
                add_message = user_cart.add(Apple)
            elif add_operation == "Orange":
                Orange = Food("Orange", ORANGE_PRICE)
                add_message = user_cart.add(Orange)

        # Removes item from cart
        elif "remove_submit" in request.form:
            remove_operation = request.form["remove_operation"]
            
            # Check if the cart is not empty before attempting removal
            if remove_operation == "Banana":
                Banana = Food("Banana", BANANA_PRICE)
                remove_message = user_cart.remove(Banana)
            elif remove_operation == "Apple":
                Apple = Food("Apple", APPLE_PRICE)
                remove_message = user_cart.remove(Apple)
            elif remove_operation == "Orange":
                Orange = Food("Orange", ORANGE_PRICE)
                remove_message = user_cart.remove(Orange)

        # Sorts the items in the cart by price in descending order
        elif "sort_submit" in request.form and request.form['sort_submit'] == 'High-to-Low': 
            user_cart.sort("desc")

        # Sorts the items in the cart by price in ascending order
        elif "sort_submit" in request.form and request.form['sort_submit'] == 'Low-to-High': 
            user_cart.sort("asc")

        # Redirects user to cart page
        elif "see_cart" in request.form:
            return redirect(url_for('cart'))
        
        # Displays the quantity of items
        elif "quantity_form" in request.form:
            check_quantity = request.form["check_quantity"]
            
            # Check if the cart is not empty before attempting removal
            if check_quantity == "Banana":
                quantity_message = f"Number of Bananas in stock: {user_cart.quantity['Banana']}"
            elif check_quantity == "Apple":
                quantity_message = f"Number of Apples in stock: {user_cart.quantity['Apple']}" 
            elif check_quantity == "Orange":
                quantity_message = f"Number of Oranges in stock: {user_cart.quantity['Orange']}" 
    return render_template("index.html", cart=user_cart, item_list=user_cart.items, subtotal=user_cart.subtotal, 
                           total=user_cart.total, purchase_message=user_cart.purchase_message, remove_message=remove_message, add_message = add_message,
                           BANANA_PRICE = BANANA_PRICE, APPLE_PRICE = APPLE_PRICE, ORANGE_PRICE = ORANGE_PRICE, quantity_message = quantity_message)# Rendering templates is how Flask interfaces with html.

@app.route("/cart", methods=["GET", "POST"])
def cart():
    name_message = ""
    if request.method == "POST":
        #Clears the list and resets the subtotal. Confirms Purchase.
        if "purchase_submit" in request.form:
            user_name = request.form.get("user_name") 
            if user_name.isalpha():
                name_message = ""
                user_cart.name = user_name
                return redirect(url_for('receipt'))
            else:
                name_message = "Invalid name. Must contain only letters A-Z."
        
        #Applies a discount code. Updates subtotal into Total.
        elif "discount_submit" in request.form: 
            discount_code = request.form.get("discount_code")
            if discount_code == DISCOUNT_CODE:
                user_cart.apply_discount(DISCOUNT)

        # Sorts the items in the cart by price in descending order
        elif "sort_submit" in request.form and request.form['sort_submit'] == 'High-to-Low': 
            user_cart.sort("desc")

        # Sorts the items in the cart by price in ascending order
        elif "sort_submit" in request.form and request.form['sort_submit'] == 'Low-to-High': 
            user_cart.sort("asc")

        elif "return_home" in request.form:
            return redirect(url_for('index'))

    return render_template("cart.html", cart=user_cart, item_list=user_cart.items, subtotal=user_cart.subtotal, total=user_cart.total, purchase_message=user_cart.purchase_message,
                           name_message=name_message, BANANA_PRICE = BANANA_PRICE, APPLE_PRICE = APPLE_PRICE, ORANGE_PRICE = ORANGE_PRICE)

@app.route("/receipt", methods=["GET", "POST"])
def receipt():
    if request.method == "POST":
        if "submit" in request.form:
            user_cart.purchase()
            user_cart.purchase_message = ""
            return redirect(url_for('index'))

    return render_template("receipt.html", cart=user_cart, item_list=user_cart.items, subtotal=user_cart.subtotal, total=user_cart.total,
                            name = user_cart.name, BANANA_PRICE = BANANA_PRICE, APPLE_PRICE = APPLE_PRICE, ORANGE_PRICE = ORANGE_PRICE)



if __name__ == "__main__":
    app.run(debug=True) # Runs app in debug mode, change debug=False for production version
