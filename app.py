from flask import Flask, render_template, \
  request, redirect, url_for
import pymysql.cursors, os

app = Flask(__name__)


# @app.route('/nama')
# def hello_worl():
#     return 'Hello World'

conn = cursor = None

#fungsi koneksi database
def bukaDB():
   global conn, cursor
   conn = pymysql.connect(host='localhost',
        user='root',
        password='',
        db='data_siswa',
        charset='utf8mb4')
   cursor = conn.cursor()	

#fungsi untuk menutup koneksi
def tutupDB():
   global conn, cursor
   cursor.close()
   conn.close()

@app.route('/')
def index():
    bukaDB()
    container = []
    sql = "SELECT * FROM siswa"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        container.append(data)
    tutupDB()
    return render_template('index.html', container=container)

@app.route('/tambah')
def tambah():
    return render_template('tambah.html')




if __name__ == '__main__':
   app.run(debug=True)

