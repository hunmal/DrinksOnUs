from flask import Flask, render_template, request, Response
from flask.helpers import make_response
from werkzeug.wrappers import response
from APIQuery import APIQuery
import os

# app is Flask server object
app = Flask(__name__)
# static_folder_root is path to static folder in project directory
static_folder_root = os.path.join(os.path.dirname(os.path.abspath(__file__)))

# When GET request for landing page is made
@app.route('/')
def hello():
    return render_template("/index.html") # Render HTML template index.html as response to GET

# When GET request for mocktail page is made
@app.route('/mocktail/')
def mocktail():
    return render_template("/mocktail.html")

# When POST request for mocktail search is made
@app.route('/mocktail/search',methods=['POST'])
def mocktailSearch():
    data = list(dict(request.form).keys()) # Get data from HTML form
    q = APIQuery() # Init instance of APIQuery object
    results = q.nonAlcSearchByIngredients(data) # Query API through APIQuery member func
    response  = make_response(render_template("/mocktail.html", results=results))
    return response # Make and return a response object to be accessed in HTML

# When GET request for cocktial page is made
@app.route('/cocktail/')
def cocktail():
    return render_template("/cocktail.html")
    
# When POST request for cocktial search is made
@app.route('/cocktail/search/')
def cocktailSearch():
    data = list(dict(request.form).keys()) # Get data from HTML form
    q = APIQuery() # Init instance of APIQuery object
    results = q.searchByIngredients(data) # Query API through APIQuery member func
    response  = make_response(render_template("/cocktail.html", results=results))
    return response # Make and return a response object to be accessed in HTML
    
