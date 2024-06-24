from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import logging
import time
import requests
from requests.exceptions import RequestException
from selenium.common.exceptions import WebDriverException
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from utils import sanitize_output, read_urls, html_scrapper
from sys_prompts import system_prompt
from logs.logger import logger  # Assuming this is a custom logger instance

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
from dotenv import load_dotenv
import os

load_dotenv()

# Fetch API key
api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI Chat model
llm = ChatOpenAI(temperature=0.8, api_key=api_key)

# Initialize Chrome WebDriver using WebDriver Manager
def get_webdriver():
    return webdriver.Chrome(ChromeDriverManager().install())

# Function to check interactions with Selenium WebDriver
def check_chain_interactions(chain_results, urls):
    for url in urls:
        try:
            driver = get_webdriver()
            driver.get(url)
            for result in chain_results:
                element = driver.find_element(By.XPATH, f"//*[contains(text(), '{result}')]")
                if not element:
                    logger.error(f"Element {result} not found on the webpage {url}")
                    driver.quit()
                    return False
            driver.quit()
            return True
        except WebDriverException as e:
            logger.error(f"Selenium WebDriver error: {e}")
            return False

# Function to execute the chain process
def execute_chain(urls, max_attempts=5, attempt=1):
    if attempt > max_attempts:
        logger.error("Max attempts reached. Exiting.")
        return

    try:
        response = requests.get(urls[0])
        response.raise_for_status()

        logger.info("Starting chain execution...")
        chain_results = chain.invoke({"urls": read_urls(urls)})
        time.sleep(2)
        logger.info("Chain execution successful.")

        if not check_chain_interactions(chain_results, urls):
            raise RuntimeError("Selenium process did not execute properly")

        return

    except (RequestException, ValueError, RuntimeError) as e:
        logger.error(f"Error occurred: {e}")
        logging.error(f"Error occurred: {e}")

    logger.info(f"Retrying... Attempt {attempt}/{max_attempts}")
    time.sleep(3)
    execute_chain(urls, max_attempts, attempt + 1)

if __name__ == '__main__':
    execute_chain(urls)
