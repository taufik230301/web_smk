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

@app.route('/tambah', methods=['GET','POST'])
def tambah():
    if request.method == 'POST':
        nama = request.form['nama']
        kelas = request.form['kelas']
        asal_sekolah = request.form['asal_sekolah']
        date = request.form['date']
        alamat = request.form['alamat']
        bukaDB()
        sql = "INSERT INTO siswa (nama, kelas, asal_sekolah, tanggal, alamat) VALUES(%s, %s, %s, %s, %s)"
        val = (nama, kelas, asal_sekolah, date, alamat)
        cursor.execute(sql, val)
        conn.commit()
        tutupDB()
        return redirect(url_for('index'))
    else:
        return render_template('tambah.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    bukaDB()
    if request.method == 'POST':
        nama = request.form['nama']
        kelas = request.form['kelas']
        asal_sekolah = request.form['asal_sekolah']
        date = request.form['date']
        alamat = request.form['alamat']
        no = request.form['no']
        sql = "UPDATE siswa SET nama=%s, kelas=%s, asal_sekolah=%s, tanggal=%s, alamat=%s WHERE no=%s"
        val = (nama, kelas, asal_sekolah, date, alamat, no)
        cursor.execute(sql, val)
        conn.commit()
        tutupDB()
        return redirect(url_for('index'))
    return render_template('index.html')


if __name__ == '__main__':
   app.run(debug=True)

