from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_experimental.utilities import PythonREPL
from langchain.tools import Tool
from langchain_core.output_parsers import StrOutputParser
from utils import sanitize_output, read_urls, html_scrapper
from sys_prompts import system_prompt
from logs.logger import logger
import requests
from requests.exceptions import RequestException
from configs.read_config import Read_Configs
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


# Load environment variables from the .env file where our api key is stored
load_dotenv()

# fetching the api key from the .env file
api_k = os.getenv('OPENAI_API_KEY')

# chat model object (default model- gpt3.5 turbo)
llm = ChatOpenAI(temperature=0.8,api_key=api_k)


# Prompt for system message
sys_prompt = system_prompt("Selenium 4.20.0 generator openai")


# Fetching urls form config files
page_list = ["admin_page", "data_entry"]
urls = Read_Configs("configs/url.ini", page_list, "url")


# Web scrapping
logger.info("Starting scraping... ")
html_src_prompt = html_scrapper(urls)
logger.info("Content scraped") 


# Prompt
prompt = ChatPromptTemplate.from_messages(
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
        prompt |
        llm | 
        StrOutputParser() | 
        sanitize_output |
        (lambda x: repl_tool(x) if x is not None else None)
        )


def check_chain_interactions(chain_results,urls):
    
    for url in urls:
      try:
          # Initialize Selenium WebDriver
          driver = webdriver.Chrome()  
          driver.get(url)  

          # Check if the elements interacted with by the chain are present on the webpage
          for result in chain_results:
              element = driver.find_element(By.XPATH, f"//*[contains(text(), '{result}')]")
              if not element:
                  logger.error(f"Element {result} not found on the webpage")
                  return False

          driver.quit()
          return True

      except WebDriverException as e:
          logger.error(f"Selenium WebDriver error: {e}")
          return False
      

  
def execute_chain(urls:list, max_attempts=5, attempt=1):
    
    if attempt > max_attempts:
        logger.error("Max attempts reached. Exiting.")
        return

    try:
        # Checking web application status
        response = requests.get(urls[0])
        response.raise_for_status()

        # Invoking chain results
        logger.info("Chain execution has started . . . ")

        # Capture relevant information during chain execution
        chain_results = chain.invoke({"urls": read_urls(urls)})  # chain invoke
        time.sleep(2)

        logger.info("Chain has successfully executed.")

        # Check if Selenium process executed properly
        if not check_chain_interactions(chain_results,urls):
            raise RuntimeError("Selenium process did not execute properly")

        return 

    except (RequestException, ValueError, RuntimeError) as e:
        logger.error(f"Error occurred: {e}")
        print(f"Error occurred: {e}")

    # If selenium didnt execute properly or validation failed, retry
    logger.info(f"Retrying... Attempt {attempt}/{max_attempts}")
    time.sleep(3)  # wait for some time before re-executing
    execute_chain(urls, max_attempts, attempt + 1)

if __name__ == '__main__':
    execute_chain(urls=urls)