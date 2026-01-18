# Python Factorial Calculator

A simple Python application that calculates the factorial of a given number.

## Usage

Run the application with a command-line argument:

```bash
python main.py <number>
```

For example:

```bash
python main.py 5
```

Output:
```
The factorial of 5 is 120
```

## Testing

To run the tests, use pytest:

```bash
pytest
```

## GitHub Actions

This project includes a GitHub Actions workflow that runs on every push and pull request to the main branch. The workflow:

- Sets up Python 3.9
- Installs dependencies
- Runs the tests
- Runs the application with an example input

## Requirements

- Python 3.6+
- pytest (for testing)

Install dependencies:

```bash
pip install -r requirements.txt
```

## Troubleshooting

- Ensure Python is installed and in your PATH.
- For testing, make sure pytest is installed.
- If running on GitHub Actions, check the workflow logs for any errors.