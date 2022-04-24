from cost import *
# * everything 


def trip_cost():
  destination_input = input("what is your destination: ")
  

  days_input = input("how many days")

  total_cost = flight_cost(destination_input) + hotel_cost(destination_input ,days_input)
# define fight cost function

# define hotel cost function

print(trip_cost())
