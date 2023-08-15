from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.controllers import controllers_users
from flask import flash
import os
import requests
from playsound import playsound
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
    aliases = controllers_users.session['aliases']
    return render_template('show_heroes_and_villains.html', aliases=aliases)

# Post Routes
# Route to search for a being.
@app.post('/search/heroes/villains')
def search_heroes_and_villains():

    # URl for searching a name that returns an id. The id carries all the beings data.
    name = request.form['name']
    url = f"https://superheroapi.com/api/{header}/search/{name}"
    response = requests.get(url)

    # Validaton for searching a being.
    if 'results' not in response.json():
        flash("No records found", "h_and_v")
        return redirect('/')
    else:
        """This second Url injects the id that is returned from the search
        and gets all of the beings data"""
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
    if response_two.json()['biography']['aliases'] == ['-']:
        session['aliases'] = ['No known aliases']
    else:
        session['aliases'] = response_two.json()['biography']['aliases']
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
    session['speed'] = response_two.json()['powerstats']['speed']
    session['durability'] = response_two.json()['powerstats']['durability']
    session['power'] = response_two.json()['powerstats']['power']
    session['combat'] = response_two.json()['powerstats']['combat']
    # End of Powerstats

    # Total Power
    intelligence = int(session['intelligence'])
    strength = int(session['strength'])
    speed = int(session['speed'])
    durability = int(session['durability'])
    power = int(session['power'])
    combat = int(session['combat'])
    sum = intelligence + strength + speed + durability + power + combat
    session['total_power'] = sum
    # if session['total_power'] > 500:
    #     playsound('', block=False)
    # else:
    #     pass
    # print(f"Total power = {session['total_power']}")
    # End of total Power

    return redirect('/show/heroes/villains')