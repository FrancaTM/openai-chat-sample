from openai import OpenAI
import api_key

client = OpenAI(api_key=api_key.api_key)

user_input = input("Add prompt: ")

completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "user", "content": user_input},
    ],
    temperature=0.2,
    max_tokens=50,
)

print(completion.choices[0].message)
