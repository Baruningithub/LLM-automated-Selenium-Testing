from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_experimental.utilities import PythonREPL
from langchain_core.output_parsers import StrOutputParser
from langchain_core.exceptions import OutputParserException
from utilities import sanitize_output
from chat_templates import html_src, system_prompt
from logger import logger
import requests
from requests.exceptions import RequestException

# Load environment variables from the .env file where our api key is stored
load_dotenv()

# fetching the api key from the .env file
api_k = os.getenv('OPENAI_API_KEY')

# chat model object (default model- gpt3.5 turbo)
chat_model = ChatOpenAI(api_key = api_k)

home_url = "http://127.0.0.1:5500/openai-automated-selenium-project/Templates/index.html"
sys_prompt = system_prompt("Selenium generator using html src")
src_prompt = html_src(["Templates/index.html","Templates/data_entry.html"])

# chat template 
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", sys_prompt),
        ("human", src_prompt),
        ("human", "{url}")
    ]
)


# the model chain 
# StrOutputParser() - converts response into string parser
# PythonREPL().run - excutes the final sanitised result (the selenium starts interacting with the webpages)
chain = chat_template | chat_model | StrOutputParser() | sanitize_output | PythonREPL().run


# finally invoke chain results, passing urls as user inputs
if __name__=='__main__':
  
  try:
    response = requests.get(home_url)
    response.raise_for_status()

    logger.info("Chain execution has started . . . ")
    chain.invoke({"url":home_url})
    logger.info("Chain has successfully executed")

  except RequestException as re:
    logger.error("Unable request web application")
    print("Error occurred while requesting web app: ",re)

  except OutputParserException as e:
    logger.error("Unable to execute chain")
    print("Error occurred while parsing the output: ",e)