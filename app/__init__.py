from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_connection():
    conn = sqlite3.connect('app/database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_connection()
    livros = conn.execute('SELECT * FROM livros').fetchall()
    conn.close()
    return render_template('index.html', livros=livros)

@app.get("/livro/create")
def create_livro():
    return render_template('create_livro.html')
    
@app.post("/livro/store")
def store_livro():
    nome = request.form['nome']
    preco = request.form['preco']
    status = request.form['status']
    
    conn = get_connection()
    cur = conn.cursor()
    query = f"INSERT INTO livros(nome, valor, status_atual) VALUES ('{nome}', {preco}, '{status}') "
    cur.execute(query)
    conn.commit()
    conn.close()
    return redirect("/", code=302)

@app.get("/livro/update/<int:id>")
def update_livro(id):
    conn = get_connection()
    livro = conn.execute(f"SELECT * FROM livros WHERE id = '{id}'").fetchone()
    conn.close()
    livro = list(livro)
    return render_template('update_livro.html', livro=livro)

@app.route("/livro/del/<int:id>")
def delete_livro(id):
    conn = get_connection()
    cur = conn.cursor()
    query = f"DELETE FROM livros WHERE id = '{id}'"
    cur.execute(query)
    conn.commit()
    conn.close()
    return redirect("/", code=302)

