from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import random
import json
import time

# Load email configuration
configPath = r"C:\Users\SK\Desktop\x\src\json\config.json"
with open(configPath) as f:
    config = json.load(f)

confEmail = config['email']
password = config['password']

# Set up Chrome options for incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
)

# Set up the webdriver with the specified options
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://twitter.com/i/flow/signup")

def type_like_human(element, text):
    """Type text with random delays for human-like input"""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))

# Step 2: Click the "Create account" button
try:
    create_account_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span"))
    )
    create_account_button.click()
    time.sleep(random.uniform(1, 3))  # Random delay
except (NoSuchElementException, TimeoutException):
    print("Failed to find or click the create account button")

# Step 3: Enter a random name
try:
    random_name = random.choice(["Alan", "Murat", "Azad", "Necati", "Aaron"])
    name_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))
    )
    type_like_human(name_input, random_name)
    time.sleep(random.uniform(1, 3))  # Random delay
except (NoSuchElementException, TimeoutException):
    print("Failed to find the name input field")

# Step 4: Enter the email
try:
    email_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, 'email'))
    )
    type_like_human(email_input, confEmail)  # Use the email from config
    time.sleep(random.uniform(1, 3))  # Random delay
except (NoSuchElementException, TimeoutException):
    print("Failed to find the email input field")

# Step 5: Enter the date of birth (month, day, year)
try:
    # Select Month
    month_dropdown = Select(WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "SELECTOR_1"))  # Updated ID for month
    ))
    month_dropdown.select_by_value("11")  # Select November
    time.sleep(random.uniform(1, 3))

    # Select Day (randomly between 18 and 31)
    day_dropdown = Select(WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "SELECTOR_2"))  # Assuming ID for day is SELECTOR_2
    ))
    random_day = random.randint(18, 31)  # Random day between 18 and 31
    day_dropdown.select_by_value(str(random_day))  # Select random day
    time.sleep(random.uniform(1, 3))

    # Select Year
    year_dropdown = Select(WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "SELECTOR_3"))  # Assuming ID for year is SELECTOR_3
    ))
    year_dropdown.select_by_value("1999")  # Select 1999
    time.sleep(random.uniform(1, 3))
except (NoSuchElementException, TimeoutException):
    print("Failed to find or select the date of birth fields")

# Step 6: Click the "Next" button
try:
    next_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='ocfSignupNextLink']"))
    )
    next_button.click()
    time.sleep(random.uniform(1, 3))  # Random delay
except (NoSuchElementException, TimeoutException):
    print("Failed to find or click the Next button")

# Wait for a moment before closing the browser
time.sleep(30)
browser.quit()
