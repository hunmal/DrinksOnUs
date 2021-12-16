from urllib import urlopen
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
        self.ingKey = self.key + "filter.php?i="    # Filter by alc ingredients
        self.naKey = self.key + "filter.php?a=Non_Alcoholic"    # Filter by non-alc 
        self.lingKey = self.key + "lookup.php?i="     # look up receipe for drink by ID
        self.nonAlc = json.load(open("nonalc.json", "r"))
    
    def searchWorker(self, q):
        # q is an API call
        url = q
        response = urlopen(url) # open URL (API call)
        qResponse = json.load(response) # Read JSON response to call and load 
        return qResponse

    # Only constraints are ingredients
    def searchByIngredients(self, xs):
        """
            Takes list of ingredients
            Only constraints are ingredients
            Returns a tuple of a list of dictionaries where each dictionary is full drink profile and number of
                ingredients in the drink
        """
        # ingSearch is multiple ingredient search API endpoint concat with list of ingredients xs
        ingSearch = self.ingKey + ",".join(xs)
        workerRes = self.searchWorker(ingSearch)
        print("\nWaiting for searchWorker")
        if (workerRes['drinks'] == 'None Found'):
            return ('None Found')
        resDrinkIds = [x["idDrink"] for x in workerRes["drinks"]]   # Get ids of all drinks returned
        # lookup by id drinks to get their full profile
        drinksAndInstr = [self.searchWorker(self.lingKey + x)["drinks"][0] for x in resDrinkIds]
        ingCount = self.ingFinder(drinksAndInstr) # find number of ingredients for each drink
        
        return (drinksAndInstr, ingCount)

    def nonAlcSearchByIngredients(self, xs):
        ingCount = self.ingFinder(self.nonAlc) # get number if ingredients for each drink
        print(xs)
        xs = set(xs)
        dcount = 0
        drinkList = []
        closeDrinkList = []
        for drink in self.nonAlc: # for each drink
            passableCheck = 0
            for i in range(1, ingCount[dcount]): # for each ingredient
                if drink["strIngredient" + str(i)] in xs: # if ingredient is in drinks ingredients, add to passibleCheck
                    passableCheck += 1
            if passableCheck != 0: # if at least 1 matching ingredient, append drink to return list
                drinkList.append(drink)

            dcount += 1
        return ( (drinkList, self.ingFinder(drinkList)) )
    
    def ingFinder(self, drinks):
        ingCounter = []
        for d in drinks:
            ingCount = 1
            while ingCount < 16:
                if d["strIngredient" + str(ingCount)] == None:
                    break
                ingCount += 1
            ingCounter.append(ingCount)
        return ingCounter

    # Not in active use, used once to get all non alc data
    # def scrapeNonAlc(self):
    #     ingSearch = self.naKey
    #     print("\n")
    #     print(ingSearch)
    #     workerRes = self.searchWorker(ingSearch)

    #     resDrinkIds = [x["idDrink"] for x in workerRes["drinks"]]   # Get ids of all drinks returned
    #     # lookup by id drinks to get their full profile
    #     drinksAndInstr = [self.searchWorker(self.lingKey + x)["drinks"][0] for x in resDrinkIds]

    #     outfile = open('nonalc.json', 'w')
    #     json.dump(drinksAndInstr, outfile)
             

# q = APIQuery()
# #q.nonAlcSearchByIngredients([1,2])
# q.nonAlcSearchByIngredients(['Lime'])

    






