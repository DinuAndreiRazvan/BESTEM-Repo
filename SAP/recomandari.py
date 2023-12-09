import os
from openai import OpenAI

client = OpenAI(api_key="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")


content = input("User: ")
completion = client.chat.completions.create(
    model="gpt-3", messages=[{"role": "user", "content": content}]
)

chat_response = completion.choices[0].message.content
print(f"ChatGPT: {chat_response}")
