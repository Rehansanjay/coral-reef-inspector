import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", 
        database="coral_db"
    )

def save_prediction(image_path, prediction, confidence, name, country, temperature):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO predictions 
        (image_path, prediction, confidence, name, country, temperature) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (image_path, prediction, confidence, name, country, temperature))
    conn.commit()
    conn.close()