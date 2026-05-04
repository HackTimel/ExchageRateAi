import os
import requests

def get_exchange_rate(amount: float, base_currency: str, target_currency: str) -> str:
    """
    Converts an amount from one currency to another using the ExchangeRate-API 'pair' endpoint.
    """
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




