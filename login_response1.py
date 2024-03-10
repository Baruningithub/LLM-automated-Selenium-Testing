
from selenium import webdriver
import time

# Page 1 Script
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")

time.sleep(1)

username = driver.find_element("id", "username")
username.send_keys("Barun")
time.sleep(0.5)

password = driver.find_element("id", "password")
password.send_keys("pswd")
time.sleep(0.5)

login_button = driver.find_element("xpath", "//button[text()='Login']")
login_button.click()
time.sleep(2)

# Page 2 Script
driver.get("http://127.0.0.1:5500/data_entry.html")
time.sleep(1)

regd_no = driver.find_element("id", "data1")
regd_no.send_keys("123456")
time.sleep(0.5)

semester = driver.find_element("id", "data2")
semester.send_keys("Spring 2023")
time.sleep(0.5)

submit_button = driver.find_element("xpath", "//button[text()='Submit']")
submit_button.click()
time.sleep(2)

driver.quit()

