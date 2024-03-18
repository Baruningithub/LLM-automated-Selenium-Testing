

def html_src(file_paths:list):
    '''
    Reads multiple html src files, concatenates their content and returns a readable string for our prompt
    '''
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
    return '\n'.join(combined_contents)

# predefined choices for our prompts for simplicity
system_prompt_choices = {

    "Selenium 4.18.1 using html src":
    '''You are a python selenium 4.18.1 script generator, which generates python 
     selenium 4.18.1 script for all classes(use id or path) of all given html/javascript pages 
    separated # page url name which you can directly use as get url with try and except, also 
     add time sleeps after input send keys and for web waiting ''',

    "Selenium 4.18.1 from url" :""
}    

def system_prompt(choice):
    '''
    Returns detailed predefined prompt for the system based on your choice
    '''
    return system_prompt_choices[choice]