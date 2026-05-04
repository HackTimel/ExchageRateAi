import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from tools import get_exchange_rate

# Load secrets from the .env file
load_dotenv()

# Initialize the Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def start_interactive_chat():
    print("=== Financial AI Assistant ===")
    print("Type 'exit' or 'quit' to stop the program.\n")
    
    # Create the chat session once so it remembers the conversation context (gemini documentation)
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            tools=[get_exchange_rate], 
            temperature=0.0,   #i've put this setting to 0 to have more factual answers.           
        )
    )

    # Infinite loop to keep asking for user input
    while True:
        # Wait for the user to type something in the terminal
        user_query = input("You: ")
        
        # Check if the user wants to close the program
        if user_query.lower() in ['exit', 'quit', 'q']:
            print("Agent: Goodbye!")
            break # Breaks the loop and stops the program
            
        # Prevent sending empty messages
        if not user_query.strip():
            continue
            
        # Send the user's message to the AI and print the response
        try:
            response = chat.send_message(user_query)
            print(f"Agent: {response.text}\n")
        except Exception as e:
            print(f"System Error: {e}\n")

if __name__ == "__main__":
    start_interactive_chat()
