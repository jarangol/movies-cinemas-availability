from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
  return 'Web App with Python Flask!'

@app.route('/cinemas')
def getCinemas():
  url = "http://159.122.183.100:32341/api/v1.0/films/"
  response = requests.get(url)
  movies_json = response.json()
  cinemas = {}
  for movie in movies_json:
    for cinema in movie['cines']:
      cinema_id = cinema['id']
      if (cinema_id not in cinemas):
        cinemas[cinema_id] = {
          'name': cinema['name'],
          'id': cinema_id,
          'address': cinema['adress'],
          'movies': [movie]
        }
      else:
        cinemas[cinema_id]['movies'].append(movie)

  return cinemas

app.run(host='0.0.0.0', port=3080)
