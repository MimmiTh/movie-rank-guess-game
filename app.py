#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, g, make_response, request
from pymysql.err import IntegrityError
from models import Movie, Guess, User
from decorators import (
    require_login,
    identify_user,
    identify_or_create_user,
    is_not_done
)

app = Flask(__name__)
app.config.from_object('config')

# Encrypt cookies
app.secret_key = app.config['SECRET_KEY']


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/movie', methods=['GET'])
@identify_or_create_user
@is_not_done
def movie():
    return render_template('movie.html', movie=Movie.next_for_user(g.user))


@app.route('/answer', methods=['POST'])
@require_login
def answer():
    # Prevent user from guessing twice on the same movie
    try:
        guess = Guess.save(
            request.form['guess'],
            g.user.id,
            request.form['movie']
        )
    except IntegrityError, e:
        return 'Du har redan gissat på den här filmen', 403

    return render_template(
        'answer.html',
        movie=guess.movie,
        complete=(False if Movie.next_for_user(g.user) else True),
        guess=guess
    )


@app.route('/leaderboard', methods=['GET', 'POST'])
@identify_user
def leaderboard():
    # Let user set their name
    if request.method == 'POST' and g.user:
        g.user.name = request.form['name']
        g.user.update()

    return render_template(
        'leaderboard.html',
        users=User.by_score(),
        score=g.user.score
    )

if __name__ == '__main__':
    app.run(debug=True)
