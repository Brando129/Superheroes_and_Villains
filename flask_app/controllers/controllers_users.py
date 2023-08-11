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
    # url = f"https://superheroapi.com/api/{header}/{id}"
    response = requests.get(url)

    # session['id'] = response.json()['results'][0]['id']
    # session['image'] = response.json()['results'][0]['image']
    # pprint(session['id'])
    # pprint(session['image'])
    id = response.json()['results'][0]['id']
    url_two = f"https://superheroapi.com/api/{header}/{id}"
    response_two = requests.get(url_two)

    # session['image'] = f"https://superheroapi.com/api/{header}/{id}/image"
    session['image'] = response_two.json()['image']['url']
    session['name'] = response_two.json()['name']
    session['powerstats'] = response_two.json()['powerstats']
    print(session['image'])

    return redirect('/show/heroes/villains')