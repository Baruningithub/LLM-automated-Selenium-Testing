# Utility functions

def sanitize_output(text:str):
    '''modifies the string converted response into 
    executable code string'''
    _, after = text.split("```python")
    return after.split("```")[0]