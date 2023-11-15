from openai import OpenAI
import os

client = OpenAI(
    api_key="YOUR-API-KEY"
)


def chat_with_gpt(prompt):
    response = client.chat.completions.create(
       messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        try:
            response = chat_with_gpt(user_input)
            print("Chatbot:", response)
        except Exception as e:
            print("An error occurred:", e)