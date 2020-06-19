# Article ke sare routes idhar hai!

from flask import Blueprint, Response, request
from database.models import Article

articles = Blueprint('articles', __name__)

@articles.route('/articles', methods=['POST'])       #create article - C
def add_movie():
    body = request.get_json()
    article = Article(**body).save()          #collection = Class(**body).save() <-- syntax samajh lo
    id = article.id
    return 'article add ho gayi', 200


@articles.route('/articles')                 #view articles - R
def get_movies():
    articles = Article.objects().to_json()
    return Response(articles, mimetype="application/json", status=200)      #prints whatever is present in that colection


@articles.route('/articles/<id>', methods=['PUT'])           #iski zarurat nahi padegi - UPDATE
def update_movie(id):
    body = request.get_json()
    Article.objects.get(id=id).update(**body)
    return 'article update ho gayi', 200


@articles.route('/articles/<id>', methods=['DELETE'])        #Delete
def delete_movie(id):
    article = Article.objects.get(id=id).delete()
    return 'article delete ho gayi', 200
