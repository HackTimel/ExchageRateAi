import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from tools import get_exchange_rate, get_stock_value

# Load secrets from the .env file
load_dotenv()

# Initialize the Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

system_rules = (
        "You are a helpful financial assistant. "
        "critical rule: If a tool returns any kind of Error such as API Error, rate limit, "
        "missing key, or network issue, you must stop immediately. DO NOT call the tool again. "
        "Directly tell the user what the error was."
    )

def start_interactive_chat():
    print("=== Financial AI Assistant ===")
    print("Type 'exit' or 'quit' to stop the program.\n")
    
    # Create the chat session once so it remembers the conversation context (gemini documentation)
    chat = client.chats.create(
        model="gemini-3.1-flash-lite-preview",
        config=types.GenerateContentConfig(
            tools=[get_exchange_rate, get_stock_value], 
            temperature=0.0,   #i've put this setting to 0 to have more factual answers.
            system_instruction=system_rules
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
