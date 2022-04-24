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
  