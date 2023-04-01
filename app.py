from flask import Flask
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return 'Web App with Python Flask!'

@app.route('/cinemas', methods=['GET'])
def getCinemas():
  url = "http://159.122.183.100:32341/api/v1.0/films/"
  response = requests.get(url)
  movies_json = response.json()
  cinemas = []
  added_cinemas = set()

  for movie in movies_json:
    for cinema in movie['cines']:
      if (cinema['id'] not in added_cinemas):
        added_cinemas.add(cinema['id'])
        cinemas.append(cinema)
  return cinemas

@app.route('/cinemas/<id>/movies', methods=['GET'])
def getCinemaMovies(id):
  url = "http://159.122.183.100:32341/api/v1.0/films/"
  response = requests.get(url)
  movies_json = response.json()
  cinema_movies = []
  for movie in movies_json:
    for cinema in movie['cines']:
      if (cinema['id'] == int(id)):
        cinema_movies.append(movie)
  return cinema_movies

app.run(host='0.0.0.0', port=3080)
