import requests
import json

import os

# clear cmd
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# # Open new termanal """
# import os
# import sys

# if "--terminal" not in sys.argv:
#     os.system(
#         f'start "NeuralLink" cmd /k python "{os.path.abspath(__file__)}" --terminal'
#     )
#     sys.exit()
# # """

# Function to run loader make work done by \r
def loader(str, sec=10):
    import time
    
    spinner = ["|", "/", "-", "\\"]

    for _ in range(sec):
        for symbol in spinner:
            print(f"\r{symbol} {str}", end="", flush=True)
            time.sleep(0.1)

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
