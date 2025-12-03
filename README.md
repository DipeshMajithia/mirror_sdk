# Mirror SDK

The official Python SDK for the Mirror Chat API. Easily integrate your Mirror agents into any Python application.

## Features

- **Session Management**: Create and manage chat sessions with your agents.
- **Streaming Chat**: Real-time streaming responses from your agents.
- **Simple Authentication**: Easy-to-use API key authentication.
- **Type Hinting**: Fully typed for better development experience.

## Installation

Install the package via pip:

```bash
pip install mirrorsdk
```

## Quick Start

Here's how to get started with the Mirror SDK:

```python
from mirror_sdk import MirrorClient

# 1. Initialize the client
# Replace with your actual API key and base URL
client = MirrorClient(
    api_key="your_api_key_here",
    base_url="http://localhost:807"
)

# 2. Create a new chat session
session = client.create_session(model="mirror_general")
print(f"Created session: {session['id']}")

# 3. Chat with your agent
prompt = "Hello! Tell me a fun fact about space."

print(f"User: {prompt}")
print("Assistant: ", end="", flush=True)

# Responses are streamed in chunks
for chunk in client.chat(session['id'], prompt):
    print(chunk, end="", flush=True)
```

## Configuration

The `MirrorClient` accepts the following parameters:

- `api_key` (str): Your secret API key.
- `base_url` (str): The base URL of your Mirror API server (default: `http://localhost:807`).

## Error Handling

The SDK raises standard exceptions when things go wrong:

```python
try:
    client.create_session()
except Exception as e:
    print(f"An error occurred: {e}")
```

## License

MIT License