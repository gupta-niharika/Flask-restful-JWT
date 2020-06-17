from flask import Response,request
from database.models import Movie, User
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


class MoviesApi(Resource):
    def get(self):    #Retrieve
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required
    def post(self):     #Create
        user_id = get_jwt_identity()
        body = request.get_json()
        #movie = Movie(**body).save()
        user = User.objects.get(id=user_id)
        movie = Movie(**body, added_by=user)
        movie.save()

        id = movie.id 
        return {'id': str(id)}, 200


class MovieApi(Resource):
    @jwt_required
    def put(self, id):      #Update
        user_id = get_jwt_identity()
        movie = Movie.objects.get(id=id, added_by = user_id)
        body = request.get_json()
        Movie.objects.get(id=id).update(**body)
        #movie = Movie(**body, added_by=user_id)
        #movie.save()
        return 'update ho gaya', 200
    
    @jwt_required
    def delete(self, id):       #Delete
        #movie = Movie.objects.get(id=id).delete()
        user_id = get_jwt_identity()
        movie = Movie.objects.get(id=id, added_by = user_id)
        movie.delete()
        return 'delete ho gaya', 200
    
    def get(self, id):
        movies = Movie.objects.get(id=id).to_json()
        return Response(movies, mimetype="application/json", status=200)


