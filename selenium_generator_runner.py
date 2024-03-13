from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_experimental.utilities import PythonREPL
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from the .env file where our api key is stored
load_dotenv()

api_k = os.getenv('OPENAI_API_KEY')

# chat model 
chat_model = ChatOpenAI(api_key = api_k)


# chat template 

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", """You are a python selenium 4.18.1 script generator, which generates python 
     selenium 4.18.1 script for all classes(use id or path) of all given html/javascript pages 
    separated # page url name which you can directly use as get url, also 
     add time sleeps after input send keys and for web waiting"""),
        ("human", '''
                
        # {url1} 

        <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Admin Login</title>
  <link rel="stylesheet" href="index.css">
</head>
<body>

  <div class="container">
    <h2>Login</h2>

    <form id="loginForm">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" required>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required>
      <button type="submit">Login</button>
    </form>
  </div>

  <script src="index.js"></script>

</body>
</html>


# {url2}

    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Data Entry</title>
  <link rel="stylesheet" href="data_entry.css">
</head>
<body>

  <div class="container">
    <h2>Add Details</h2>

    <form id="dataEntryForm">
      <label for="Regd no.">University Regd no.:</label>
      <input type="int" id="data1" name="data1" required>
      <label for="Sem">Semester:</label>
      <input type="text" id="data2" name="data2" required>
      <button type="submit">Submit</button>
    </form>

    <h2>Saved Entries</h2>
    <ul id="entries"></ul>
  </div>

  <script src="data_entry.js"></script>

</body>
</html>


            '''
         
         ),
        
    ]
)


# # converting chat to readable prompt
# chat_prompt = chat_template.format_messages()

def _sanitize_output(text:str):
    _, after = text.split("```python")
    return after.split("```")[0]

chain = chat_template | chat_model | StrOutputParser() | _sanitize_output | PythonREPL().run

response = chain.invoke({"url1":"http://127.0.0.1:5500/openai-automated-selenium-project/index.html","url2":"http://127.0.0.1:5500/openai-automated-selenium-project/data_entry.html"})
print(response)