import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestAgentWorkflow(unittest.TestCase):

    @patch("main.client")
    def test_agent_exits_on_quit(self, mock_client):
        mock_chat = MagicMock()
        mock_client.chats.create.return_value = mock_chat

        from main import start_interactive_chat

        with patch("builtins.input", side_effect=["quit"]):
            with patch("builtins.print"):
                start_interactive_chat()

        mock_chat.send_message.assert_not_called()

    @patch("main.client")
    def test_agent_handles_api_exception(self, mock_client):
        mock_chat = MagicMock()
        mock_chat.send_message.side_effect = Exception("Gemini unavailable")
        mock_client.chats.create.return_value = mock_chat

        from main import start_interactive_chat

        printed = []
        with patch("builtins.input", side_effect=["what is AAPL stock price?", "exit"]):
            with patch("builtins.print", side_effect=lambda *a: printed.append(str(a))):
                start_interactive_chat()

        self.assertIn("Error", " ".join(printed))


if __name__ == "__main__":
    unittest.main(verbosity=2)
