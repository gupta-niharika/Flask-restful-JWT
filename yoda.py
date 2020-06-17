from flask import Flask
from flask_bcrypt import Bcrypt 
from database.db import initialize_db
from flask_restful import Api 
from resources.routes import initialize_routes 
from flask_jwt_extended import jwt_required, JWTManager

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION') #environment variable which should store the location of .env file relative to yoda.py 
# run this on terminal : set ENV_FILE_LOCATION =.env


api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# movies = [
#     {
#         "name": "The Shawshank Redemption",
#         "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
#         "genres": ["Drama"]
#     },
#     {
#        "name": "The Godfather ",
#        "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
#        "genres": ["Crime", "Drama"]
#     }
# ]


app.config['MONGODB_SETTINGS'] = {
    'host' : 'mongodb://localhost/movie-bag'
}
initialize_db(app)

initialize_routes(api)

app.run()


# if __name__ == '__main__':
#     app.run(debug=True)