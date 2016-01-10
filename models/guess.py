from db import connect
from models import Movie, User

# Maximum difference between incorrect guess and ranking
MAX_DIFF = 8


class Guess:
    '''Represents guess on movie ranking'''
    def __init__(self, id, guess, user, movie):
        self.id = id
        self.guess = guess
        self.user = user
        self.movie = movie

    '''Checks if guess is correct'''
    def is_correct(self):
        return int(self.movie.rating) is int(self.guess)

    '''Creates new guess'''
    @staticmethod
    def save(guess, user_id, movie_id):
        user = User.from_id(user_id)
        rating = Movie.from_id(movie_id).rating
        guess_id = None

        connection = connect()
        try:
            with connection.cursor() as cursor:
                sql = """INSERT INTO `guesses` (guess, user_id, movie_id, diff)
                    VALUES (%s, %s, %s, %s)"""
                cursor.execute(
                    sql,
                    (
                        guess,
                        user_id,
                        movie_id,
                        Guess.calculate_score(rating, guess)
                    )
                )
                guess_id = cursor.lastrowid

                sql = """SELECT SUM(`diff`) AS score
                    FROM `guesses` WHERE `user_id`=%s"""
                cursor.execute(sql, (user_id))
                result = cursor.fetchone()

                user.score = result[u'score']

            connection.commit()

        finally:
            connection.close()

        user.update()
        return Guess.from_id(guess_id)

    '''Calculates score to be added to user total score'''
    @staticmethod
    def calculate_score(rating, guess):
        return MAX_DIFF - abs(rating - int(guess))

    '''Gets guess by ID'''
    @staticmethod
    def from_id(id):
        connection = connect()
        try:
            with connection.cursor() as cursor:
                # Gets guess with associated user and movie
                sql = """SELECT
                    `guesses`.`id` AS guess_id,
                    `guesses`.`guess`,
                    `users`.`id` AS user_id,
                    `users`.`name` AS user_name,
                    `users`.`score`,
                    `movies`.`id` AS movie_id,
                    `movies`.`name` AS movie_name,
                    `movies`.`synopsis`,
                    `movies`.`poster`,
                    `movies`.`rating` FROM `guesses`
                    INNER JOIN `users` on `guesses`.`user_id` = `users`.`id`
                    INNER JOIN `movies` on `guesses`.`movie_id` = `movies`.`id`
                    WHERE `guesses`.`id` = %s"""
                cursor.execute(sql, (id))
                data = cursor.fetchone()

                if data is None:
                    return None

                return Guess(
                    data[u'guess_id'],
                    data[u'guess'],
                    User(
                        data[u'user_id'],
                        data[u'user_name'],
                        data[u'score']
                    ),
                    Movie(
                        data[u'movie_id'],
                        data[u'movie_name'],
                        data[u'synopsis'],
                        data[u'poster'],
                        data[u'rating']
                    )
                )
        finally:
            connection.close()
