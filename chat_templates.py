# functions to define our prompt templates
from langchain_community.document_loaders import AsyncChromiumLoader,AsyncHtmlLoader


def html_scrapper(urls: list)-> str:
    """Scraps html of multiple pages from their urls

    Args:
        urls (list): list of urls to be scrapped

    Returns:
        str: a combined string conatining all html sources
    """
    src = []
    loader = AsyncHtmlLoader(urls)
    docs = loader.load()
    for doc in docs:
        src.append(doc.page_content)
    return '\n#next page\n'.join(src)
    



# predefined choices for our prompts 
system_prompt_choices = {

    "Selenium 4.18.1 generator":
    '''You are a Python Selenium 4.18.1 script generator, which generates Python Selenium 4.18.1 script for all 
    classes (use ID or path) of all given HTML/JavaScript pages separated by '#next page' followed by the home 
    page URL which you can directly use as get URL. Use http try and exceptions for the pages, also add sufficient 
    time sleeps after input send keys and for web waiting.''',

}    


def system_prompt(choice:str)->str:
    """Returns detailed predefined prompt for the system based on your choice

    Args:
        choice (str): Simple predefined choice

    Returns:
        str: predefined prompt for your choice
    """
    return system_prompt_choices[choice]



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

    return '\n#next page\n'.join(combined_contents)


