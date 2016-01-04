#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, g, make_response
import os
from decorators import session

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
@session.identify_or_create_user
def movie():
	resp = make_response(render_template('movie.html', movie=movie))
	resp.set_cookie('movie_quiz_user', str(g.user.id))
	return resp
	# Auth decorator - if user != exist create user
	# Get next movie from db

@app.route('/answer', methods=['POST'])
def answer():
	# Auth decorator - if user != exist redirect, if guess >9 leaderboard
	# Get movie by id
	# Save guess
	# Check nr of guesses - new movie or leaderboard
	return render_template('answer.html', movie=movie, complete=complete)

@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
	# If postdata - save name
	# Get leaderboard
	return render_template('leaderboard.html', users=users)

if __name__ == '__main__':
	app.run(debug=True)