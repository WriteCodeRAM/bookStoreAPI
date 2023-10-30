from flask import jsonify, request
from database import app, get_db


@app.route('/comments', methods=['GET'])
def get_comments():
    try:
        connection = get_db()
        cursor = connection.cursor()

        query = "SELECT * FROM comments"
        cursor.execute(query)

        data = cursor.fetchall()
        cursor.close()
        connection.close()

        result = []
        for row in data:
            result.append({
                'user_id': row[0],
                'book_id': row[1],
                'comment_text': row[2],
            })

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/comment', methods=['POST'])
def comment():

    try:

        connection = get_db()
        cursor = connection.cursor()

        data = request.get_json()
        user_id = data["user_id"]
        book_id = data["book_id"]
        comment_text = data["comment_text"]

        print(data)

        # Insert comment into the database
        query = """INSERT INTO comments (user_id, book_id, comment_text) 
        VALUES (%s, %s, %s)"""

        params = (
            user_id,
            book_id,
            comment_text,
        )
        cursor.execute(query, params)
        connection.commit()

        comment_data = {
            "user_id": user_id,
            "book_id": book_id,
            "comment_text": comment_text
        }

        return jsonify(comment_data), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/ratings', methods=['GET'])
def get_ratings():
    try:
        connection = get_db()
        cursor = connection.cursor()

        query = "SELECT * FROM ratings"
        cursor.execute(query)

        data = cursor.fetchall()
        cursor.close()
        connection.close()

        result = []
        for row in data:
            result.append({
                'user_id': row[0],
                'book_id': row[1],
                'rating_val': row[2],
            })

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/rate', methods=['POST'])
def rate_books():

    try:

        connection = get_db()
        cursor = connection.cursor()

        data = request.get_json()
        user_id = data['user_id']
        book_id = data['book_id']
        rating_val = data['rating_val']

        query = """insert into ratings (user_id, book_id, rating_val)
        values (%s, %s, %s)"""

        params = (
            user_id,
            book_id,
            rating_val,
        )

        cursor.execute(query, params)
        connection.commit()

        rating_data = {
            "user_id": data["user_id"],
            "book_id": data["book_id"],
            "rating_val": data["rating_val"],
        }

        return jsonify(rating_data), 201

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/average_rating', methods=['GET'])
def get_average_rating():
    try:

        book_id = request.args.get('book_id')
        book_id = int(book_id)
        if book_id is None:
            return jsonify({"message": "A book ID is required."}), 400

        connection = get_db()
        cursor = connection.cursor()

        # Query to calculate the average rating for the specific book_id
        query = "SELECT AVG(rating_val) FROM ratings WHERE book_id = %s"
        cursor.execute(query, (book_id,))

        average_rating = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        if average_rating is not None:
            return jsonify({"average_rating": average_rating})
        else:
            return jsonify({"message": "Book not found"}), 404

    except Exception as e:
        return jsonify({'error': str(e)})
