from functools import total_ordering
from lib2to3.pgen2.token import LESS

from numpy import sort


# TASK :
# create an algorithm that is given a list of lists and prints the total_ordering
# number of similar elements in those and how many times they appear.

# LOGIC .1
# take the first list and compare to second list, create a set from the two, and then add the rest of the 
# lists one after another to the set. In the end count the number of elements in all the lists 
# and subtract it from the total number of elements in the final set and voila!!!

# LOGIC .2
# combine all the lists into one big list and find the repeated elements and how many times they've 
# been repeated

# LOGIC .3
# combine all the lists into one big list and find the repeated elements and how many times they've 
# been repeated



list1 = ["onion", "pepper", "olive"]
list2 = ["mushroom", "tomato", "basil"]
list3 = ["chicken", "mushroom", "pepper"]
list4 = ["tomato", "mushroom", "basil"]
list5 = ["chicken", "basil"]

l=[] 
l.append(list1)
l.append(list2)
l.append(list3)
l.append(list4)
l.append(list5)
print(l[0])


class Optimization():
    pizzaIndexes = []
    ingridientsList = []
    def __init__(self, list, teamsize):
        self.ingridientsList = list
       

    def optimize(self):
        list1= []
        dFinal = {} 

        for i in range(1, len(self.ingridientsList)):
            list1 = self.ingridientsList[0]
            list2 = self.ingridientsList[i]
            intersection=[i for i in list1 if i in list2] 
            intersectionLen = len(intersection)
            pizzaId = i
            d = {pizzaId:intersectionLen}
            dFinal.update(d)
            
        #finding the index with the least number of intersections
        min = self.leastIntersectingList(dFinal)

        bList = list(set(list1 + self.ingridientsList[min]))

        print(dFinal)
        print(bList)
        return self.pizzaIndexes 

    def appendtoEnd(self):
        pass

    def leastIntersectingList(self, dFinal):
        print("in sorting")
        min_value = min(dFinal)
        print(min_value)
        return min_value


optimization = Optimization(l, 2)
optimization.optimize()

# A=[1, 2, 3, 2, 5, 1]
# unique=[i for i in A if A.count(i)==1]
# print(unique)