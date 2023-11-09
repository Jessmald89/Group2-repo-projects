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

BDD Lab F/U: 10/26/23, 11/2/23

API Tests Lab F/U: 11/9/23

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


