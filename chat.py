import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_history = []

while True:
    prompt = input("Enter a prompt:")

    if prompt == "exit":
        break

    chat_history.append({
        "role": "user",
        "content": prompt
    })

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = chat_history,
        stream = True,
    )

    collected_messages = []

    for chunk in response:
        chunck_messages = chunk["choices"][0]["delta"]
        collected_messages.append(chunck_messages)
        full_reply_content = "".join([m.get('content','') for m in collected_messages])
        print(full_reply_content)
        print("\033[H\033[J", end="")

    chat_history.append({
        "role": "assistant",
        "content": full_reply_content
    })
    print(full_reply_content)

    