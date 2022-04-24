def calculator():
  # def keyword 
  # parenthesis () for every function
  # return must be defined at the end

  # get input from user
  user_input = input("select operation, + - / *")

  # get first number from user
  first_num = input("first input")

  # get second number from user
  second_num = input("second input")

  def add(first, second): 
    return print(float(first) ** 3)

  # check operation provided by user
  if user_input == "+":
    # sum = float(first_num) + float(second_num)
    add(first_num, second_num)
    
  else: 
    print("operation is invalid")

  return print(sum)

calculator()