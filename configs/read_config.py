from configparser import ConfigParser

config = ConfigParser()

def Read_Config(ini_file_path:str, entry:str, value:str)->str:
    """Reads config files and returns respective value

    Args:
        ini_file_path (str): file path to 
        entry (str): _description_
        value (str): _description_

    Returns:
        str: _description_
    """
    config = ConfigParser()
    config.read(ini_file_path)
    return config[entry][value]