import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chanakya@2005",
        database="employee_portal"
    )