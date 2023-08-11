from flask_app import app
from flask import render_template, request, session, redirect
import os
import requests
from pprint import pprint

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

    id = response.json()['results'][0]['id']
    url_two = f"https://superheroapi.com/api/{header}/{id}"
    response_two = requests.get(url_two)

    session['image'] = response_two.json()['image']['url']
    session['name'] = response_two.json()['name']
    session['powerstats'] = response_two.json()['powerstats']

    return redirect('/show/heroes/villains')