# Group2-repo-projects
__Project/Team Lead:__ Jessica Maldonado

__Code Developers:__ 

1) Saeed Jamal Haddad

2) Bryan Ramsey

__Document Writers:__
1) Andrew Bader

2) Georgette Crudup

3) Julia McDonald
   
__Testers:__
1) Jose Reyes

2) Jacob Sparks
   
__Schedule:__

Initial Group meeting: 9/28/23 at 7pm

F/U group meeting: 10/01/23 at 6pm

Check-In: Daily

Meetings: 1-2x per week

Sprint 1 Instructor meeting: 10/04/23

Sprint 2 Instructor meeting: 10/24/23 @ 7pm

Sprint 3 Instructor meeting:

Sprint 4 Instructor meeting:

Selenium Lab F/U: 10/15/23

RTM Meeting: 10/22/23

BDD Lab F/U: 10/26/23

API Tests Lab F/U

TDD Lab F/U

Secondary Lab F/U


# Selenium Lab
__Introduction__

Selenium is an extremely popular testing tool for web UI testing. Selenium is free & open source, making it a great option for most developers. There are three components offered in the Selenium Suite – WebDriver, IDE, and Grid. This tutorial will focus on WebDriver.

__Getting Started__
1. You will need to install the Selenium bindings for your desired language. Below is how you would use Pip if using Python.

   ```
   pip install selenium
   ```
2. Open your IDE of choice. Import the required packages and start the session with WebDriver (assuming you're using Chrome).

   ```
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   driver = webdriver.Chrome()
   ```
3. Navigate to a webpage of your choice (we're using Wake Tech's for example purposes).

   ```
   driver.get("https://www.waketech.edu/")
   ```
4. Request the title of the webpage.

   ```
   title = driver.title
   ```
5. Print all cookies from the webpage.

   ```
   print(driver.get_cookies())
   ```
6. Quit the session

   ```
   driver.quit()
   ```
# BDD Lab

Behavior Driven Development (BDD) Lab - Behave 

__Introduction__

In software development, Behavior Driven Development is a methodology that promotes collaboration and testing automation among developers and testers. Behavior in the software can be defined as how features operate. BDD is an approach that emphasizes the behaviors of features in the software. There are many BDD frameworks for Python, but this tutorial will focus on using Behave.  

__Getting Started__

1. 	Behave can be installed by executing the following command: 
 
a. pip install behave  

This command can be executed on your local command prompt or through the terminal in Python if that’s the specified programming language being used. It’s optional to install other packages such as Selenium, for web browser interactions. Or the package for requests, for API calls.  These packages are not required but can be useful for testing purposes.  

2. 	Create a directory for the project called “features.” This is where you will store all your feature files. In this same directory, create a file called “fruitstand.feature.” This file will contain the following: 

Feature: Running the Fruit Stand Application 
As a user 
I want to be able to run the Fruit Stand application 
So that I can interact with its features and navigate the application   
Scenario: Launching the Application 
Given I have initiated the application by running the app module in my project 
When I launch the application with the given link provided by the output  
Then I should see the main screen for the Fruit Stand application 

3. 	Create another directory for the project called “features/steps.” In this directory, create a file called “fruitstand.py.” The file will contain the following: 

from behave import * 
@given(‘I have initiated the application by running the app module in my project’) 
def run_the_application() 
# Code to start the application 
pass  
@when(‘I launch the application with the given link provided by the output’) 

# Code to open the application 
def open_the_application(): 
pass 
@then(‘I should see the main screen for the Fruit Stand application’) 
# Code that verifies that the main screen of the application is displayed  
def main_screen_of_application(): 
pass  

4. 	Finally, it’s time to run the tests using Behave. Use the behave command to run all the tests for the project. If you would like to run the scenarios in the feature file, use the command behave features/fruitstand.feature.  

Adding an Item 

Now, we can create more features to test our application. The expected outcome of a user selecting and adding an item to their cart, that the cart will be updated with the change. Let’s test that.  

In your features directory, create a new file named, “additem.feature”. This file will contain the following: 

Feature: Shopping Cart 

Scenario: Adding an item to the cart 

Given a user has selected an item 

When the user adds said item to the cart 

Then the item should appear in the cart 

Now, in the features/steps directory, create a file called add_shopping_cart_steps.py. All following steps should be in that file. 

Import Behave 

From behave import given, when, then 

Let’s write the given step: 

‘@ given (“a user has selected an item”)’ 

def step_select_item(context): 

ADD CODE HERE 

Let’s write the “when” step: 

‘@ when(“the user adds said item to the cart”)  

Def step_add_item(context): 

ADD CODE HERE 

Let’s write the “then” step: 

‘@ then(“the item should appear in the cart”) 

Def step_in_cart(context): 

ADD CODE HERE 

Return TRUE  

Put it all together: 

ADD CODE HERE 

And finally, run in command prompt using the behave command! 
 

 

Removing an Item 

Let’s also make sure that removing an item from your cart works as well. This will be extremely similar to the adding an item test.  

In your features directory, create a new file named, “removeitem.feature”. This file will contain the following: 

Feature: Shopping Cart 

Scenario: Removing an item to the cart 

Given a user has selected an item 

When the user removes said item from the cart 

Then the item should disappear from the cart 

Now, in the features/steps directory, create a file called remove_shopping_cart_steps.py. All following steps should be in that file. 

Import Behave 

From behave import given, when, then 

Let’s write the given step: 

‘@ given (“a user has selected an item”)’ 

def step_select_item(context): 

ADD CODE HERE 

Let’s write the “when” step: 

‘@ when(“the user removes said item from the cart”)  

Def step_remove_item(context): 

ADD CODE HERE 

Let’s write the “then” step: 

‘@ then(“the item should disappear from the cart”) 

Def step_not_in_cart(context): 

ADD CODE HERE 

Return TRUE  

Put it all together: 

ADD CODE HERE 

And finally, run in command prompt using the behave command! 
 
 

