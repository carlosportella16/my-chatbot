from openai import OpenAI
import os

# Load the API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OpenAI API key found. Set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)


def chat_with_gpt(prompt):
    response = client.chat.completions.create(
       messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-4",
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