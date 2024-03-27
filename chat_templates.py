# functions to define our prompt templates

def html_src(file_paths:list)->str:
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


# predefined choices for our prompts 
system_prompt_choices = {

    "Selenium generator using html src":
    '''You are a Python Selenium 4.18.1 script generator, which generates Python Selenium 4.18.1 script for all 
    classes (use ID or path) of all given HTML/JavaScript pages separated by '# next page' followed by the home 
    page URL which you can directly use as get URL. Use http try and exceptions for the pages, also add sufficient 
    time sleeps after input send keys and for web waiting.''',

    "Selenium generator from url" :""
}    


def system_prompt(choice:str)->str:
    """Returns detailed predefined prompt for the system based on your choice

    Args:
        choice (str): Simple predefined choice

    Returns:
        str: predefined prompt for oyur choice
    """
    return system_prompt_choices[choice]