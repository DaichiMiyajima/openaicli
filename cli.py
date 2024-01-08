import os
import openai
import readline

# APIキーの設定
openai.api_key = os.environ["OPENAI_API_KEY"]

def converse(prompt):
    stream = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        stream = True
    )

    print("AI Answer")
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
    print("\n")

def main():
    print("Welcome to the Conversation CLI!\n Type \n'ok' to send a message to openai \n'exit' to quit.")
    user_inputs = ""
    while True:
        user_input = input("You: ")
       

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        if user_input.lower() == 'ok':
            print(user_inputs)
            converse(user_inputs)
        
        user_inputs += user_input + "\n"

if __name__ == "__main__":
    main()
