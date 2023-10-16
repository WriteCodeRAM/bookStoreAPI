
from flask import Flask
from flask_cors import CORS
from commentsandratings import get_ratings, get_comments, get_average_rating, rate_books, comment

app = Flask(__name__)
CORS(app)


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


if __name__ == "__main__":
    app.run(debug=True)
