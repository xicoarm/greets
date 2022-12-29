import openai
import time

def generate_prompt():
    return "suggest three happy new year wishes to my girlfriend"


response = openai.Completion.create(
    model="text-davinci-003",
    prompt=generate_prompt(),
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print (response["choices"][0]["text"])


