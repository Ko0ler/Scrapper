# Scrapper

## Extraction Tool

The Extraction Tool, called Scrapper, is a Python-based application that allows users to extract and process web content from a given URL. It's written with Object Oriented model, follows the Model-View-Controller (MVC) architecture, and provides a command-line interface for interaction.

## Usage

1. Easy step : use the .exe file in the dist directory
2. Manual step :
   - Fork the project, but only main.py file and mvc folder are required
   - Open your terminal, and make sure you have Python 3.10 or above installed
   - Install the required packages from requirements.txt using pip : pip install -r requirements.txt
   - Run the file main.py and follow the instructions : python main.py

## Features

- Extracts source code or specific content (title, text, link, image) from a web page
- Supports saving the extracted content in various formats (txt, html, XML)
- Validates user input and handles errors gracefully
- Provides options for retrying or quitting the extraction process

## Future features

- Best-suited algorithm for Checking extraction eligibility and authorization before processing
- Cross-platform GUI app (maybe with PyQt), for user interaction and accessibility

## License
This project is licensed under the MIT License.
