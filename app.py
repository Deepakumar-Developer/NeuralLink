import requests
import json

URL = "http://127.0.0.1:11434/api/generate"

def ask_llm(prompt):

    response = requests.post(
        URL,
        json={
            "model": "smollm2:135m",
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )

    for line in response.iter_lines():
        if line:
            data = json.loads(line)

            if "response" in data:
                yield data["response"]

            if data.get("done"):
                break


for chunk in ask_llm("Write the python code to run the ifconfig at 192.168.0.10"):
    print(chunk, end="", flush=True)