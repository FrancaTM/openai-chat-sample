from openai import OpenAI
import api_key

client = OpenAI(api_key=api_key.api_key)

chat_messages = []

while True:
    user_message = input("User: ")

    chat_messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=chat_messages,
        temperature=0.2,
        max_tokens=10,
    )

    ai_response = response.choices[0].message.content
    chat_messages.append({"role": "assistant", "content": ai_response})
    print("\nAI: ", ai_response, "\n")
    # print(chat_messages, "\n")
