import requests
import json
from typing import Generator, Optional, Dict, Any

class MirrorClient:
    def __init__(self, api_key: str, base_url: str = "http://localhost:807"):
        """
        Initialize the Mirror SDK Client.
        
        :param api_key: Your secret API key.
        :param base_url: The base URL of the Mirror API (default: http://localhost:807).
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "X-API-Key": self.api_key,
            "Content-Type": "application/x-www-form-urlencoded"
        }

    def create_session(self, model: str = "mirror_general") -> Dict[str, Any]:
        """
        Create a new chat session.
        
        :param model: The model ID to use (default: "mirror_general").
        :return: A dictionary containing session details (id, title, etc.).
        """
        url = f"{self.base_url}/api-chat/create_session"
        data = {"model": model}
        
        resp = requests.post(url, headers=self.headers, data=data)
        if resp.status_code != 200:
            raise Exception(f"Failed to create session: {resp.status_code} - {resp.text}")
        
        return resp.json()

    def chat(self, session_id: str, prompt: str, model: str = "mirror_general") -> Generator[str, None, None]:
        """
        Send a message to the chat session and stream the response.
        
        :param session_id: The ID of the active session.
        :param prompt: The user's message.
        :param model: The model ID to use.
        :return: A generator yielding chunks of the assistant's response.
        """
        url = f"{self.base_url}/api-chat/stream"
        data = {
            "session_id": session_id,
            "prompt": prompt,
            "model": model
        }
        
        with requests.post(url, headers=self.headers, data=data, stream=True) as resp:
            if resp.status_code != 200:
                raise Exception(f"Chat request failed: {resp.status_code} - {resp.text}")
            
            for line in resp.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    # print(f"DEBUG: {decoded_line}") # Uncomment for debug
                    try:
                        json_obj = json.loads(decoded_line)
                        if json_obj.get("type") == "assistant":
                            content = json_obj.get("content")
                            if content:
                                yield content
                        elif json_obj.get("type") == "error":
                            raise Exception(f"API Error: {json_obj.get('content')}")
                    except json.JSONDecodeError:
                        pass
