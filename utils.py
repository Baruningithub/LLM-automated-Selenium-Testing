# Utility functions

def sanitize_output(text:str)->str:
    """modifies the string converted response into executable code string

    Args:
        text (str): llm response text

    Returns:
        str: sanitized text
    """
    
    _, after = text.split("```python")
    return after.split("```")[0]