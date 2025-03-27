# Selenium_test2
Automated Customer Form Submission Using Selenium

## Overview
This project automates the process of logging into a CRM system, adding a new customer, and signing out using **Selenium WebDriver** in Python. It interacts with web elements such as input fields, buttons, and checkboxes on `automationplayground.com`.

## Prerequisites
create a requirement.txt file
move all installed packages to the requirement.txt file
-from your terminal,type pip freeze
all packages installed will be displayed on your terminal
-type pip freeze > requirements.txt, click enter.
Before running the script, ensure you have the following installed:

- **Python 3.x**
- **Google Chrome Browser**
- **Chromedriver** 
- **Selenium WebDriver**

### Install Selenium
Run the following command to install Selenium:
pip install selenium

## How the Code Works

### 1. **Initialize WebDriver**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://automationplayground.com/crm/login.html")
driver.maximize_window()
```
- Opens Chrome and navigates to the CRM login page.
- Maximizes the browser window for better visibility.

### 2. **Login Process**
```python
email_address = driver.find_element(By.NAME, "email-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.CSS_SELECTOR, "#submit-id")

email_address.send_keys("onyinyeazunna5@gmail.com")
password.send_keys("Pycharm@92")
login_button.click()
time.sleep(5)

- Locate and fill in the email and password fields.
- Click the login button to access the system.

### 3. **Navigate to 'New Customer' Page**
```python
driver.find_element(By.ID, "new-customer").click()
time.sleep(5)
```
- Clicks the **New Customer** button after logging in.

### 4. **Fill Customer Details**
```python
email = "onyinyeazunna5@gmail.com"
first_name = "Onyinye"
last_name = "Azunna"
city = "Lagos"

driver.find_element(By.ID, "EmailAddress").send_keys(email)
driver.find_element(By.ID, "FirstName").send_keys(first_name)
driver.find_element(By.ID, "LastName").send_keys(last_name)
driver.find_element(By.ID, "City").send_keys(city)
time.sleep(3)
```
- Enters customer details into the required fields.

### 5. **Select Gender**
```python
driver.find_element(By.CSS_SELECTOR, "input[name='gender'][value='female']").click()
```
- Clicks on the **Female** checkbox.

### 6. **Submit the Form**
```python
driver.find_element(By.CSS_SELECTOR, "button:first-of-type").click()
time.sleep(5)
```
- Submits the form and waits for processing.

### 7. **Verify Success Message**
```python
driver.find_element(By.ID, "Success")
time.sleep(3)
```
- Confirms that the success message appears after submission.

### 8. **Sign Out**
```python
driver.find_element(By.CSS_SELECTOR, "nav a:first-of-type").click()
time.sleep(3)
```
- Clicks on the first navigation link to **sign out**.

## Running the Script
1. Ensure **Chromedriver** is correctly installed and in your system PATH.
2. Run the script using:
```bash
python script_name.py
```
3. The script will automate the login, customer entry, and sign out processes.

## Notes
- The script includes `time.sleep()` to allow elements to load before interacting.
- Ensure the website structure remains unchanged; otherwise, update the CSS selectors accordingly.
- If elements are not found, check for dynamic loading and replace with `WebDriverWait` if needed.

## Author
Onyinye Azunna  
Email: onyinyeazunna5@gmail.com  

Happy Coding! 🚀

