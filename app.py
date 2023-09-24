from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


db_config = {
    # user is first name lowercase 
    'user': '',
    'password': '',
    'host': 'test-database.cdlfxfopbica.us-east-2.rds.amazonaws.com',
    'database': 'testdb',
    'raise_on_warnings': True
}


# connect to database 
def get_db():
    return mysql.connector.connect(**db_config)


 # Sprint 2 example GET request
@app.get('/store')
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


if __name__ == '__main__':
    app.run(debug=True)
