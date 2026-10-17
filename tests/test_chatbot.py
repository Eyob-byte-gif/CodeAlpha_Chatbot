
import unittest
from unittest.mock import patch
from io import StringIO

from chatbot import chatbot


class TestChatbot(unittest.TestCase):

    @patch("builtins.input", side_effect=["hello", "bye"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_hello_response(self, mock_stdout, mock_input):
        chatbot()
        output = mock_stdout.getvalue()
        self.assertIn("Bot: Hello! How can I help you?", output)

    @patch("builtins.input", side_effect=["how are you", "bye"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_how_are_you_response(self, mock_stdout, mock_input):
        chatbot()
        output = mock_stdout.getvalue()
        self.assertIn(
            "Bot: I'm doing well! Thanks for asking.",
            output
        )

    @patch("builtins.input", side_effect=["unknown message", "bye"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_unknown_message(self, mock_stdout, mock_input):
        chatbot()
        output = mock_stdout.getvalue()
        self.assertIn("Bot: Sorry, I don't understand that.", output)

    @patch("builtins.input", side_effect=["bye"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_bye_exits_chatbot(self, mock_stdout, mock_input):
        chatbot()
        output = mock_stdout.getvalue()
        self.assertIn("Bot: Goodbye! Have a great day!", output)


if __name__ == "__main__":
    unittest.main()

