from flask import Flask, render_template, abort
import os
import json

app = Flask (__name__)

f = open("books.json")
datos = json.load(f)
f.close()

categorias = set()
for libro in datos:
    categorias.update(libro["categories"])

@app.route('/',methods=["GET","POST"])
def index():
    return render_template("index.html",libros=datos)

@app.route('/libro/<isbn>',methods=["GET","POST"])
def libro(isbn):
    for libro in datos:
        if "isbn" in libro.keys() and isbn == libro["isbn"]:
            return render_template("libro.html", libro=libro)

    abort(404)

@app.route('/categoria/<categoria>',)
def categoria(categoria):
    if categoria not in categorias:
        abort(404)
    return render_template("categoria.html", datos=datos, categoria=categoria)

app.run('0.0.0.0' ,debug=False)
