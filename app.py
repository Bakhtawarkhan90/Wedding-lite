from flask import Flask, send_from_directory, request, redirect
import mysql.connector
import os

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="database",  # This is the MySQL container name if you're using Docker
    user="root",
    password="kali",
    database="rsvp"
)

@app.route('/')
def index():
    # Serve the index.html directly from the root directory
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    guests = request.form['guests']
    message = request.form['message']

    cursor = db.cursor()
    query = "INSERT INTO invitations (name, email, guests, message) VALUES (%s, %s, %s, %s)"
    values = (name, email, guests, message)
    cursor.execute(query, values)
    db.commit()

    return redirect('/')

# Serve static files like CSS, JS, and images
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.getcwd(), filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
