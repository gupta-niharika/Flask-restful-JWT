from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Movie
import json

app = Flask(__name__)

app.config['MONGODB_HOST'] = 'mongodb://admin:admin@cluster0-shard-00-00-iim6b.mongodb.net:27017,cluster0-shard-00-01-iim6b.mongodb.net:27017,cluster0-shard-00-02-iim6b.mongodb.net:27017/MSTC?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
app.config['MONGODB_DB'] = 'MSTC'
initialize_db(app)

@app.route('/movies')
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)


@app.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return 'movie added', 200

@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return 'movie updated', 200

@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.objects.get(id=id).delete()
    return 'movie deleted', 200

app.run()
