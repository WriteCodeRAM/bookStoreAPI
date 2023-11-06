from flask import Flask, request, jsonify

app = Flask(__name__)

wishlist_data = {
    1: ["To Kill A Mockingbird", "The Great Gatsby", "Romeo and Juliet"],
    2: ["Hamlet", "Dracula"],
    # ...
}

@app.route('/wishlist/<int:wishlistId>', methods=['GET'])
def get_wishlist(wishlistId):
    if wishlistId in wishlist_data:
        books_in_wishlist = wishlist_data[wishlistId]
        return jsonify(books_in_wishlist)
    else:
        return jsonify({"error": "Wishlist not found"}), 404

if __name__ == '__main__':
    app.run()



