from flask import Flask, flash, redirect, request, session, render_template, abort
import os
import psycopg2

app = Flask (__name__)

def get_db_conn():
    conn = None
    peli = None
    actor = None
    tabla = None

    try:
        conn = psycopg2.connect(host="localhost", dbname="maravilla", user="admin", password="admin")
    except Exception as e:
        print("No puedo conectar a la base de datos:",e)

    return conn


def marvels():
    conn = get_db_conn()

    peli = conn.cursor()
    peli.execute("select * from pelicula;")
    peliculas = peli.fetchall()

    tabla_cursor = conn.cursor()
    tabla_cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
    tablas = tabla_cursor.fetchall()

    actor = conn.cursor()
    actor.execute("select * from actor;")
    actors=actor.fetchall()

    return render_template("maravilla.html", tablas=tablas, peliculas=peliculas, actors=actors)


@app.route('/',methods=["GET"])
def index():
    if not session.get("logged_in"):
        return render_template("index.html")
    else:
        return marvels()

@app.route('/login', methods=["POST"])
def login():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
    return redirect("/")

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run('0.0.0.0' ,debug=False)
