from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI
from dotenv import load_dotenv
import os


# Load environment variables from the .env file where our api key is stored
load_dotenv()

# fetching the api key from the .env file
api_k = os.getenv('LLAMA_API_KEY')

llama = LlamaAPI(api_token=api_k)


from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from configs.read_config import Read_Configs,read_urls 
from chat_templates import system_prompt, html_scrapper
from logs.logger import logger
from langchain_core.prompts import ChatPromptTemplate


# fetching urls form config files
page_list = ["admin_page", "data_entry"]
urls = Read_Configs("configs/url.ini", page_list, "url")

# web scrapping
logger.info("Starting scraping... ")
html_src_prompt = html_scrapper(urls)
logger.info("Content scraped")


llm = ChatLlamaAPI(client=llama)

sys_prompt = system_prompt("Selenium 4.20.0 generator llama2")


# chat template 
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", sys_prompt),
        ("human", html_src_prompt),
        ("human", "{urls}")
    ]
)

llm_chain = chat_template | llm


logger.info("Chain execution has started . . . ") 
print(llm_chain.invoke({"urls":read_urls(urls)}).content)
logger.info("Chain has successfully executed.")