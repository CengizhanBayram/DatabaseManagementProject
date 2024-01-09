from flask import Flask, render_template
import psycopg2

app = Flask(__name__)


connection = psycopg2.connect(
    database="netflix",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

@app.route('/')
def index():

    tables = ["Abonelik", "Favori", "Film", "Inceleme", "IzlemeListesi", "Kullanici", "Oyuncu"]
    data = {}

    cursor = connection.cursor()

    for table in tables:
        query = f"SELECT * FROM public.\"{table}\""
        cursor.execute(query)
        data[table] = cursor.fetchall()

    cursor.close()


    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)