from flask import Flask, flash, redirect, request, session, render_template, abort
import os
import psycopg2

app = Flask (__name__)

conn = psycopg2.connect(
    host="localhost",
    database="maravilla",
    user=os.environ['admin'],
    password=os.environ['admin'])


def marvels():
   	tablas=db.execute("\dt")
    pelicula=db.execute("select * from pelicula;")
    actor=("select * from actor;")
    return render_template("maravilla.html", tablas=tablas, pelicula=pelicula, actor=actor)


@app.route('/',methods=["GET","POST"])
def index():
    if not session.get("logged_in"):
        return render_template("index.html")
    else:
        return marvels()

@app.route('/login', methods=['POST'])
def login_required():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin': 
        session['logged_in'] = True
    else:
        flash('wrong password!')
        return index()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
app.run('0.0.0.0' ,debug=False)
