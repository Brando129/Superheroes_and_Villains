from flask_app import app
from flask import render_template, request, session, redirect
import os
import requests

# API Key
header = os.environ.get('KEY')

# Get Routes
# Route for rendering the Home Page.
@app.get('/')
def index():
    return render_template('homepage.html')

# Route for rendering Show heroes and villains page.
@app.get('/show/heroes/villains')
def show_heroes_and_villains():
    return render_template('show_heroes_and_villains.html')

# Post Routes
@app.post('/search/heroes/villains')
def search_heroes_and_villains():
    name = request.form['name']
    url = f"https://superheroapi.com/api/{header}/search/{name}"
    response = requests.get(url)

    session['name'] = response.json()['name']
    return redirect('/show/heroes/villains')