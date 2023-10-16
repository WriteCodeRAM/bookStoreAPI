from flask import jsonify, request
from database import app, get_db

wishlist = {}


@app.route('/wishlist', methods = ['GET'])
def get_wishlist():
    connection = get_db
    cursor = connection.cursor()

    query = "SELECT * FROM wishlist"
    cursor.execute(query)



