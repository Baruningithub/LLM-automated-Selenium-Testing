from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI

llama = LlamaAPI("LL-VgYKjgRlpb0I7sFAUE5SPUipwyn6sINxJOmiOP5ACcUux2adLl5x8iDckNi5B8yf")


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