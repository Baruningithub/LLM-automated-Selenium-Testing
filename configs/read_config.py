from configparser import ConfigParser

def Read_Config(ini_file_path:str, entry: str, value:str)->str:
    """Reads a config file and returns value of given entry

    Args:
        ini_file_path (str): path to config file(ini file)
        entry (str): entry we want to access
        value (str): value we want from the entry

    Returns:
        str: _description_
    """
    config = ConfigParser()
    config.read(ini_file_path)
    return config[entry][value]


def Read_Configs(ini_file_path:str, entries: list, value:str)->list:
    """Reads a config file and returns list of values of given entries

    Args:
        ini_file_path (str): path to config file(ini file)
        entries (list): entries we want or access values of
        value (str): value we want

    Returns:
        list: list of values
    """
    values = []
    for entry in entries:
        values.append(Read_Config(ini_file_path, entry, value))
    return values

def read_urls(list_of_urls:list)->str:
    """_summary_

    Args:
        list_of_urls (list): _description_

    Returns:
        str: _description_
    """
    return ", ".join(list_of_urls)
