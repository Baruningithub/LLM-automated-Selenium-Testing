# OpenAI automated Selenium Project

1. This Project uses OpenAI API to generate Selenium script of given html pages as prompt and executes the same using langchain.
2. Here we are giving a simple two page html/js login webpage, one login form followed by one data entry form as prompt.
3. Using model chains in langchain we are generating the selenium script, modifying it into executable code and executing it all at once.
4. We are able succesfully interact with all classes in the login page, redirect to data entry page, interact with all its classes and finally quit the driver.


#### Modules/Libraries used
- selenium (internally)
- webdriver (internally)
- openai/ChatOpenAI
- langchain_core.prompts.ChatPromptTemplate
- langchain_experimental.utilities.PythonREPL
- langchain_core.output_parsers.StrOutputParser

