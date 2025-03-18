# Define the correct paths for pip and python
PIP = .venv\Scripts\pip.exe
PYTHON = .venv\Scripts\python.exe

# Variables
VENV = venv
ENTRY = main.py
OUTPUT = dist\main

# Create a virtual environment
venv:
	$(PYTHON) -m venv $(VENV)

# Install dependencies
install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run the Flask app
run: install
	$(PYTHON) $(ENTRY)

# Run tests using pytest
test:
	$(PYTHON) -m pytest tests

# Lint code using flake8
lint:
	$(PIP) install flake8
	flake8 .

# Format code using Black
format:
	$(PIP) install black
	$(PYTHON) -m black .

# Check for unused imports using autoflake
unused:
	$(PIP) install autoflake
	$(PYTHON) -m autoflake --remove-all-unused-imports --in-place --recursive .

# Create an executable using PyInstaller
build: install
	$(PIP) install pyinstaller
	pyinstaller --onefile --name=main $(ENTRY)

# Clean up build files
clean:
	rmdir /s /q __pycache__ $(VENV) build dist

# Remove only the generated executable
clean-build:
	rmdir /s /q build dist

# Reinstall everything from scratch
reinstall: clean install

.PHONY: venv install run test lint format build clean clean-build reinstall