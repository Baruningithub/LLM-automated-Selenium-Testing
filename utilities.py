
# function that modifies the string converted response into executable code by removing uneccessary tags
def sanitize_output(text:str):
    _, after = text.split("```python")
    return after.split("```")[0]