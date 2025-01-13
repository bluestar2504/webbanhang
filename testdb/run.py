from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def search_employee(keyword):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='company',
            user='root',
            password='root'
        )
        cursor = connection.cursor()
        query = "SELECT * FROM employee WHERE first_name LIKE %s OR last_name LIKE %s"
        cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
        results = cursor.fetchall()
        for x in results:
         print(x)
        return results
        print("success")
    except Exception as e:
        print("Error:", e)
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        keyword = request.form['keyword']
        results = search_employee(keyword)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

