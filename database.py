import mysql.connector

def get_db():
    """إنشاء اتصال بقاعدة البيانات"""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pythone"
    )