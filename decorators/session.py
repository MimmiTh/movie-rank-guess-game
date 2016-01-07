from functools import wraps
from flask import g, request, redirect, url_for, session
from db import connect
from models import User

def _get_user_from_cookie():
	try:
		return User.from_id(session[u'user_id'])
	except KeyError, e:
		return None

def require_login(func):
	@wraps(func)
	def decorated_function(*args, **kwargs):
		g.user = _get_user_from_cookie()
		if g.user is None:
			return redirect(url_for('index'))
		return func(*args, **kwargs)
	return decorated_function

def identify_user(func):
	@wraps(func)
	def decorated_function(*args, **kwargs):
		if getattr(g, 'user', None) is None:
			g.user = _get_user_from_cookie()
		return func(*args, **kwargs)
	return decorated_function

def identify_or_create_user(func):
	@wraps(func)
	def decorated_function(*args, **kwargs):
		if getattr(g, 'user', None) is None:
			user = _get_user_from_cookie()
			if user is None:
				user = User.save()
				session[u'user_id'] = user.id
			g.user = user
		return func(*args, **kwargs)
	return decorated_function