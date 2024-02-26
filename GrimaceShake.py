print("\n*****************************************************\n")

print("Weather Branch\n")

#Import libraries here
import random
from time import sleep

#Create a function that randomly chooses the weather from a list
def weather():
    weatherForecast = ["snowy", "blizzarding", "rainy", "foggy", "windy", "icy", "sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

#Variab;e to call the weathe() once VRS(Vehicle Response System) is determined
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 50 MPH.")
    elif weatherAlert == "blizzarding":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 40 MPH.")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 60 MPH.")


vehicleResponseSystem()


