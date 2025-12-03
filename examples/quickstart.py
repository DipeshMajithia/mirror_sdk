from mirror_sdk import MirrorClient
import sys

# Replace with your actual API key
API_KEY = "iufvqK9h90yW9YtrZW_Wr_wcfzQ7d_iYCdlvLTYC84M"
BASE_URL = "http://localhost:807"

def main():
    print("Initializing Mirror Client...")
    client = MirrorClient(api_key=API_KEY, base_url=BASE_URL)

    try:
        # 1. Create Session
        print("Creating session...")
        session = client.create_session()
        session_id = session["id"]
        print(f"Session created: {session_id}")

        # 2. Chat
        prompt = "Hello, tell me a short joke."
        print(f"\nUser: {prompt}")
        print("Assistant: ", end="", flush=True)

        for chunk in client.chat(session_id, prompt):
            print(chunk, end="", flush=True)
        
        print("\n\nDone!")

    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
