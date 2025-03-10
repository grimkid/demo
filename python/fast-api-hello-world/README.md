# FastAPI Hello World

A simple FastAPI application demonstrating basic setup and usage.

## Prerequisites

- Python 3.8.1 or higher
- Poetry (Python package manager)
- Just (Command runner)

## Quick Start

### 1. Project Setup

```bash
# Install just (if not already installed)
# On Ubuntu/Debian:
sudo apt-get install just

# On macOS:
brew install just

# Clone the repository
git clone <your-repository-url>
cd fast-api-hello-world

# Install Poetry (if not already installed)
curl -sSL https://install.python-poetry.org | python3 -

# Setup the project
just setup
```

### 2. Development Commands

We use `just` as our task runner. Available commands:

```bash
just                 # List all available commands
just setup          # Install project dependencies
just activate       # Activate the virtual environment (uses python3)
just dev            # Run the development server
just fmt            # Format code with black
just lint           # Run linter
just test           # Run tests
just clean          # Clean up cache files
just info           # Show Python and environment information
```

### 3. Running the Application

```bash
# First time setup:
just setup          # Install dependencies
just activate       # Activate virtual environment

# Start the server:
just dev            # Starts the development server
```

The server will start at `http://localhost:8000`

## API Documentation

- Interactive API docs (Swagger UI): `http://localhost:8000/docs`
- Alternative API docs (ReDoc): `http://localhost:8000/redoc`

## Project Structure
```
fast-api-hello-world/
├── app/
│   ├── __init__.py    # Package initialization
│   └── main.py        # Main application file
├── pyproject.toml     # Project dependencies and metadata
├── justfile          # Task runner commands
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Troubleshooting

If you encounter any issues:

1. Check your Python version:
```bash
python3 --version  # Should be 3.8.1 or higher
```

2. Check environment info:
```bash
just info  # Shows Poetry and Python environment details
```

3. Make sure you're in the project directory when running commands

## Development

### Development Commands

- Format code:
```bash
black .
```

- Run linter:
```bash
flake8
```

- Run tests:
```bash
pytest
```

## Adding New Dependencies

To add new project dependencies:
```bash
poetry add package-name
```

For development-only dependencies:
```bash
poetry add --group dev package-name
``` 