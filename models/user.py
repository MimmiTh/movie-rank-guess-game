from db import connect

class User:
	def __init__(self, id, name=None, score=0):
		self.id = id
		self.name = name
		self.score = score

	def update(self):
		connection = connect()
		try:
			with connection.cursor() as cursor:
				sql = "UPDATE `users` SET `name`=%s, `score`=%s WHERE `id`=%s"
				cursor.execute(sql, (self.name, self.score, self.id))

			connection.commit()

		finally:
			connection.close()

	@staticmethod
	def save():
		connection = connect()
		try:
			with connection.cursor() as cursor:
				sql = "INSERT INTO `users` (score) VALUES (0)"
				result = cursor.execute(sql)
			
			connection.commit()

			return User.from_id(cursor.lastrowid)
		finally:
			connection.close()

	@staticmethod
	def from_id(id):
		connection = connect()
		try:
			with connection.cursor() as cursor:
				sql = "SELECT `id`, `name`, `score` FROM `users` WHERE `id`=%s"
				cursor.execute(sql, (id))
				user = cursor.fetchone()

				if user is None:
					return None

				return User(user[u'id'], user[u'name'], user[u'score'])
		finally:
			connection.close()

	@staticmethod
	def by_score(amount=10):
		connection = connect()
		try:
			with connection.cursor() as cursor:
				sql = "SELECT `id`, `name`, `score` FROM `users` WHERE `score`>0 AND `name` != '' ORDER BY `score` DESC LIMIT %s"
				cursor.execute(sql, (amount))
				return [User(user[u'id'], user[u'name'], user[u'score']) for user in cursor.fetchall()]
		finally:
			connection.close()