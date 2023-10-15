from flask import Flask, jsonify, request
from commentsandratings import get_ratings, get_comments, get_average_rating
from book_details import get_books_ISBN, create_book, get_books_author

app = Flask(__name__)


# get book by ISBN
@app.get("/books/<book_isbn>")
def get_books(book_isbn):
    data = get_books_ISBN(book_isbn)
    return data


# get book by author ID
@app.get("/books/author/<book_author_id>")
def get_books_by_author_id(book_author_id):
    data = get_books_author(book_author_id)
    return data


# create book
@app.post("/create-book")
def new_book():
    return create_book()


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
