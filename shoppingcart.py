from flask import jsonify, request
import _mysql_connector

from database import app, get_db

cart_items = {
    "user123": [
        {"book_id": 1, "subtotal": 25.0},
        {"book_id": 2, "subtotal": 30.0},
    ],
    "user456": [
        {"book_id": 3, "subtotal": 15.0},
    ],
}

@app.route('/api/users/<user_id>/cart/subtotal', methods=['GET'])
def get_cart_subtotal(user_id):
    if user_id in cart_items:
        subtotal = sum(item["subtotal"] for item in cart_items[user_id])
        return jsonify({"userId": user_id, "subtotal": subtotal})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/users/<user_id>/cart/add', methods=['POST'])
def add_to_cart(user_id):
    data = request.json
    book_id = data.get("book_id")

    if user_id not in cart_items:
        cart_items[user_id] = []

    # Simulate adding the book to the cart (replace with actual logic)
    cart_items[user_id].append({"book_id": book_id, "subtotal": 0.0})

    return jsonify({"message": "Book added to cart"})

if __name__ == '__main__':
    app.run(debug=True)

    {
    "userId": 123,
    "books": [
        {
            "bookId": 1,
            "title": "Book Title 1",
            "author": "Author 1",
            "price": 19.99
        },
        {
            "bookId": 2,
            "title": "Book Title 2",
            "author": "Author 2",
            "price": 14.99
        },
        {
            "bookId": 3,
            "title": "Book Title 3",
            "author": "Author 3",
            "price": 29.99
        }
    ]
}

def remove_book_from_cart():
    user_id = request.args.get('user_id')
    book_id = request.args.get('book_id')

    if user_id is None or book_id is None:
        return jsonify({"error": "User Id and Book Id are required"}), 400

    if user_id in shopping_cart and book_id in shopping_cart[user_id]:
        shopping_cart[user_id].remove(book_id)
        return "", 204  # No content, book removed successfully
    else:
        return jsonify({"error": "Book not found in user's shopping cart"}), 404

if __name__ == '__main__':
    app.run(debug=True)