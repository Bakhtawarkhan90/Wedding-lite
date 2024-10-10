from flask import Flask, send_from_directory, request, redirect, url_for
import mysql.connector
import os
import time

app = Flask(__name__)

# Retry logic for MySQL connection
while True:
    try:
        db = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "database"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", "kali"),
            database=os.getenv("MYSQL_DB", "rsvp")
        )
        print("Database connection successful")
        break
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        time.sleep(5)

# Create the 'invitations' table if it doesn't exist
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS invitations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    guests INT,
    message TEXT
)
""")
cursor.close()
print("Table 'invitations' checked/created successfully")

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    guests = request.form['guests']
    message = request.form['message']

    try:
        cursor = db.cursor()
        query = "INSERT INTO invitations (name, email, guests, message) VALUES (%s, %s, %s, %s)"
        values = (name, email, guests, message)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return redirect(url_for('thank_you'))

@app.route('/thankyou')
def thank_you():
    return send_from_directory(os.getcwd(), 'thankyou.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.getcwd(), filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
