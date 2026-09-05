import requests
import json

import os
import sys
from pathlib import Path

# clear cmd
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# Function to clear the previous line in the terminal
def clear_last_line():
    # \033[1A moves cursor up 1 line, \033[2K clears the entire line
    sys.stdout.write("\033[1A\033[2K")
    sys.stdout.flush()

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

def get_greeting():

    try:
        import datetime
        # Determine dynamic time of day greeting
        hour = datetime.datetime.now().hour
        if hour < 12:
            return "Good morning"
        elif hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"

    except Exception:
        return "Welcome"    


CONFIG_PATH = Path(__file__).with_name("config.json")

def load_config():
    with CONFIG_PATH.open("r", encoding="utf-8") as config_file:
        return json.load(config_file)


def get_config_value(*keys, default=None):
    value = load_config()
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value


def update_config_value(host=None, model=None):
    config = load_config()
    system_config = config.setdefault("system", {})

    current_host = system_config.get("host", "127.0.0.1")
    current_model = system_config.get("model", "smollm2:135m")

    if host is None:
        host = input(f"[?] /server/address  :: ").strip() or current_host
        clear_last_line()
    if model is None:
        model = input(f"[?] /model/name      :: ").strip() or current_model
        clear_last_line()

    system_config["host"] = host
    system_config["model"] = model

    with CONFIG_PATH.open("w", encoding="utf-8") as config_file:
        json.dump(config, config_file, indent=4)
        config_file.write("\n")

    clear_last_line()
    summary = f"""
    [ SUMMARY ]
        [?] /server/address  :: {system_config["host"]}:{system_config['port']}
        [?] /model/name      :: {system_config['model']}
    """
    print(summary)

    return config


def get_model_url():
    host = get_config_value("system", "host", default="127.0.0.1")
    port = get_config_value("system", "port", default=11434)
    return f"http://{host}:{port}/api/generate"

def ask_llm(prompt):
    model = get_config_value("system", "model", default="smollm2:135m")

    response = requests.post(
        get_model_url(),
        json={
            "model": model,
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
