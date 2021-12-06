from urllib.request import urlopen
import json

"""
This is a class APIQuery() that contains functions to be called to various endpoints in the API and return JSON resoponse
TO USE:
    *  Import APIQuery
    *  Make search by ingredient call:
        APIQuery().searchByIngredients(xs) where xs is list of ingredients
        ***     Ingredient are NOT case sensetive
        ***     Multi word ingredients words seperated by underscore
"""

class APIQuery():

    def __init__(self):
        # Key to acess any API endpoint
        self.key = "https://www.thecocktaildb.com/api/json/v2/9973533/"
        # Multiple ingredient API endpoint
        self.ingKey = self.key + "filter.php?i="
    
    def searchWorker(self, q):
        # q is an API call
        url = q
        response = urlopen(url) # open URL (API call)
        qResponse = json.loads(response.read()) # Read JSON response to call and load 
        print(qResponse)
        return qResponse


    def searchByIngredients(self, xs):
        # masterSearch is multipe ingredient search API endpoint concat with list of ingredients xs
        masterSearch = self.ingKey + ",".join(xs)
        print("\n")
        print(masterSearch)
        
        return self.searchWorker(masterSearch)

    

q = APIQuery()
q.searchByIngredients(['Gin', 'Vodka'])

    






