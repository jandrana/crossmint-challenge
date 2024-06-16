# Coding Challenge | Crossmint | Internship
This repository contains my solution for a coding challenge as part of Crossmint's Internship program.

## Project Structure

```bash
crossmint-challenge/
├── 📁src
│ ├── main.py
│ ├── api_interactions.py   # API interactions
│ ├── astral_objects.py     # Definition of astral objects using subclasses
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
