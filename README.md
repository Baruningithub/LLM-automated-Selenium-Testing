# LLM automated Selenium Project

## 📌 Table of Contents
1. [Introduction](#introduction)
2. [Implementation](#implementation)
3. [Features](#features)
4. [WebUI - Application Showcase](#webui---application-showcase)
5. [Vertex AI Integration](#vertex-ai-integration)
6. [📸 Image Showcase](#📸-image-showcase)
7. [Packages Used](#packages-used)
## Introduction 

1. This Project uses api integrated LLM(OpenAI-gpt3.5 turbo) to generate Selenium script of given html pages as prompt and executes the same using langchain.
2. Here we are giving a simple two page html/js login webpage, one login form followed by one data entry form as url to the scrapper defined using langchain itself.
3. The scrapped html source is now feeded to the model as prompt followed by their url as well.
4. Using a langchain chain we are generating the selenium script, modifying it into executable code and executing it all at once.
5. We are able to succesfully interact with all classes in the login page, redirect to data entry page, interact with all its classes and finally quit the driver.

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

## Challenges Faced 

## Future goals

## 📚 Links-and-References


Thanks for reading!
















