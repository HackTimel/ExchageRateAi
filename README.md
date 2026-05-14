# Financial AI Assistant (Agent-Based System)

A Python-based intelligent agent that uses external tools to answer financial queries in natural language. Powered by the Gemini LLM (Flash Lite), this assistant dynamically decides when to call external Python functions to fetch live data.

## Features & Tools

This agent is equipped with 2 specific tools:
1. **Currency Converter ([ExchangeRate-API](https://www.exchangerate-api.com/))**: Converts amounts between global currencies using live rates.
2. **Stock Market Tracker ([Alpha Vantage API](https://www.alphavantage.co/)**: Fetches the latest daily closing price for global equities.


## Tech Stack
- **Language:** Python 3
- **AI Model:** Google Gemini 3.1 Flash Lite (google-genai SDK)
- **Environment Management:** python-dotenv for secure API key storage
- **Network Requests:** requests library for REST APIs

### Prerequisites
You need Python installed on your computer and API keys for Google Gemini, ExchangeRate-API, and Alpha Vantage.

### 1. Clone the repository

```
git clone https://github.com/HackTimel/ExchageRateAi.git
```


### 2. Set up the Virtual Environment

# On Windows
```
python -m venv venv
```
```
venv\Scripts\activate
```
# On macOS / Linux
```
python3 -m venv venv
```
```
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```


### 4. Setup Environment Variables

Create a file named .env in the root folder of the project. Add your API keys inside:

```
GEMINI_API_KEY=your_gemini_key_here
EXCHANGERATE_API_KEY=your_exchangerate_key_here
STOCK_VALUE_API=your_alphavantage_key_here
```


### 5. Run the Agent

Start the interactive terminal session by running:

```
python main.py
```

You can now chat with the AI! Type quit, exit or q to stop the program. 


### 6. Run the Tests

Navigate to the tests folder and run either test file with pytest:

```
cd tests
```
```
pytest test_tools.py
```
```
pytest test_integration.py
```

No API keys are required to run the tests, all external API calls are mocked.
