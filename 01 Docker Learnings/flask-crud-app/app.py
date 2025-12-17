from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD']
            )
    return conn

@app.route('/users', methods=['GET', 'POST'])
def users():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.json['name']
        cursor.execute("""INSERT INTO users
                       (name) VALUES (%s);""", (name,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"status": "User Added Successfully"}), 201
    
    cursor.execute("SELECT * From users;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
