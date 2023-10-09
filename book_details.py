from database import get_db
from flask import jsonify


#  GET BOOK BY ISBN
def get_books(ISBN):
    try:
        # connect to the database
        connection = get_db()

        # cursor to interact with the database
        cursor = connection.cursor()

        # Sprint 2 example GET request
        query = f"SELECT * FROM Books WHERE isbn = {ISBN}"
        # execute will run the query above
        cursor.execute(query)

        # get all rows from the result
        data = cursor.fetchall()

        # close the cursor and connection
        cursor.close()
        connection.close()

        print(type(data))

        # turn the data into a list of objects
        results = []

        for row in data:
            # print(row)
            results.append(
                {
                    "Book_ID": row[0],
                    "ISBN": row[1],
                    "Title": row[2],
                    "Description": row[3],
                    "Price": row[4],
                    "Author ID": row[5],
                    "Genre": row[6],
                    "Publisher": row[7],
                    "Year Published": row[8],
                    "Copies Sold": row[9],
                }
            )

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)})


# CREATE A BOOK


# CREATE AN AUTHOR


# GET BOOKS FROM SPECIFIC AUTHOR
