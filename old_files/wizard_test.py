
# Failed llm, requires CUDA for execution


from openai import OpenAI

API_URL = "/"
model_path = "/wizard_model_path"
client = OpenAI(
    base_url=API_URL,
    api_key="EMPTY",
)
system_prompt = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. "
stop_tokens = []
completion = client.chat.completions.create(
    model=model_path,
    temperature=0,
    top_p=1,
    max_tokens=4096,
    stop=stop_tokens,
    messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Hello! What is your name?"},
    {"role": "assistant", "content": "I am WizardLM2!"},
    {"role": "user", "content": "Nice to meet you!"},
  ]
)

print(completion.choices[0].message.content)
