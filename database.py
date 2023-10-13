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
