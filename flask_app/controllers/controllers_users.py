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

    # Appearance
    session['image'] = response_two.json()['image']['url']
    session['name'] = response_two.json()['name']
    session['gender'] = response_two.json()['appearance']['gender']
    session['race'] = response_two.json()['appearance']['race']
    session['height'] = response_two.json()['appearance']['height'][0]
    session['cm'] = response_two.json()['appearance']['height'][1]
    session['weight'] = response_two.json()['appearance']['weight'][0]
    session['kilograms'] = response_two.json()['appearance']['weight'][1]
    session['eye_color'] = response_two.json()['appearance']['eye-color']
    session['hair_color'] = response_two.json()['appearance']['hair-color']
    # End of Appearance

    # Biography
    session['full_name'] = response_two.json()['biography']['full-name']
    session['alter_egos'] = response_two.json()['biography']['alter-egos']
    session['aliases'] = response_two.json()['biography']['aliases'] # needs for loop
    session['place_of_birth'] = response_two.json()['biography']['place-of-birth']
    session['base'] = response_two.json()['work']['base']
    session['occupation'] = response_two.json()['work']['occupation']
    session['first_appearance'] = response_two.json()['biography']['first-appearance']
    session['publisher'] = response_two.json()['biography']['publisher']
    session['alignment'] = response_two.json()['biography']['alignment']
    # End of Biography

    # Connections
    session['group_affiliation'] = response_two.json()['connections']['group-affiliation']
    session['relatives'] = response_two.json()['connections']['relatives']
    # End of Connections

    # Powerstats
    session['intelligence'] = response_two.json()['powerstats']['intelligence']
    session['strength'] = response_two.json()['powerstats']['strength']
    session['speedd'] = response_two.json()['powerstats']['speed']
    session['durability'] = response_two.json()['powerstats']['durability']
    session['power'] = response_two.json()['powerstats']['power']
    session['combat'] = response_two.json()['powerstats']['combat']
    # End of Powerstats

    return redirect('/show/heroes/villains')