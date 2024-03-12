from selenium import webdriver
import time

# Page 1 Script

# Initialize a Chrome webdriver instance
driver = webdriver.Chrome()

# Open the URL of the index.html page
driver.get("http://127.0.0.1:5500/index.html")

# Wait for 1 second for the page elements to load
time.sleep(1)

# Find the username input field and enter "Barun"
username = driver.find_element("id", "username")
username.send_keys("Barun")  # This username was set in the js(automaticalyy read by openai generator)
time.sleep(0.5)

# Find the password input field and enter "pswd"
password = driver.find_element("id", "password")
password.send_keys("pswd")  # This password was set in the js(automaticalyy read by openai generator)
time.sleep(0.5)

# Find and click the login button
login_button = driver.find_element("xpath", "//button[text()='Login']")
login_button.click()
time.sleep(2)

# Page 2 Script

# Redirect to the data_entry.html page
driver.get("http://127.0.0.1:5500/data_entry.html")
time.sleep(1)

# Find the registration number input field and enter input
regd_no = driver.find_element("id", "data1")
regd_no.send_keys("123456")
time.sleep(0.5)

# Find the semester input field and enter input
semester = driver.find_element("id", "data2")
semester.send_keys("Spring 2023")
time.sleep(0.5)

# Find and click the submit button
submit_button = driver.find_element("xpath", "//button[text()='Submit']")
submit_button.click()
time.sleep(2)

# Quit the WebDriver, closing all windows
driver.quit()
