#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, g, make_response, request
import os
from decorators import require_login, identify_or_create_user
from models import Movie, Guess

app = Flask(__name__)
app.config.update(
	DATABASE_HOST=os.environ['DB_HOST'],
	DATABASE_PORT=os.environ['DB_PORT'],
	DATABASE_NAME=os.environ['DB_NAME'],
	DATABASE_USER=os.environ['DB_USER'],
	DATABASE_PASSWORD=os.environ['DB_PASSWORD']
	)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/movie', methods=['GET'])
@identify_or_create_user
def movie():
	resp = make_response(render_template('movie.html', movie=Movie.next_for_user(g.user)))
	resp.set_cookie('movie_quiz_user', str(g.user.id))
	return resp

@app.route('/answer', methods=['POST'])
@require_login
def answer():
	guess = Guess.save(request.form['guess'], g.user.id, request.form['movie'])
	return render_template('answer.html', movie=guess.movie, complete=(False if Movie.next_for_user(g.user) else True), guess=guess)

@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
	# If postdata - save name
	# Get leaderboard
	return render_template('leaderboard.html', users=users)

if __name__ == '__main__':
	app.run(debug=True)