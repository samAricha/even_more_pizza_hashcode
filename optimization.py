class Optimization():
    pizzaIndexes = []
    ingridientsList = []
    def __init__(self, availablePizzas, teamsize):
        self.availablePizzas = availablePizzas
        self.teamSize = teamsize
        

    def optimize(self):
        list1= self.availablePizzas[0].pizzaIngridents
        self.pizzaIndexes.append(self.availablePizzas[0].pizzaId)
        

        

        #finding the index with the least number of intersections
        #min = self.leastIntersectingList(dFinal)
        bList = list(set(list1 + self.availablePizzas.pizzaIngridents[min]))
        self.pizzaIndexes.append(self.availablePizzas.pizzaIngridents[min])        
        print("intersection")
        return self.pizzaIndexes 

    def leastIntersectingList(self, dFinal):
        print("in sorting")
        min_value = min(dFinal)
        print(min_value)
        return min_value

    def intersection(self, list1):
        dFinal = {}
        for i in range(1, len(self.availablePizzas)):
            list2 = self.availablePizzas[i].pizzaIngridents
            intersection=[i for i in list1 if i in list2] 
            intersectionLen = len(intersection)
            pizzaId = self.availablePizzas[i].pizzaId
            d = {pizzaId:intersectionLen}
            dFinal.update(d)


optimization = Optimization()
optimization.optimize()