# Coding Challenge | Crossmint | Internship
This repository contains my solution for a coding challenge as part of Crossmint's Internship program.

## Project Structure

```plaintext
crossmint-challenge/
├── 📁src
│ ├── main.py
│ ├── api_interactions.py   # API interactions
│ ├── astral_objects.py     # Definition of astral objects using subclasses
│ ├── utils.py     			# Util functions for development
├── 📁docs
│ ├── 📁build
│ │ ├── 📁html				# HTML documentation files ✨
│ │ │ ├── (HTML documentation files)
│ └── (...)
├── .env.template           # Template for environment variables
├── requirements.txt        # Python package dependencies
├── .gitignore
└── README.md
```

## Setup

1. Clone the repository and install the required packages:
	```bash
	git clone https://github.com/jandrana/crossmint-challenge && cd crossmint-challenge && pip install -r requirements.txt
	```

2. Configure environment variables
	- Copy the `.env.template` to a new `.env` file
		```bash
		cp .env.template .env
		```
	- Edit and fill the `.env` file with the correct values

## Running Instructions

To run the application:
```bash
python src/main.py
```

## Documentation

This project uses Sphinx to generate documentation from the Google-style docstrings added in the code.

### View Documentation

If you want to view the documentation, open the [`index.html`](docs/build/html) file in your browser.

### Updating the Documentation

To update/create the documentation, run the following command in the project's root directory:

```bash
cd docs && sphinx-apidoc -o source ../src && make html
```

This command builds the HTML documentation from the docstrings added in the application  