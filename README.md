# Student Message Generator

This Python script, `write_messages.py`, generates personalized messages for each student based on their score in a given test and also generates a results page listing all students and their respective scores. The script utilizes the Jinja2 templating engine for rendering the messages from templates.

## Features

- Generates individual text files with personalized messages for each student.
- Creates an HTML results page summarizing the test scores of all students.
- Utilizes Jinja2 templates for easy customization of message and results formats.

## Requirements

- Python 3.6 or higher
- Jinja2

## Installation

To set up the script on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-message-generator.git
   cd student-message-generator
   
Install the required Python package:

pip install Jinja2
Usage
To run the script, execute the following command in the terminal:

python write_messages.py
Upon execution, the script will:

Create individual text files for each student containing their personalized message.
Generate an HTML file (students_results.html) that lists all students along with their scores.
Templates
The templates used by the script are located in the templates/ directory. The following templates are currently used:

message.txt: Template for individual student messages.
results.html: Template for the HTML results page.
You can modify these templates to change the format and content of the generated messages and results page.

This README template gives an overview of the project, explains how to install and run
