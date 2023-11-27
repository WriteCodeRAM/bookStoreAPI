from flask import jsonify, request
from database import app, get_db

users = {}


@app.route('/users', methods=['GET'])
def get_users():
    try:
        connection = get_db()

        cursor = connection.cursor()

        query = "SELECT * FROM users"
        cursor.execute(query)

        data = cursor.fetchall()

        cursor.close()
        connection.close()

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


@app.route('/users/update/<username>', methods=["PUT", "PATCH"])
def update_user(username):
    try:
        user_data = request.get_json()
        if not user_data:
            return jsonify({'error': 'No data provided'})

        password = user_data.get("password")
        first_name = user_data.get("first name")
        last_name = user_data.get("last name")

        if not password and not first_name and not last_name:
            return jsonify({'error': 'No fields provided for update'})

        connection = get_db()
        cursor = connection.cursor()

        update_fields = []
        if password:
            update_fields.append(f"password = '{password}'")
        if first_name:
            update_fields.append(f"first_name = '{first_name}'")
        if last_name:
            update_fields.append(f"last_name = '{last_name}'")

        set_query = ", ".join(update_fields)
        query = f"UPDATE users SET {set_query} WHERE username = '{username}'"
        cursor.execute(query)
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"message": "User updated successfully"})

    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/users/<username>/creditcard/new', methods=["POST"])
def add_credit_card(username):
    try:
        user_data = request.get_json()

        credit_card_number = user_data.get("credit_card_number")
        expiration_date = user_data.get("expiration_date")
        cvv = user_data.get("cvv")

        if not (credit_card_number and expiration_date and cvv):
            return jsonify({'error': 'Incomplete credit card details provided'})

        connection = get_db()
        cursor = connection.cursor()

        cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
        user_id = cursor.fetchone()

        if user_id:
            query = "INSERT INTO credit_cards (user_id, credit_card_number, expiration_date, cvv) VALUES (%s, %s, %s, %s)"
            values = (user_id[0], credit_card_number, expiration_date, cvv)
            cursor.execute(query, values)
            connection.commit()

            cursor.close()
            connection.close()

            return jsonify({"message": "Credit card added successfully for the user"})

        else:
            return jsonify({"error": "User not found"})

    except Exception as e:
        return jsonify({'error': str(e)})

