from flask import Flask, jsonify
import mysql.connector
from commentsandratings import get_ratings, get_comments, get_average_rating
from users import get_users

app = Flask(__name__)


@app.route('/ratings', methods=['GET'])
def get_rating():
    ratings = get_ratings()
    return ratings


@app.route('/comments', methods=['GET'])
def get_comment():
    comments = get_comments()
    return comments


@app.route('/average_rating', methods=['GET'])
def avg_rating():
    avg_rate = get_average_rating()
    return avg_rate


@app.route('/users', methods=['GET'])
def all_users():
    users = get_users()
    return users


if __name__ == '__main__':
    app.run(debug=True)
