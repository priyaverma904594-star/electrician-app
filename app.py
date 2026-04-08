from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    problem = request.form['problem']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO bookings (name, problem, status) VALUES (?, ?, 'Pending')")
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/worker')
def worker():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bookings")
    data = c.fetchall()
    conn.close()
    return render_template('worker.html', data=data)

@app.route('/accept/<int:id>')
def accept(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("UPDATE bookings SET status='Accepted' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/worker')

@app.route('/complete/<int:id>')
def complete(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("UPDATE bookings SET status='Completed' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/worker')

app.run(debug=True)