
from selenium import webdriver
import time

# Open the first page
url1 = "http://127.0.0.1:8090/"
driver = webdriver.Chrome()

try:
    driver.get(url1)
    time.sleep(2)

    username_input = driver.find_element("id", "username")
    username_input.send_keys("admin")
    time.sleep(2)

    password_input = driver.find_element("id", "password")
    password_input.send_keys("password")
    time.sleep(2)

    login_button = driver.find_element("xpath", "//button[@type='submit']")
    login_button.click()
    time.sleep(5)

except Exception as e:
    print(e)

# Open the second page
url2 = "http://127.0.0.1:8090/data_entry.html"

try:
    driver.get(url2)
    time.sleep(2)

    regd_input = driver.find_element("id", "data1")
    regd_input.send_keys("123456")
    time.sleep(2)

    sem_input = driver.find_element("id", "data2")
    sem_input.send_keys("Spring 2022")
    time.sleep(2)

    submit_button = driver.find_element("xpath", "//button[@type='submit']")
    submit_button.click()
    time.sleep(5)

except Exception as e:
    print(e)

finally:
    driver.quit()
