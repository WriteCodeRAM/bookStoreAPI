from flask import Flask, jsonify
import mysql.connector
from commentsandratings import get_ratings, get_comments, get_average_rating
from users import get_users, get_user, create_user, update_user, add_credit_card

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

@app.route('/users/<username>', methods=['GET'])
def find_user(username):
    user = get_user(username)
    return user

@app.route('/users/create', methods=['POST'])
def new_user():
    return create_user()

@app.route('/users/update/<username>', methods=["PUT", "PATCH"])
def edit_user(username):
    return update_user(username)

@app.route('/users/<username>/creditcard/new', methods=["POST"])
def new_credit_card(username):
    return add_credit_card(username)


if __name__ == '__main__':
    app.run(debug=True)
