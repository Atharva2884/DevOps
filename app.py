from flask import Flask, render_template, request, redirect, flash, url_for
import sqlite3
import csv

app = Flask(__name__)
app.secret_key = 'secret123'

# Initialize the SQLite Database and create the feedback table if not exists
def init_db():
    conn = sqlite3.connect('feedback.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS feedback (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT,
                        course TEXT,
                        instructor TEXT,
                        rating INTEGER,
                        comments TEXT
                    )''')
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = (
        request.form['name'],
        request.form['email'],
        request.form['course'],
        request.form['instructor'],
        request.form['rating'],
        request.form['comments']
    )
    conn = sqlite3.connect('feedback.db')
    conn.execute("INSERT INTO feedback (name, email, course, instructor, rating, comments) VALUES (?, ?, ?, ?, ?, ?)", data)
    conn.commit()
    conn.close()
    flash('Thank you for your feedback!')
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    feedbacks = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', feedbacks=feedbacks)

@app.route('/export')
def export():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    rows = cursor.fetchall()
    with open('feedback_export.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Name', 'Email', 'Course', 'Instructor', 'Rating', 'Comments'])
        writer.writerows(rows)
    flash('Data exported to feedback_export.csv')
    return redirect('/dashboard')

# Route to delete a specific feedback entry by ID
@app.route('/delete/<int:feedback_id>', methods=['GET'])
def delete_feedback(feedback_id):
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM feedback WHERE id=?", (feedback_id,))
    conn.commit()
    conn.close()
    flash('Feedback deleted successfully!')
    return redirect('/dashboard')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)