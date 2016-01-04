from db import connect

class Movie:
	def __init__(self, id, name, synopsis, poster, rating):
		self.id = id
		self.name = name
		self.synopsis = synopsis
		self.poster = poster
		self.rating = rating

	@staticmethod
	def from_id(id):
		connection = connect()
		try:
			with connection.cursor() as cursor:
				sql = "SELECT `id`, `name`, `synopsis`, `poster`, `rating` FROM `movies` WHERE `id`=%s"
				cursor.execute(sql, (id))
				movie = cursor.fetchone()
				
				if mpvie is None:
					return None

				return Movie(movie[u'id'], movie[u'name'], movie[u'synopsis'], movie[u'poster'], movie[u'rating'])
		finally:
			connection.close()

	@staticmethod
	def next_for_user(user):
		connection = connect()
		try:
			with connection.cursor() as cursor:
				sql = "SELECT * FROM `movies` WHERE `id` NOT IN (SELECT `movie_id` FROM `guesses` WHERE `user_id`=%s) LIMIT 1"
				cursor.execute(sql, (user.id))
				movie = cursor.fetchone()
				
				if movie is None:
					return None

				return Movie(movie[u'id'], movie[u'name'], movie[u'synopsis'], movie[u'poster'], movie[u'rating'])
		finally:
			connection.close()