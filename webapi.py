import random

from flask import Blueprint, jsonify

app_api = Blueprint('api', __name__,
                    url_prefix='/api',
                    template_folder='templates',
                    static_folder='static', static_url_path='static/api')

movie_data = []
movie_list = [

    "The movie Titanic, released in 1997, won 11 Oscars, including Best Picture. ",
    'During the making of Toy Story 2, 90% of the animation work got deleted on the master machine. Even the backups failed. Luckily, the director had a copy!'
    "In the Pixar movie 'Up', the animators created 10,297 balloons individually"
    "The character Chewbacca in Star Wars was inspired by George Lucas's dog!"
    "The green code from 'The Matrix' comes from symbols from a Sushi cookbook!"
    "'Cleopatra' was one of the most expensive movies ever made, amounting to over $370 million. "
    "Tony Stark's death scene in 'Endgame' was completely improvised"
]


def _init_movie():
    item_id = 1
    for item in movie_list:
        movie_data.append({"id": item_id, "movie": item,})
        item_id += 1


@app_api.route('/movie')
def movie():
    if len(movie_data) == 0:
        _init_movie()
    return jsonify(random.choice(movie_data))


@app_api.route('/movie')
def jokes():
    if len(movie_data) == 0:
        _init_movie()
    return jsonify(movie_data)


if __name__ == "__main__":
    print(random.choice(movie_list))