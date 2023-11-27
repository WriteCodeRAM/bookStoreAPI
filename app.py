from flask import Flask
from flask_cors import CORS
from commentsandratings import get_ratings, get_comments, get_average_rating, rate_books, comment
from shoppingcart import get_subtotal, add_to_cart, get_Book_List, remove_book_from_cart

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

if __name__ == '__main__':
    app.run(debug=True)