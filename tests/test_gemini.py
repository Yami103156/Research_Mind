from config.model import llm

response = llm.invoke("Who are you? Answer in one sentence.")

print(response.content)