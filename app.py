from flask import Flask, Blueprint, render_template, request, jsonify, abort
from utils import get_movie_by_title, get_movie_by_years, get_movie_by_rating_child, get_movie_by_rating_family, \
    get_movie_by_rating_adult, get_movie_genre

app = Flask(__name__)


@app.route("/movie/<title>/")
def search_by_title(title):
    film = get_movie_by_title(title)
    return jsonify(film)


@app.route("/movie/<int:first_year>/to/<int:second_year>/")
def search_by_years(first_year, second_year):
    films = get_movie_by_years(first_year, second_year)
    return jsonify(films)


@app.route("/rating/children")
def get_movie_by_child():
    films = get_movie_by_rating_child()
    return jsonify(films)


@app.route("/rating/family")
def get_movie_by_family():
    films = get_movie_by_rating_family()
    return jsonify(films)


@app.route("/rating/adult")
def get_movie_by_adult():
    films = get_movie_by_rating_adult()
    return jsonify(films)


@app.route("/genre/<genre>")
def get_movie_by_genre(genre):
    films = get_movie_genre(genre)
    return jsonify(films)

if __name__ == "__main__":

        app.run()