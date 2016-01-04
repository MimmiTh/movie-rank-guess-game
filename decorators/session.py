from functools import wraps
from flask import g, request, redirect, url_for
from db import connect
from models import User

def _get_user_from_cookie():
	id = request.cookies.get('movie_quiz_user')
	if id is None:
		return None
	return User.from_id(id)

def require_login():
	@wraps(func)
	def decorated_function(*args, **kwargs):
		g.user = _get_user_from_cookie()
		if g.user is None:
			return redirect(url_for('index'))
		return func(*args, **kwargs)
	return decorated_function

def identify_or_create_user(func):
	@wraps(func)
	def decorated_function(*args, **kwargs):
		if getattr(g, 'user', None) is None:
			user = _get_user_from_cookie()
			if user is None:
				user = User.save()
			g.user = user
		return func(*args, **kwargs)
	return decorated_function