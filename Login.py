from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# User credentials
USERNAME = "student"  # Replace with your username
PASSWORD = "Password123"  # Replace with your password

# Setup WebDriver
driver = webdriver.Chrome()  # Use appropriate WebDriver (e.g., Firefox, Edge)
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

username_field = driver.find_element(By.ID, "username")  # Input field for email/phone
password_field = driver.find_element(By.ID, "password")  # Input field for password
login_button = driver.find_element(By.ID, "submit")  # Login button

username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
login_button.click()

time.sleep(5)