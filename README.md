# OpenAI automated Selenium Project

## How the project works until now: 

1. This Project uses OpenAI API to generate Selenium script of given html/js pages as prompt and exexutes the same using
2. Here we are giving a simple two page html/js one login form followed by one data entry form as prompt.
2. Using model chains in langchain we are generating the selenium script, modifying it into executable code and executing it all at once.
3. We are able succesfully interact with all classes in the login page, move to data entry page, interact with all its classes and finally quit the driver.


#### Modules/Libraries used
- selenium (internally)
- webdriver (internally)
- openai/ChatOpenAI
- langchain_core.prompts.ChatPromptTemplate
- langchain_experimental.utilities.PythonREPL
- langchain_core.output_parsers.StrOutputParser

