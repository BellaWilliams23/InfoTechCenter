print("*************************************************************")
print("Gasoline Branch\n\n")

# Import Libraries Here
import random

#Function that lists Gas Levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists Gas Stations, randomly choosing one and returning its value
def listOfGasStations():
    gasStation = ["Shell", "Marathon", "Circle K", "Mobile", "Costco", "Meijer", "7Eleven"]
    gasStationsNearby = random.choice(gasStation)
    return gasStationsNearby

#Fuction will call the gasLevelGauge to determine our gas level then find a close gas station
#by calling the list of gas stations function if we are on low or quarter tank
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1,50),1)
    #gasLevelGauge = gasLevelGauge()
    print(milesToGasStationsLow)
    print(milesToGasStationsQuarterTank)

gasLevelAlert()








