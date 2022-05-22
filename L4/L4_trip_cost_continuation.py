from cost import *
# * everything 

def flight_cost(city):
  if city == "tokyo":
    return 818
  elif city == "kuala lumpur":
    return 245
  elif city == "bangkok": 
    return 359
  elif city == "taipei":
    return 657

def hotel_cost(city, days):
  cost = 0
  if city == "tokyo": 
    cost = 192 * float(days)
  elif city == "kuala lumpur": 
    cost = 72 * float(days) 
  elif city == "bangkok":
    cost = 88 * float(days) 
  elif city == "taipei":
    cost = 90 * float(days)  
  return print(cost)


def trip_cost():
  destination_input = input("what is your destination: ")
  

  valid_cities = ["tokyo", "kuala lumpur", "bangkok", "taipei"]

  while destination_input not in valid_cities:
    destination_input = input("what is your destination")

  days_input = input("how many days")

  

  total_cost = flight_cost(destination_input) + hotel_cost(destination_input ,days_input)
# define fight cost function

# define hotel cost function

print(trip_cost())
