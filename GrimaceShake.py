# Import Libraries Here
import time
import sys
import random
from time import sleep

# Welcome Branch starts here
timeToSleep = 1

print("\n\n\nWelcome to InfoTech Center Version 1.0\n")
time.sleep(timeToSleep)

# Code to have the ellipsis add a dot every 0.5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center System Loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message)  # \r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")

# Gasoline branch starts here
print("*************************************************************")
print("Gasoline Branch\n\n")

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
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("\n  ***Calling Triple AAA***")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(), "which is",milesToGasStationsLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is a quarter full, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(), "which is",milesToGasStationsLow,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half full, which is plenty to get to your destination.")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(), "which is",milesToGasStationsLow,"miles away.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three-quarters full, which is plenty to get to your destination.")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(), "which is",milesToGasStationsLow,"miles away.")
    elif gasLevelIndicator == "Full Tank":
        print("Your gas tank is FULL !!! YAY !!! YOU'RE NOT POOR AFTER ALL !!!!")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(), "which is",milesToGasStationsLow,"miles away.")


gasLevelAlert()









