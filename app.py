from openai import OpenAI
import api_key

client = OpenAI(api_key=api_key.api_key)

user_message = input("User: ")

response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "user", "content": user_message},
    ],
    temperature=0.2,
    max_tokens=50,
)

ai_response = response.choices[0].message.content
print("AI: ", ai_response)
