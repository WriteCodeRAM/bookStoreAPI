from flask import Flask
from flask_cors import CORS
from commentsandratings import get_ratings, get_comments, get_average_rating, rate_books, comment

app = Flask(__name__)
CORS(app)


@app.route('/ratings', methods=['GET'])
def get_rating():
    ratings = get_ratings()
    return ratings


@app.route('/comments', methods=['GET'])
def get_comment():
    comments = get_comments()
    return comments


@app.post("/rate")
def post_rating():
    return rate_books()


@app.post("/comment")
def post_comment():
    return comment()


@app.route('/average_rating', methods=['GET'])
def avg_rating():
    avg_rate = get_average_rating()
    return avg_rate


if __name__ == '__main__':
    app.run(debug=True)