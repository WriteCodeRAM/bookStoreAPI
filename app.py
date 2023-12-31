from flask import Flask
from commentsandratings import get_ratings, get_comments, get_average_rating
from book_details import get_books_ISBN, create_book, get_books_author
from wishlistmanagement import new_wishlist, add_book, delete_book, list_books
from users import get_users, get_user, create_user, update_user, add_credit_card

app = Flask(__name__)


@app.get("/books/<book_isbn>")
def get_books(book_isbn):
    data = get_books_ISBN(book_isbn)
    return data


@app.get("/books/author/<book_author_id>")
def get_books_by_author_id(book_author_id):
    data = get_books_author(book_author_id)
    return data


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


@app.route('/wishlist/<user_id>/<wishlist_name>/<book_id>', methods=['POST'])
def create_wishlist(user_id, wishlist_name, book_id):
    return new_wishlist(user_id, wishlist_name, book_id)

@app.route('/add_wishlist/<user_id>/<wishlist_name>/<book_id>', methods=['POST'])
def add_books(user_id, wishlist_name, book_id):
    return add_book(user_id, wishlist_name, book_id)

@app.route('/wishlist/<wishlist_name>/<book_id>', methods=['DELETE'])
def delete_books(wishlist_name, book_id):
    return delete_book(wishlist_name, book_id)
@app.route('/wishlist/<book_id>', methods=['GET'])
def list_bookss(book_id):
    return list_books(book_id)

if __name__ == "main":
    app.run(debug=True)
