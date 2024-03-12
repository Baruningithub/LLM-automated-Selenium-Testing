# OpenAI automated Selenium Project

## How the project works until now: 

1. This Project uses OpenAI API to generate Selenium script of given html/js pages as prompt.
2. Here we are giving a simple two page html/js one [login form](https://gitlab.mindfire.co.in/barunh/openai-automated-selenium-project/-/blob/main/index.html
) followed by one [data entry](https://gitlab.mindfire.co.in/barunh/openai-automated-selenium-project/-/blob/main/data_entry.js) form to the [script generator](https://gitlab.mindfire.co.in/barunh/openai-automated-selenium-project/-/blob/main/login_response1.py
).
2. The generated script is saved and executed in a separate [file](https://gitlab.mindfire.co.in/barunh/openai-automated-selenium-project/-/blob/main/login_response1.py
).
3. We are able succesfully interact with all classes in the login page, move to data entry page, interact with all its classes and finally quit the driver.


### Modules/Libraries used
selenium

webdriver

openai
