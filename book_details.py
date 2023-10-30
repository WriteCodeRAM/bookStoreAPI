from database import get_db
from flask import jsonify, request


# GET BOOK BY ISBN
def get_books_ISBN(ISBN):
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


# GET BOOKS FROM SPECIFIC AUTHOR ID
def get_books_author(author_id):
    try:
        connection = get_db()

        cursor = connection.cursor()

        query = f"SELECT * FROM Books WHERE author_id = {author_id}"

        cursor.execute(query)

        data = cursor.fetchall()

        cursor.close()
        connection.close()

        results = []

        for row in data:
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
def create_book():
    try:
        # connect to the database
        connection = get_db()

        # cursor to interact with the database
        cursor = connection.cursor()

        data = request.json

        title = data["title"]
        publisher = data["publisher"]
        copies_sold = data["copies_sold"]
        genre = data["genre"]
        author_id = data["author_id"]
        price = data["price"]
        isbn = data["isbn"]
        year_published = data["year_published"]
        description = data["description"]

        query = """
            INSERT INTO Books 
            (isbn, book_name, description, price, author_id, genre, publisher, year_published, copies_sold) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

        params = (
            isbn,
            title,
            description,
            price,
            author_id,
            genre,
            publisher,
            year_published,
            copies_sold,
        )

        cursor.execute(query, params)

        connection.commit()

        book = {
            "title": data["title"],
            "publisher": data["publisher"],
            "copies_sold": data["copies_sold"],
            "genre": data["genre"],
            "price": data["price"],
            "author_id": data["author_id"],
            "isbn": data["isbn"],
            "year_published": data["year_published"],
            "description": data["description"],
        }

        return jsonify(book), 201

    except Exception as e:
        return jsonify({"error": str(e)})


# CREATE AN AUTHOR
def create_author():
    try:
        # connect to the database
        connection = get_db()

        # cursor to interact with the database
        cursor = connection.cursor()

        data = request.json

        first_name = data["first_name"]
        last_name = data["last_name"]
        biography = data["biography"]
        publisher = data["publisher"]

        query = """
            INSERT INTO Authors 
            (first_name, last_name, biography, publisher) 
            VALUES (%s, %s, %s, %s)
            """

        params = (first_name, last_name, biography, publisher)

        cursor.execute(query, params)

        connection.commit()

        author = {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "biography": data["biography"],
            "publisher": data["publisher"],
        }

        return jsonify(author), 201

    except Exception as e:
        return jsonify({"error": str(e)})
