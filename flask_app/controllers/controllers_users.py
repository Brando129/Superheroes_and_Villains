from flask_app import app
from flask import render_template
import os
import requests

# API Key
header = os.environ.get('KEY')

# Route for rendering the Home Page.
@app.get('/')
def index():
    return render_template('homepage.html')