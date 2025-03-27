import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://automationplayground.com/crm/login.html")
driver.maximize_window()

# Locate input fields and login button
email_address = driver.find_element(By.NAME, "email-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.CSS_SELECTOR, "#submit-id")

# Enter credentials
email_address.send_keys("onyinyeazunna5@gmail.com")
password.send_keys("Pycharm@92")

# Click the login button
login_button.click()
time.sleep(5)

# Find the "New Customer" button and click it
driver.find_element(By.ID, "new-customer").click()
time.sleep(5)

# Define customer details
email = "onyinyeazunna5@gmail.com"
first_name = "Onyinye"
last_name = "Azunna"
city = "Lagos"

# Fill in the customer information
driver.find_element(By.ID, "EmailAddress").send_keys(email)
driver.find_element(By.ID, "FirstName").send_keys(first_name)
driver.find_element(By.ID, "LastName").send_keys(last_name)
driver.find_element(By.ID, "City").send_keys(city)
time.sleep(3)

# Select Gender - Click "Female" Checkbox
driver.find_element(By.CSS_SELECTOR, "input[name='gender'][value='female']").click()

# Submit the form
driver.find_element(By.CSS_SELECTOR, "button:first-of-type").click()

# Wait for submission process
time.sleep(5)

#verify success message (Success! New customer added.)
driver.find_element(By.ID, "Success")
time.sleep(3)

#sign out
driver.find_element(By.CSS_SELECTOR, "nav a:first-of-type").click()
time.sleep(3)


