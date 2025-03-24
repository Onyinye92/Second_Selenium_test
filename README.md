# Selenium_test2
ANST community Selenium python test2
Project Overview:
This project automates the process of logging into a CRM web application, filling in customer details, submitting the form, and logging out using Selenium WebDriver with Python in PyCharm.

Technologies Used:
Python (Version 3.x)
Selenium WebDriver
PyCharm IDE
ChromeDriver 

Prerequisites:
Before running the script, ensure you have the following installed:
Python 3.x: Download and install from your browser
PyCharm: Install from your browser
Selenium WebDriver: Install using pip:
pip install selenium
ChromeDriver (or the driver for your preferred browser):
Download from ChromeDriver
Ensure it matches your Chrome browser version.
Add it to your system PATH.

Project Setup:
Clone the repository (if applicable):
git clone <repository-url>
cd <project-directory>

Install dependencies:
pip install -r requirements.txt  # If a requirements file exists
Open the project in PyCharm.

Script Workflow

The Selenium script performs the following actions:
Launches the browser and navigates to CRM Login Page.
Enters login credentials (username & password) and submits the form.
Fills in customer details in the form.
Clicks the submit button to save customer details.
Logs out from the CRM application.
Closes the browser.

Running the Script:
Open the Python file in PyCharm.

Run the script using:
python Second_test.py
The automation process will execute, logging into the CRM system, entering customer details, submitting, and logging out.

Expected Output:
The script successfully logs in, fills customer details, submits the form, logs out, and closes the browser.
If an issue occurs (e.g., incorrect login, missing elements), Selenium will raise an error.

Troubleshooting:
Ensure ChromeDriver is correctly installed and matches your Chrome version.
Verify the website is accessible and elements have not changed (inspect elements if necessary).
If running on a different browser, update the WebDriver accordingly.

Future Enhancements:
Implement exception handling for better error management.
Use config files to store login credentials securely.
Add reporting & logging for test results.
Convert script into a pytest framework for structured automation testing.

Author: Onyinye Sarah Azunna

Contact: onyinyeazunna5@gmail.com
