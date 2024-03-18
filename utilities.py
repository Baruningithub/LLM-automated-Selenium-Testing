# Utility unctions

def sanitize_output(text:str):
    '''function that modifies the string converted response into 
    executable code by removing uneccessary tags'''
    _, after = text.split("```python")
    return after.split("```")[0]