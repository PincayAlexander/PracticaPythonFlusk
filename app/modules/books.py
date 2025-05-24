from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.database.db import mysql

bookBp = Blueprint('book', __name__, template_folder='app/templates')

@bookBp.route('/', methods=['GET'])
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM books')
    data = cur.fetchall()
    
    book = None
    id = request.args.get('id')
    if id:
        book = get_by_id(id)
    cur.close()
    return render_template('index.html', libros=data, edit_book=book)

def get_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM books WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    return data[0]

@bookBp.route('/addBook', methods=['POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        publication = request.form['publication']
        rating = request.form['rating']
        status = request.form['status']
        notes = request.form['notes']
        try:
            cur = mysql.connection.cursor()
            cur.execute("""
                        INSERT INTO books (title, author, genre, publication, rating, status, notes)
                        VALUES (%s,%s,%s,%s,%s,%s,%s)
                    """, (title, author, genre, publication, rating, status, notes))
            mysql.connection.commit()
            flash('Libro agregado exitosamente', 'exitoso')
            return redirect(url_for('book.index'))
        except Exception as e:
            flash(f'Error al guardar el libro {e.args[1]}', 'error')
            return redirect(url_for('book.index'))


@bookBp.route('/update/<id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        publication = request.form['publication']
        rating = request.form['rating']
        status = request.form['status']
        notes = request.form['notes']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE books
            SET title = %s,
                author = %s,
                genre = %s,
                publication = %s,
                rating = %s,
                status = %s,
                notes = %s
            WHERE id = %s
        """, (title, author, genre, publication, rating, status, notes, id))
        flash('Libro actualizado exitosamente', 'info')
        mysql.connection.commit()
        return redirect(url_for('book.index'))

@bookBp.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM books WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Libro elimiado exitosamente', 'exitoso')
    return redirect(url_for('book.index'))