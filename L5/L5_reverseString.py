#1
# input a word to reverse
user_input_word = input("enter a word: ")

# 
result = ""


#2
# reverse input
for char in user_input_word: 
  result = char + result 
  # result = result + char 
  # add the new letters in the front
  # instead of going back

#3
# print the reverse input   
print(result)



# EASTER EGGS:
# -use a for loop
# -use reassignment


# (BRIEFLY)
# for loop syntax

# for i in variable:
#    print(i)

# PYTHON TUTOR TOOL FOR VISUALIZING LOGIC IN CODES
# https://pythontutor.com/visualize.html#mode=display