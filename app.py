from openai import OpenAI
import api_key

client = OpenAI(api_key=api_key.api_key)

user_input = input("Add prompt: ")

completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        # {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input},
    ],
)

print(completion.choices[0].message)
