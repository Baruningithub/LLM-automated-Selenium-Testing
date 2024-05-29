from langchain_community.llms import GPT4All
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from configs.read_config import Read_Configs 
from sys_prompts import system_prompt
from utils import html_scrapper, read_urls
from logs.logger import logger
from langchain_core.prompts import ChatPromptTemplate


model_path = ("/home/barunh/Documents/mpt-7b-chat-newbpe-q4_0.gguf")

# fetching urls form config files
page_list = ["admin_page", "data_entry"]
urls = Read_Configs("configs/url.ini", page_list, "url")

# web scrapping
logger.info("Starting scraping... ")
html_src_prompt = html_scrapper(urls)
logger.info("Content scraped")

llm = GPT4All(model=model_path)

sys_prompt = system_prompt("Selenium 4.18.1 generator")


# chat template 
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", sys_prompt),
        ("human", html_src_prompt),
        ("human", "{urls}")
    ]
)

llm_chain = LLMChain(prompt=chat_template, llm=llm)


logger.info("Chain execution has started . . . ") 
print(llm_chain.invoke({"urls":read_urls(urls)})['text'])
logger.info("Chain has successfully executed.")