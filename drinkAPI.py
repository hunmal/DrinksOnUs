#ingkey = "https://www.thecocktaildb.com/api/json/v2/9973533/filter.php?i="
import urllib.request, json

class APIQuery():

    def __init__(self):
        self.key = "https://www.thecocktaildb.com/api/json/v2/9973533/"
        self.ingKey = self.key + "filter.php?i="
    
    def searchByIngredients(self, xs):
        masterSearch = self.ingKey + ",".join(xs)
        print()
        print()
        print(masterSearch)
        
        #jsonURL = urllib.request.urlopen(masterSearch)
        #data = json.read(jsonURL.read().decode())

        # with urllib.request.urlopen(masterSearch) as url:
        #     data = json.read(url.read().decode())
        #     print(data)
    

q = APIQuery()
q.searchByIngredients(['Gin', 'Vodka'])

    






