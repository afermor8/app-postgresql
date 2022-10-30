from flask import Flask, flash, redirect, request, session, render_template, abort
import os
import psycopg2

app = Flask (__name__)

def con_db():
    conn = None
    peli = None
    actor = None
    tabla = None

    try:
        conn = psycopg2.connect(host="localhost", dbname="maravilla", user="admin", password="admin")
    except Exception as e:
        print("No puedo conectar a la base de datos:",e)
#    finally:
#        cursor.close()
#        conn.close()

#conn = psycopg2.connect(
#    host="localhost",
#    database="maravilla",
#    user=os.environ['admin'],
#    password=os.environ['admin'])


def marvels():
    peli = conn.peli()
    peli.execute("select * from pelicula;")
    peliculas = peli.fetchall()
    tabla = conn.tabla()
    tablas=tabla.execute("\dt")
    actor = conn.actor()
    actor.execute("select * from actor;")
    actors=actor.fetchall()
    return render_template("maravilla.html", tablas=tablas, peliculas=peliculas, actors=actors)


@app.route('/',methods=["GET","POST"])
def index():
    if not session.get("logged_in"):
        return render_template("index.html")
    else:
        return marvels()

@app.route('/login', methods=['GET', 'POST'])
def login_required():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
    return index()

if __name__ == "__main__":
#    app.secret_key = os.urandom(12)

    app.run('0.0.0.0' ,debug=False)
