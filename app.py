from flask import Flask, render_template

# Create a Flask web application
app = Flask(__name__)

@app.route('/') # This defines the route that the app will be hosted on, i.e. the root URL

# Sample view function that demonstrates Flask capabilities
def hello_world():
    message = "Hello, world!"
    return render_template('index.html', message = message) # render_template is the Flask method for rendering HTML. Flask handles all the pesky escaping using Jinja2.

# Run the web application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)