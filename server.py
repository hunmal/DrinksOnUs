from flask import Flask, render_template, request, Response
from flask.helpers import make_response
from werkzeug.wrappers import response
from APIQuery import APIQuery
import json
import os

app = Flask(__name__)
#app.static_folder='DrinksOnUs/static'
static_folder_root = os.path.join(os.path.dirname(os.path.abspath(__file__)))
# app.register_routes_to_resources(static_folder_root)

@app.route('/')
def hello():
    return render_template("/index.html")

@app.route('/mocktail/')
def mocktail():
    return render_template("/mocktail.html")

@app.route('/mocktail/search',methods=['POST'])
def mocktailSearch():
    data = list(dict(request.form).keys())
    q = APIQuery()
    results = q.nonAlcSearchByIngredients(data)
    #render_template("/mocktail.html")
    response  = make_response(render_template("/mocktail.html", results=results))
    return response
    return str(results)

@app.route('/cocktail/')
def cocktail():
    return render_template("/cocktail.html")
    

@app.route('/cocktail/search/')
def cocktailSearch():
    data = list(dict(request.form).keys())#['subSearchMock']
    q = APIQuery()
    results = q.searchByIngredients(data)
    response  = make_response(render_template("/cocktail.html", results=results))
    return response
    
