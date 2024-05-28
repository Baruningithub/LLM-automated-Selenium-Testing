# Utility functions
from langchain_community.document_loaders import AsyncChromiumLoader,AsyncHtmlLoader
from configs.read_config import Read_Configs

def sanitize_output(text:str)->str:
    """modifies the string converted response into executable code string

    Args:
        text (str): llm response text

    Returns:
        str: sanitized text
    """
    
    _, after = text.split("```python")
    return after.split("```")[0]


def read_urls(list_of_urls:list)->str:
    """_summary_

    Args:
        list_of_urls (list): _description_

    Returns:
        str: _description_
    """
    return ", ".join(list_of_urls)


# web scarping functionalities
def html_scrapper(urls: list)-> str:
    """Scraps html of multiple pages from their urls

    Args:
        urls (list): list of urls to be scrapped

    Returns:
        str: a combined string containing all html sources
    """
    src = []
    loader = AsyncHtmlLoader(urls)
    docs = loader.load()
    for doc in docs:
        src.append(doc.page_content)
    return '\n#next page\n'.join(src)


def html_scrapper_for_liveserver(urls: list)-> str:
    """Scraps html of multiple pages from their urls

    Args:
        urls (list): list of urls to be scrapped

    Returns:
        str: a combined string conatining all html sources
    """
    combined = []
    for url in urls:
        loader = AsyncChromiumLoader(urls)
        html = loader.load()
        src = (html[0].page_content).split("<!-- Code injected by live-server -->")[0]
        combined.append(''.join(src))
    return '\n#next page\n'.join(combined)


def html_file_reader(file_paths:list)->str:
    """Reads multiple html src files, concatenates their content

    Args:
        file_paths (list): source files

    Returns:
        str: source as text
    """
    
    combined_contents = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                file_contents = file.read()
                combined_contents.append(file_contents)  
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"Error occurred while reading file '{file_path}': {e}")

    return '\n #next page \n\n'.join(combined_contents)