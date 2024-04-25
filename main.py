from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_experimental.utilities import PythonREPL
from langchain.tools import Tool
from langchain_core.output_parsers import StrOutputParser
from langchain_core.exceptions import OutputParserException
from utils import sanitize_output
from chat_templates import system_prompt, html_scrapper
from logs.logger import logger
import requests
from requests.exceptions import RequestException
from configs.read_config import Read_Configs,read_urls 
import time 


# Load environment variables from the .env file where our api key is stored
load_dotenv()

# fetching the api key from the .env file
api_k = os.getenv('OPENAI_API_KEY')

# chat model object (default model- gpt3.5 turbo)
chat_model = ChatOpenAI(temperature=0.8,api_key=api_k)


# Prompt to define sytem
sys_prompt = system_prompt("Selenium 4.20.0 generator openai")


# Fetching urls form config files
page_list = ["admin_page", "data_entry"]
urls = Read_Configs("configs/url.ini", page_list, "url")


# Web scrapping
logger.info("Starting scraping... ")
html_src_prompt = html_scrapper(urls)
logger.info("Content scraped") 


# Chat template 
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", sys_prompt),
        ("human", html_src_prompt),
        ("human", "{urls}")
    ]
)

# Setting up python_repl that runs valid python command
python_repl = PythonREPL()
repl_tool = Tool(
    name = "python_repl",
    description = '''A Python shell. Use this to execute python commands. 
    Input should be a valid python command. Wait for code to execute completely ''',
    func = python_repl.run,
)

 
# StrOutputParser() - converts response into parsable string
chain = (
        chat_template |
        chat_model | 
        StrOutputParser() | 
        sanitize_output |
        (lambda x: repl_tool(x) if x is not None else None)
        )


if __name__=='__main__':
  try:
    # Checking web appplication status
    response = requests.get(urls[0])  
    response.raise_for_status()

    # Invoking chain results
    logger.info("Chain execution has started . . . ") 

    chain.invoke({"urls":read_urls(urls)})  # chain invoke 
    time.sleep(2) 

    logger.info("Chain has successfully executed.")


  except RequestException as re:
    logger.error("Unable to request web application")
    print("Error occurred while requesting web app: ",re)

  except OutputParserException as e:
    logger.error("Unable to execute chain")
    print("Error occurred while parsing the output: ",e)