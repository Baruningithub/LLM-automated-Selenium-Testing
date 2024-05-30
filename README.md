# LLM automated Selenium Project

## 📌 Table of Contents
1. [Introduction](#introduction)
2. [Implementation](#implementation)
3. [OpenAI Integration](#openai-integration)
4. [Packages used](#packages-used)
5. [Challenges faced](#challenges-faced)
6. [Future goals](#future-goals)
7. [Links and References](#links-and-references)
## Introduction 

1. This project uses the OpenAI GPT-3.5 Turbo API to generate Selenium scripts from given HTML pages and executes them using LangChain.
2. A couple of sample website URLs are provided to the web scraper, which is built using LangChain.
3. The scraped HTML source is fed to the model as a prompt, along with the URL.
4. A LangChain chain created using prompts,llm and code executer generates the Selenium script, modifies it into executable code, and executes it.
5. The process includes interacting with all elements on the on the sample pages and finally quitting the driver.


## Implementation

### Environment Setup
 **Create a virtual environment**:

To ensure a consistent and isolated development environment, we use Python's built-in venv module to create a virtual environment. Follow the steps below to set up the virtual environment and install the necessary dependencies:

   ```sh
   cd /path/to/your/project
   python -m venv venv
   source venv/bin/activate
```

 **Install the required dependencies from the [`requirements.txt`](https://gitlab.mindfire.co.in/barunh/openai-automated-selenium-project/-/blob/main/requirements.txt) file**:
 
   ```sh
   pip install --upgrade pip
   pip install -r requirements.txt

```

### Execution

Run the [`main.py`](https://gitlab.mindfire.co.in/barunh/openai-automated-selenium-project/-/blob/main/main.py) file on your local machine with Python 3.10+ installed:

  ```sh
cd /path/to/your/project
python3 main.py
```

## OpenAI Integration
This project integrates with [OpenAI](https://openai.com/) to leverage its powerful machine learning models(gpt3.5) for selenium script generation. OpenAI is an AI research and deployment company for more details on how LangChain integrates with OpenAI, refer to the [official documentation](https://python.langchain.com/docs/integrations/providers/openai).

You need Open AI API **Key** to use this project. To get your key, follow these steps:

### Get OpenAI API key

1. Go to the [OpenAI website](https://beta.openai.com/signup/).
2. Fill out the form with your information and click “Create Account”.
3. Once you are logged in, click on “API Keys” in the left-hand menu.
4. Click on “Generate New Key” to create a new API key.
5. Copy your API key – we will use it later in our Python code.

## Packages Used

- **langchain**: A Python client library for interacting with the LangChain API.
- **openai**: A Python client library for interacting with the OpenAI API.
- **python-dotenv**: Reads the key-value pair from .env file and adds them to environment variable.
- **selenium**: A powerful tool for controlling web browsers through programs and performing browser automation.


## 📚Links and References

- [LangChain documentation](https://python.langchain.com/v0.1/docs/get_started/introduction
)
- [OpenAI API documentation](https://platform.openai.com/docs/overview
)



Thanks for reading!
















