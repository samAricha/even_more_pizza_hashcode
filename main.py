from posixpath import split
from matplotlib.style import available

from sqlalchemy import null
from optimization import *


#1. sort the ingridients before adding the lists to the ingridients list
#2. when adding a pizza to a list first choose the first pizza and then look for a list 
#   of ingridients that is least similar i.e with least no. of items in the list of similar 
#   ingridients in pizza.
#  - that data is going to be stored in a dictionary(pizzaid & no. of similar ingridients) or list and we are going to choose the one 
#   with the least number of similar elements.
#  - we are then going to remove the ids of the selected pizzas from the list of availablePizzas.

class Program():
    availablePizzas = None#this is a list of the pizzas that are left when others have been delivered.
    def __init__(self):
        pass
        
     
    def readInputFile(self, inputFileName):
        lines = []
        self.ingridientsList = []
        with open(inputFileName) as f:
            lines = f.readlines()

        for i in range(len(lines)):
            line = lines[i]
            splitLine = line.split(' ')

            if(i == 0):
                totalPizzas = splitLine[0]
                t2 = splitLine[1]
                t3 = splitLine[2]
                t4 = splitLine[3]
                print(f"{totalPizzas} {t2} {t3} {t4}")
            elif(i > 0):  
                ingridients = Ingridients(str(i-1), splitLine[0], splitLine[1:])
                self.ingridientsList.append(ingridients)
            
        emp = EvenMorePizza(totalPizzas, t2, t3, t4, self.ingridientsList)
        return emp

    
    def writeOutputFile(self, outputFileName, output):
        outputFileText = str(len(output.deliveries)) + "\n"

        for delivery in output.deliveries:
            outputFileText += str(delivery.teamType) +" " + " ".join(delivery.pizzas) + "\n"
             
        with open(outputFileName, 'w') as wf:
            wf.write(outputFileText)
            #print(delivery.pizzas)

    
    
    #the PIZZAID is equivalent to the position of the pizza in the list
    currentId = 0
    def createDelivery(self, emp, numOfTeams, teamSize):
        pizzaIndexes = []
        
        optimization = Optimization(self.availablePizzas, teamSize)
        pizzaIndexes = optimization.optimize()
        for k in range(teamSize):
            self.currentId += 1
            pizzaIndexes.append(str(self.currentId))

        return Delivery(teamSize, pizzaIndexes)
                
        
    #the return of this method should contain 
    # 1. the no. of teams that have received pizzas 
    # 2. a list of the Deliveries i.e No. of people in the team + the ids of the delivered pizzas
    def pizzaDelivery(self, evenMorePizza):
        output = Output()
        output.deliveredPizzas = 0
        deliveries = []
        
        team2Ppl = int(evenMorePizza.team2Ppl)
        team3Ppl = int(evenMorePizza.team3Ppl)
        team4Ppl = int(evenMorePizza.team4Ppl)
        self.pizzasAvailable = int(evenMorePizza.availablePizzas)

        team2PplSize = 2
        team3PplSize = 3
        team4PplSize = 4

        totalPeople = team2Ppl * 2 + team3Ppl * 3 + team4Ppl * 4

        print("Loops\n\n")

    
        #Required: a loop which will loop through ALWAYS checking if the pizzas are available
        #for loop is not ALWAYS looping through
        #while loop is bringing about errors
   
        while (self.pizzasAvailable > 0):
            #print(f"at the start: {self.pizzasAvailable}")
            if ((team2Ppl > 0) and (self.pizzasAvailable >= 2)):
                
                i = 0
                for i in range(team2PplSize):               
                    i += 1                               
                    self.pizzasAvailable -= 1
                    print(f"in the 2ppl team: {self.pizzasAvailable}")
                delivery = self.createDelivery(evenMorePizza,team2Ppl, team2PplSize)
                deliveries.append(delivery)
                team2Ppl -= 1
                print(f"finally: {self.pizzasAvailable}") 
                if(self.pizzasAvailable >= 3 and (team4Ppl > 0)):
                    continue
                else:
                    print(f"remaining pizzas: {self.pizzasAvailable}")
                    output.deliveries = deliveries
                    
                                                     
            elif ((team3Ppl > 0) and (self.pizzasAvailable >= 3)): 
                print("in team 3 ppl")
                i = 0
                for i in range(team3PplSize):               
                    i += 1                   
                    self.pizzasAvailable -= 1
                    print(f"in the 3ppl team: {self.pizzasAvailable}")
                delivery = self.createDelivery(evenMorePizza,team3Ppl, team3PplSize)
                deliveries.append(delivery)
                team3Ppl -= 1
                if(self.pizzasAvailable >= 3 and (team3Ppl > 0)):
                    continue
                else:
                    print(f"remaining pizzas: {self.pizzasAvailable}")
                    output.deliveries = deliveries
                    
                  
                                              
            elif ((team4Ppl > 0) and (self.pizzasAvailable >= 4)):
                print("in team 4 ppl") 
                i = 0
                for i in range(team4PplSize):               
                    i += 1                                         
                    self.pizzasAvailable -= 1
                delivery = self.createDelivery(evenMorePizza,team4Ppl, team4PplSize)
                deliveries.append(delivery)
                team4Ppl -= 1
                if(self.pizzasAvailable >= 4 and (team4Ppl > 0)):
                    continue
                else:
                    print(f"remaining pizzas: {self.pizzasAvailable}")
                    output.deliveries = deliveries
            
            return output
                
                    
            # print(f"remaining pizzas: {self.pizzasAvailable}")
            # output.deliveries = deliveries
            # return output

          
#classes for the various activities in the program start here

#this is the class that will be printed to the output file i.e teams received pizza and 
#a description of the deliveries see Delivery class
class Output():
    deliveredPizzas = null
    deliveries = []
    def __init__(self):
        pass

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

#this is the file that will contain a description of the deliveries i.e team type and the list of pizzas the 
#team will receive
class Delivery():
    teamType = null
    pizzas = []
    def __init__(self, teamType, pizzas):
        self.teamType = teamType
        self.pizzas = pizzas

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
        

class EvenMorePizza():
    pizzaIngridients = []
    def __init__(self, availablePizzas, team2Ppl, team3Ppl, team4Ppl, pizzaIngridents):
        self.availablePizzas = availablePizzas
        self.team2Ppl = team2Ppl
        self.team3Ppl = team3Ppl
        self.team4Ppl = team4Ppl
        self.pizzaIngridients = pizzaIngridents

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class Ingridients:   
    def __init__(self, pizzaId, numOfIngridients, ingridients):
         self.pizzaId = pizzaId
         self.numOfIngridients = numOfIngridients
         self.ingridents = ingridients
    
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    # getter methods
    def get_pizzaId(self):
        return self.pizzaId
    def get_numOfIngridients(self):
        return self.numOfIngridients
    def get_ingridients(self):
        return self.ingridients    
    # setter methods
    def set_pizzaId(self, x):
        self.pizzaId = x
    def set_numOfIngridients(self, x):
        self.numOfIngridients = x
    def set_ingridients(self, x):
        self.ingridients = x

exampleInputFile = "pizza_input.txt"
littleBitofEverythingFile = "b_little_bit_of_everything.in"
manyIngridientsFile = "c_many_ingredients.in"
manyPizzasFile = "d_many_pizzas.in"
manyTeamsFile = "e_many_teams.in"
program = Program()

emp = program.readInputFile(manyTeamsFile)
output = program.pizzaDelivery(emp)
program.writeOutputFile('output_file.txt', output)

