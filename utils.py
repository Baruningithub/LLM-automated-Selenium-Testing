# Utility functions

def sanitize_output(text:str)->str:
    """modifies the string converted response into executable code string

    Args:
        text (str): _description_

    Returns:
        str: _description_
    """
    
    _, after = text.split("```python")
    return after.split("```")[0]