from flask import Flask
<<<<<<< HEAD
from flask_cors import CORS
from commentsandratings import get_ratings, get_comments, get_average_rating, rate_books, comment
from shoppingcart import get_subtotal, add_to_cart, get_Book_List, remove_book_from_cart
=======
from commentsandratings import get_ratings, get_comments, get_average_rating
from book_details import get_books_ISBN, create_book, get_books_author
from wishlistmanagement import new_wishlist, add_book, delete_book, list_books
from users import get_users, get_user, create_user, update_user, add_credit_card
>>>>>>> 06c7e0d8b5d81d4a9a54106dd044615b4f0e9960

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

#Subtotal 
@app.route('/shoppingcart/<UserId>', methods=['GET'])
def get_total(UserId):
    return get_subtotal(UserId)
   
#Add Book
@app.route('/shoppingcart/add-book/<BookID>/<UserId>/<Subtotal>', methods=['POST'])
def add_book_to_cart(BookID, UserId, Subtotal):
    return add_to_cart(BookID, UserId, Subtotal)

#Retrieve List
@app.route('/shopping-cart/<UserId>/', methods=['GET'])
def get_books_in_cart(UserId):
  return get_Book_List(UserId)

#Delete Book 
@app.route('/shopping-cart/remove-book/<BookID>/<UserId>', methods=['DELETE'])
def remove_book(BookID, UserId):
    return remove_book_from_cart(BookID, UserId)

<<<<<<< HEAD
if __name__ == '__main__':
    app.run(debug=True)
=======
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
>>>>>>> 06c7e0d8b5d81d4a9a54106dd044615b4f0e9960
