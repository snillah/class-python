# Lightweight: Flask has a small core and is easy to extend with additional libraries and tools as needed. 

# Routing: It features a simple and intuitive routing system that allows developers to map URLs to Python functions using decorators. 

# Template Engine: Flask uses Jinja2 as its templating engine, enabling dynamic HTML generation with variables and control structures. 

# WSGI Compliance: Flask is built on the Werkzeug WSGI toolkit, which provides a standard interface between web servers and web applications. 

# RESTful API Support: Flask is popular for building RESTful APIs, making it a great choice for web services. 

# Getting Started with Flask
# Installation: You can install Flask using pip:
pip install Flask
# Creating a Simple Application: Here’s a basic example of a Flask application:
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
return "Hello, World!"
if __name__ == "__main__":
app.run(debug=True)
# This code creates a simple web server that responds with "Hello, World!" when accessed. 
# PyPI

# Running the Application: Save the code in a file named app.py and run it using:
# python app.py