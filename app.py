from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def get_k_line_data():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM k_line")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/api/k-line-data')
def k_line_data():
    data = get_k_line_data()
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return jsonify({'labels': labels, 'values': values})

if __name__ == '__main__':
    app.run(debug=True)