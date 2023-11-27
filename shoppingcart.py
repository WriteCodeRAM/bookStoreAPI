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
    ]
}

#Retrieve subtotal 
def get_subtotal(UserId):
    try:    

        # connect to the database
        connection = get_db()

        # cursor to interact with the database
        cursor = connection.cursor()

        # Sprint 2 example GET request
        query = f"SELECT * FROM ShoppingCart WHERE UserId = {UserId}"
        # execute will run the query above
        cursor.execute(query)

        # get all rows from the result
        data = cursor.fetchall()

        print(data)

        # close the cursor and connection
        cursor.close()
        connection.close()

        subtotal = sum(float(item[2]) for item in data)

        return jsonify({"subtotal": subtotal})

    except Exception as e:
        return jsonify({"error": str(e)})

    
#add book
def add_to_cart(BookID, UserId, Subtotal):
    try:    
        # connect to the database
        connection = get_db()

        # cursor to interact with the database
        cursor = connection.cursor()

        # Sprint 2 example INSERT request
        query = f"INSERT INTO ShoppingCart (UserId, BookID, Subtotal) VALUES({UserId}, {BookID}, {Subtotal})"
        
        # execute will run the query above
        cursor.execute(query)

        # commit the changes to the database
        connection.commit()

        # close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify({"success": True, "message": "Book added to the cart successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})
        
#Retrieve Book List
def get_Book_List(UserId):
    try:    
        # connect to the database
        connection = get_db()

        # cursor to interact with the database
        cursor = connection.cursor()

        # Sprint 2 example GET request with JOIN
        query = f"""
            SELECT ShoppingCart.BookID, ShoppingCart.UserId, Books.book_name
            FROM ShoppingCart
            JOIN Books ON ShoppingCart.BookID = Books.book_id
            WHERE ShoppingCart.UserId = {UserId}
        """

        # execute will run the query above
        cursor.execute(query)

        # get all rows from the result
        data = cursor.fetchall()

        # close the cursor and connection
        cursor.close()
        connection.close()

        # turn the data into a list of objects
        results = []

        # for row in data:
        #     results.append(
        #         {
        #             "Book_ID": row[0],
        #             "User_ID": row[1],
        #             "Book_Name": row[2],
        #         }
        #     )

        return jsonify(data)
        
    except Exception as e:
        return jsonify({"error": str(e)})

#remove_book
def remove_book_from_cart(Book_ID, UserID):
    try:    
        # connect to the database
        connection = get_db()

        # cursor to interact with the database
        cursor = connection.cursor()

        # Sprint 2 example DELETE request
        query = f"DELETE FROM ShoppingCart WHERE BookID = {Book_ID} AND UserId = {UserID}"
        
        # execute will run the query above
        cursor.execute(query)

        # commit the changes to the database
        connection.commit()

        # close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify({"success": True, "message": "Book removed from the cart successfully"})
    
    except Exception as e:
        return jsonify({"error": str(e)})