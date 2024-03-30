from configparser import ConfigParser

config = ConfigParser()

config["admin_page"] = {
    "url" : "http://127.0.0.1:8085/"
}
config["data_entry"] = {
    "url" : "http://127.0.0.1:8085/data_entry.html"
}

with open ("openai-automated-selenium-project/configs/url.ini","w") as f:
    config.write(f)