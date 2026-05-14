import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools import get_exchange_rate, get_stock_value


class TestGetExchangeRate(unittest.TestCase):

    @patch("tools.os.getenv", return_value="fake_api_key")
    @patch("tools.requests.get")
    def test_successful_conversion(self, mock_get, mock_env):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "result": "success",
            "conversion_rate": 1.08,
            "conversion_result": 108.0,
        }
        mock_get.return_value = mock_response

        result = get_exchange_rate(100, "EUR", "USD")

        self.assertIn("108.0", result)
        self.assertIn("EUR", result)
        self.assertIn("USD", result)

    @patch("tools.os.getenv", return_value="fake_api_key")
    @patch("tools.requests.get")
    def test_api_error(self, mock_get, mock_env):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "result": "error",
            "error-type": "unsupported-code",
        }
        mock_get.return_value = mock_response

        result = get_exchange_rate(100, "XXX", "USD")

        self.assertIn("Error", result)

    @patch("tools.os.getenv", return_value=None)
    def test_missing_api_key(self, mock_env):
        result = get_exchange_rate(100, "EUR", "USD")
        self.assertIn("missing", result.lower())

    @patch("tools.os.getenv", return_value="fake_api_key")
    @patch("tools.requests.get")
    def test_network_error(self, mock_get, mock_env):
        import requests
        mock_get.side_effect = requests.exceptions.RequestException("timeout")

        result = get_exchange_rate(100, "EUR", "USD")

        self.assertIn("Network", result)

    def test_input_validation(self):
        self.assertIn("Error", get_exchange_rate(-50, "EUR", "USD"))
        self.assertIn("Error", get_exchange_rate(100, "EU", "USD"))
        self.assertIn("Error", get_exchange_rate(100, "", "USD"))


class TestGetStockValue(unittest.TestCase):

    @patch("tools.os.getenv", return_value="fake_api_key")
    @patch("tools.requests.get")
    def test_successful_lookup(self, mock_get, mock_env):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "Time Series (Daily)": {
                "2024-01-15": {
                    "4. close": "153.50",
                }
            }
        }
        mock_get.return_value = mock_response

        result = get_stock_value("AAPL")

        self.assertIn("153.50", result)
        self.assertIn("AAPL", result)

    @patch("tools.os.getenv", return_value="fake_api_key")
    @patch("tools.requests.get")
    def test_invalid_symbol(self, mock_get, mock_env):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "Error Message": "Invalid API call."
        }
        mock_get.return_value = mock_response

        result = get_stock_value("INVALID_XYZ")

        self.assertIn("Error", result)

    @patch("tools.os.getenv", return_value=None)
    def test_missing_api_key(self, mock_env):
        result = get_stock_value("AAPL")
        self.assertIn("missing", result.lower())

    @patch("tools.os.getenv", return_value="fake_api_key")
    @patch("tools.requests.get")
    def test_network_error(self, mock_get, mock_env):
        import requests
        mock_get.side_effect = requests.exceptions.RequestException("connection refused")

        result = get_stock_value("AAPL")

        self.assertIn("Network", result)

    def test_empty_symbol_validation(self):
        self.assertIn("Error", get_stock_value(""))
        self.assertIn("Error", get_stock_value("   "))


if __name__ == "__main__":
    unittest.main(verbosity=2)
