from flask import Flask, jsonify, request
from database import get_db

def new_wishlist(user_id, wishlist_name, book_id):
    try:
        connection = get_db()

        cursor = connection.cursor()

        query = f"""INSERT INTO wishlist VALUES (NULL, {user_id}, '{wishlist_name}', {book_id})"""

        cursor.execute(query)

        connection.commit()

        cursor.close()

        connection.close()

        return jsonify({"message": "Wishlist created successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})

def add_book(user_id, wishlist_name,book_id):
    try:
        connection = get_db()

        cursor = connection.cursor()

        query = f"""INSERT INTO wishlist VALUES (NULL, {user_id}, '{wishlist_name}', {book_id})"""

        cursor.execute(query)

        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"message": "Books added successfully"})

    except Exception as e:
            return jsonify({"error": str(e)})
def delete_book(wishlist_name, book_id):
    try:
        connection = get_db()

        cursor = connection.cursor()

        query = f"DELETE FROM wishlist WHERE book_id = {book_id} AND wishlist_name = '{wishlist_name}'"

        cursor.execute(query)

        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"message": "Books deleted successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})

def list_books(book_id):
    try:
        connection = get_db()

        cursor = connection.cursor()

        query = f"SELECT * FROM wishlist WHERE book_id = {book_id}"

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

