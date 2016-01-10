from flask import current_app
import pymysql


def connect():
    '''Factory function to establish database connection'''
    return pymysql.connect(host=current_app.config['DATABASE_HOST'],
                           user=current_app.config['DATABASE_USER'],
                           password=current_app.config['DATABASE_PASSWORD'],
                           db=current_app.config['DATABASE_NAME'],
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
