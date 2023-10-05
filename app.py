from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)


db_config = {
    # user is first name lowercase 
    'user': 'jorge',
    'password': 'password',
    'host': 'test-database.cdlfxfopbica.us-east-2.rds.amazonaws.com',
    'database': 'testdb',
    'raise_on_warnings': True
}


# connect to database 
def get_db():
    return mysql.connector.connect(**db_config)


 # Sprint 2 example GET request
@app.get('/books')
def get_books():
    try:
        # connect to the database
        connection = get_db()

        # cursor to interact with the database
        cursor = connection.cursor()

        # Sprint 2 example GET request
        query = "SELECT * FROM books"
        # execute will run the query above
        cursor.execute(query)

        # get all rows from the result
        data = cursor.fetchall()

        # close the cursor and connection
        cursor.close()
        connection.close()

        # turn the data into a list of objects
        result = []
        for row in data:
            result.append({
                'book_id': row[0],
                'title': row[1],
                'author': row[2],
                'publication_year': row[3],

            })

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})


books = {}
ratings = {}
comments = {}


@app.route('/rate', methods=['POST'])
def rate_books():
    data = request.get_json()
    book_id = data['book_id']
    user_id = data['user_id']
    rating = data['rating']
    datestamp = data['datestamp']

    ratings.setdefault(book_id, []).append(
        {'user_id': user_id,
         'rating': rating,
         'datestamp': datestamp})
    return jsonify({"message": "Rating added successfully"}), 201


@app.route('/comment', methods=['POST'])
def comment_books():
    data = request.get_json()
    book_id = data['book_id']
    user_id = data['user_id']
    comment = data['comment']
    datestamp = data['datestamp']

    comments.setdefault(book_id, []).append(
        {'user_id': user_id,
         'comment': comment,
         'datestamp': datestamp})
    return jsonify({"message": "Comment added successfully"}), 201


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
                'rating_id': row[0],
                'user_id': row[1],
                'book_id': row[2],
                'rating_value': row[3],
                'timestamp': row[4],
            })

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})


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
                'comment_id': row[0],
                'user_id': row[1],
                'book_id': row[2],
                'comment_text': row[3],
                'timestamp': row[4],
            })

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/average_rating/<book_id>', methods=['GET'])
def get_average_rating(book_id):
    try:
        connection = get_db()
        cursor = connection.cursor()

        # Query to calculate the average rating for the specific book_id
        query = "SELECT AVG(rating_value) FROM ratings"
        cursor.execute(query)

        average_rating = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        if average_rating is not None:
            return jsonify({"average_rating": average_rating})
        else:
            return jsonify({"message": "Book not found"}), 404

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
