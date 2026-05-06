# Financial AI Assistant (Agent-Based System)

A Python-based intelligent agent that uses external tools to answer financial queries in natural language. Powered by the Gemini LLM (Flash Lite), this assistant dynamically decides when to call external Python functions to fetch live data.

## Features & Tools

This agent is equipped with 2 specific tools:
1. **Currency Converter (ExchangeRate-API)**: Converts amounts between global currencies using live rates.
2. **Stock Market Tracker (Alpha Vantage API)**: Fetches the latest daily closing price for global equities.


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
python -m venv venv
venv\Scripts\activate

# On macOS / Linux
python3 -m venv venv
source venv/bin/activate
