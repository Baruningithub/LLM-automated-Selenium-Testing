from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_experimental.utilities import PythonREPL
from langchain_core.output_parsers import StrOutputParser
from langchain_core.exceptions import OutputParserException
from utils import sanitize_output
from chat_templates import html_src, system_prompt
from logs.logger import logger
import requests
from requests.exceptions import RequestException
from configs.read_config import Read_Config 

# Load environment variables from the .env file where our api key is stored
load_dotenv()

# fetching the api key from the .env file
api_k = os.getenv('OPENAI_API_KEY')

# chat model object (default model- gpt3.5 turbo)
chat_model = ChatOpenAI(temperature=0.7, api_key = api_k)

# fetching url from config file
url = Read_Config("configs/url.ini", "admin_page", "url")

sys_prompt = system_prompt("Selenium generator using html src")
src_prompt = html_src(["html_templates/index.html","html_templates/data_entry.html"])

# chat template 
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", sys_prompt),
        ("human", src_prompt),
        ("human", "{url}")
    ]
)


# the model chain 
# StrOutputParser() - converts response into parsable string
# PythonREPL().run - excutes the final sanitised result (the selenium starts interacting with the webpages)
chain = chat_template | chat_model | StrOutputParser() | sanitize_output | PythonREPL().run


if __name__=='__main__':
  
  try:
    # checking web appplication status
    response = requests.get(url)
    response.raise_for_status()

    # invoking chain results
    logger.info("Chain execution has started . . . ") 

    chain.invoke({"url":url})    # chain invoke 

    logger.info("Chain has successfully executed.")


  except RequestException as re:
    logger.error("Unable to request web application")
    print("Error occurred while requesting web app: ",re)

  except OutputParserException as e:
    logger.error("Unable to execute chain")
    print("Error occurred while parsing the output: ",e)