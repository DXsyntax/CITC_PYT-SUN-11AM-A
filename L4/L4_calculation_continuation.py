def calculator():

	def add():
		first_num  = float(input("first number: "))
		second_num = float(input("second number: ") )
		total_sum = first_num + second_num 
		print(total_sum)

	def subtract():
		first_num  = float(input("first number: "))
		second_num = float(input("second number: ") )
		total_subtract = first_num - second_num
		print(total_subtract)

	def multiply():
		first_num = float(input("first number: "))
		second_num = float(input("second number: ") )
		total_multiply = first_num * second_num
		print(total_multiply)
                
	def divide():
		first_num = float(input("first number: "))
		second_num = float(input("second number: ") )
		total_divide = first_num / second_num 
		print(total_divide)  

	while True:
		user_input = input("select operation: (+  -  / *) ")
      
		if user_input == "+":
			add()
		elif user_input == "-":
			subtract() 
		elif user_input == "*":
			multiply()
		elif user_input == "/":
			divide()
		elif user_input == "quit":
			break
		else:
			print("this operation is not recognized, please try the recommended operations")

# while True:
calculator()