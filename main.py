from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print("Hello from LangChain!")
    print("API Key loaded:",os.environ.get("OPENAI_API_KEY"))

if __name__ == "__main__":
    main()
