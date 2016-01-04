from functools import wraps
from flask import g, request
from db import connect
from models import User

def _get_user_from_cookie():
	id = request.cookies.get('movie_quiz_user')
	if id is None:
		return None
	return User.from_id(id)

def identify_or_create_user(func):
	@wraps(func)
	def decorated_function(*args, **kwargs):
		if getattr(g, 'user', None) is None:
			user = _get_user_from_cookie()
			if user is None:
				user = User.create()
			g.user = user
		return func(*args, **kwargs)
	return decorated_function