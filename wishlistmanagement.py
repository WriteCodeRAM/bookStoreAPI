from flask import Flask, request, jsonify
from database import get_db

app = Flask(__name__)



@app.route('/wishlist/<int:wishlistId>', methods=['GET'])
def get_wishlist(wishlistId):
    if wishlistId in wishlist_data:
        books_in_wishlist = wishlist_data[wishlistId]
        return jsonify(books_in_wishlist)
    else:
        return jsonify({"error": "Wishlist not found"}), 404

if __name__ == '__main__':
    app.run()


@app.route('/api/wishlist/add_book', methods=['POST'])
def add_book_to_wishlist():
    # Get data from the request
    data = request.get_json()
    book_id = data.get('BookId')
    wishlist_id = data.get('WishlistId')

    # Check if the book_id and wishlist_id are valid
    if book_id is None or wishlist_id is None:
        return jsonify({"error": "Invalid parameters"}), 400

    # Add the book to the wishlist in your data store
    if wishlist_id in wishlist_data:
        wishlist_data[wishlist_id].append(book_id)
    else:
        wishlist_data[wishlist_id] = [book_id]

    return jsonify({"message": "Book added to the wishlist"}), 200

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/wishlist/remove_and_add_to_cart', methods=['DELETE'])
def remove_from_wishlist_and_add_to_cart():
    # Get data from the request
    data = request.get_json()
    book_id = data.get('BookId')
    wishlist_id = data.get('WishlistId')

    # Check if the book_id and wishlist_id are valid
    if book_id is None or wishlist_id is None:
        return 'Invalid parameters', 400

    # Remove the book from the wishlist in your data store
    if wishlist_id in wishlist_data and book_id in wishlist_data[wishlist_id]:
        wishlist_data[wishlist_id].remove(book_id)
        # Add the book to the user's shopping cart
        if wishlist_id in shopping_cart_data:
            shopping_cart_data[wishlist_id].append(book_id)
        else:
            shopping_cart_data[wishlist_id] = [book_id]
        return 'Book removed from wishlist and added to shopping cart', 204
    else:
        return 'Book or wishlist not found', 404

if __name__ == '__main__':
    app.run(debug=True)

#list books in wishlist
def list_books_in_wishlist():
    # Get the WishlistId from the request
    wishlist_id = request.args.get('WishlistId')

    # Check if the wishlist_id is valid
    if wishlist_id is None:
        return jsonify({"error": "Invalid parameters"}), 400

    # Retrieve the list of books associated with the specified WishlistId
    if wishlist_id in wishlist_data:
        books_in_wishlist = wishlist_data[wishlist_id]
        return jsonify(books_in_wishlist), 200
    else:
        return jsonify({"error": "Wishlist not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/wishlist/<wishlist_id>', methods=['GET'])
def list_books_in_wishlist(wishlist_id):
    try:
        connection = get_db()

        cursor = connection.cursor()

        query = f"SELECT * FROM wishlist WHERE wishlist_id = {wishlist_id}"

        cursor.execute(query)

        data = cursor.fetchall()

        cursor.close()
        connection.close()

        results = []

        for row in data:
            results.append(
                {
                    "wishlist_id": row[0],
                    "wishlist_name": row[1],
                    "user_id": row[2],
                    "book_id": row[3],
                }
            )

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)

