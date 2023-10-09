from flask import Flask, jsonify, request
from commentsandratings import get_ratings, get_comments, get_average_rating
from book_details import get_books

app = Flask(__name__)


# get book by ISBN
@app.get("/books/<book_isbn>")
def retrieve_books(book_isbn):
    data = get_books(book_isbn)
    return data


@app.route("/ratings", methods=["GET"])
def get_rating():
    ratings = get_ratings()
    return ratings


@app.route("/comments", methods=["GET"])
def get_comment():
    comments = get_comments()
    return comments


@app.route("/average_rating", methods=["GET"])
def avg_rating():
    avg_rate = get_average_rating()
    return avg_rate


if __name__ == "__main__":
    app.run(debug=True)
