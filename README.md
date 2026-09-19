
<pre>
 _   _                      _ _     _     _       _
| \ | |                    | | |   | |   (_)     | |
|  \| | ___ _   _ _ __ __ _| | |   | |    _ _ __ | | __
| . ` |/ _ \ | | | '__/ _` | | |   | |   | | '_ \| |/ /
| |\  |  __/ |_| | | | (_| | | |___| |___| | | | |   <
|_| \_|\___|\__,_|_|  \__,_|_|_____|_____|_|_| |_|_|\_\

=======================================================

</pre>

# NeuralLink

NeuralLink is a simple terminal-based AI assistant that connects to a local language model server and streams responses directly in the command line.

It is designed for quick interactive use with a local model endpoint such as Ollama, making it easy to test prompts, ask follow-up questions, and work in a lightweight CLI environment.

## Features

- Terminal UI with a styled startup banner
- Dynamic greeting based on the current time
- Interactive prompt loop for chat-style usage
- Configuration for host, port, and model name
- Streaming responses from a local model server

## Project Structure

- `app.py` - application entry point
- `widget.py` - utility functions, config handling, and model calls
- `logo.py` - ASCII banner displayed on startup
- `config.json` - runtime configuration for the model host and model name
- `README.md` - project documentation

## Requirements

- Python 3.9+
- `requests` Python package
- A running local model server, typically Ollama

## Installation

1. Open a terminal in the project folder.
2. Install the required package:

```bash
pip install requests
```

3. Make sure a local inference server is running. For example, with Ollama:

```bash
ollama pull smollm2:135m
```

Then verify the server is available at:

```text
http://127.0.0.1:11434
```

## Configuration

The app reads its settings from `config.json`.

```json
{
    "name": "NeuralLink",
    "version": "0.1.0",
    "description": "Connection to a remote AI model",
    "system": {
        "host": "127.0.0.1",
        "model": "smollm2:135m",
        "port": 11434
    }
}
```

When the app starts, it also asks for the server address and model name if they are not already set.

## Running the App

From the project directory, run:

```bash
python app.py
```

The app will:

1. Load the current settings
2. Ask for the server address and model name if needed
3. Start the chat loop
4. Send your prompts to the configured model endpoint

## Usage

Once the app is running, type a prompt and press Enter:

```text
>>> Hello! Can you summarize the benefits of local AI?
```

The model response is streamed in chunks and displayed in the terminal.

## Notes

This project is meant to work with a local model API and is intentionally lightweight. It is best suited for experimentation, personal automation, or learning how a simple CLI AI client connects to a model server.

## Troubleshooting

- If the app fails to connect, confirm the model server is running.
- Check that the host and port match your server configuration.
- Ensure the model name matches a model available in your local server.
- If needed, edit `config.json` manually and restart the app.
