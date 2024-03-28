# OpenAI automated Selenium Project

1. This Project uses OpenAI API to generate Selenium script of given html pages as prompt and executes the same using langchain.
2. Here we are giving a simple two page html/js login webpage, one login form followed by one data entry form as url to the scrapper defined using langchain itself.
3. The scrapped html source is now feeded to the model as prompt followed by their url as well.
3. Using model chains in langchain we are generating the selenium script, modifying it into executable code and executing it all at once.
4. We are able to succesfully interact with all classes in the login page, redirect to data entry page, interact with all its classes and finally quit the driver.


#### Modules/Frameworks used
- Selenium Python (API to write functional tests using Selenium WebDriver)
- openai/ChatOpenAI (OpenAI API)
- Langchain (Framework for llms)

