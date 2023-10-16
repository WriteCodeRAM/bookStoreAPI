from flask import jsonify, request
import mysql.connector

from database import app, get_db

users = {}


@app.route('/users', methods=['GET'])
def get_users():
    try:
        # connect to the database
        connection = get_db()

        # cursor to interact with the database
        cursor = connection.cursor()

        # Sprint 2 example GET request
        query = "SELECT * FROM users"
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
                'user_id': row[0],
                'username': row[1],
                'password': row[2],
                'first name': row[3],
                'last name': row[4],
                'email': row[5]

            })

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    try:
        total_users = get_users().json
        for user in total_users:
            if username == user["username"]:
                return jsonify(user)
        return jsonify({"error": "User not found"})

    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/users/create', methods=["POST"])
def create_user():
    try:
        user_data = request.get_json()
        username = user_data["username"]
        password = user_data["password"]
        first_name = user_data["first name"]
        last_name = user_data["last name"]
        email = user_data["email"]

        connection = get_db()
        cursor = connection.cursor()

        query = "INSERT INTO users (username, password, first_name, last_name, email) VALUES (%s, %s, %s, %s, %s)"
        values = (username, password, first_name, last_name, email)
        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"message": "User created successfully"})

    except Exception as e:
        return jsonify({'error': str(e)})
