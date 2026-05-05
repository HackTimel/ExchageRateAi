import os
import requests

def get_exchange_rate(amount: float, base_currency: str, target_currency: str) -> str:
    """
    Converts an amount from one currency to another using the ExchangeRate-API 'pair' endpoint.
    """

    print(f"\n[🔧 OUTIL PYTHON DÉCLENCHÉ] Le commis va chercher le taux pour {amount} {base_currency} vers {target_currency}...")#other way of testing if the agent is using the tool.

    # Retrieve the API key from the environment variables
    api_key = os.getenv("EXCHANGERATE_API_KEY")

    if not api_key:
        return "System error: The ExchangeRate API key is missing please add yours in the .env file"

    # Use the 'pair' endpoint which directly takes the currencies and the amount
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}/{amount}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Check if the API request was successful
        if data.get('result') == 'success':
            rate = data.get('conversion_rate')
            converted_amount = data.get('conversion_result')

            return f"{amount} {base_currency} equals {converted_amount} {target_currency} (Rate: {rate})."
        else:
            # Handle specific API errors (e.g., unsupported-code)
            error_type = data.get('error-type', 'Unknown error')
            return f"API Error: {error_type}"

    except requests.exceptions.RequestException as e:
        return f"Network connection error to the exchange API: {str(e)}"


'''

this was the test to see if the ai agent is really using the tool get exchange rate. It works by giving false result in any cases so i can see if the agent used the tool.
def get_exchange_rate(amount: float, base_currency: str, target_currency: str) -> str:
    # On court-circuite l'API pour le test :
    return f"{amount} {base_currency} equals 999999999 {target_currency}. The sky is purple today."
'''




def get_stock_value(stock_symbol : str) -> int:

    print("tool used")
    api_key = os.getenv("STOCK_VALUE_API")
    if not api_key:
        return "System error: The ExchangeRate API key is missing please add yours in the .env file"

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}"


    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Check if the API returned an error message
        if "Error Message" in data:
            return f"API Error: Invalid stock symbol ({stock_symbol})."
            
        # Check if we hit the free API rate limit
        if "Information" in data and "rate limit" in data["Information"].lower():
            return "API Error: Alpha Vantage rate limit reached. Please wait a moment."
            
        # Access the time series data
        time_series = data.get("Time Series (Daily)")
        if not time_series:
            return "Error: Could not retrieve time series data."
            
        # The JSON keys are dates so we can just get the first one 
        latest_date = list(time_series.keys())[0]
        
        # Extract the closing price
        latest_data = time_series[latest_date]
        closing_price = latest_data.get("4. close")
        
        return f"The latest closing price for {stock_symbol} on {latest_date} is ${closing_price}."
        
    except requests.exceptions.RequestException as e:
        return f"Network connection error to the stock API: {str(e)}"















