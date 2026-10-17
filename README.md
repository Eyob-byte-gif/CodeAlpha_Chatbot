
# CodeAlpha Basic Chatbot

A simple rule-based chatbot built with Python for the CodeAlpha Python Programming Internship.

## Features

- Responds to greetings such as `hello` and `hi`
- Answers `how are you`
- Provides a fallback response for unknown messages
- Exits when the user types `bye`
- Uses a continuous conversation loop
- Includes automated tests using `unittest`

## Requirements

- Python 3
- No third-party packages required

## Run the Chatbot

```bash
python chatbot.py
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Project Structure

```text
CodeAlpha_Chatbot/
├── chatbot.py
├── README.md
└── tests/
    └── test_chatbot.py
```

## Concepts Demonstrated

Functions, conditionals, loops, strings, terminal input/output, and automated testing.

## Limitations

This is a rule-based chatbot. It responds to predefined phrases and does not use artificial intelligence or understand unrestricted natural language.

