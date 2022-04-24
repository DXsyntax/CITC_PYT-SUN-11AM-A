
# BMI CALCULATOR

weight = input("Enter weight in KGs")
height = input("Enter Height in Ms") 

weight = float(weight)
height = float(height)

bmi = weight / (height * height) 
#remember usage of Int, Float datatypes

print("your bmi is", bmi ) 

if bmi >= 27:
  print("High health risk")
elif bmi >= 23:
  print("Moderate health risk")
elif bmi >= 18.5:
  print("healthy BMI range")
elif bmi < 18.5:
  print("nutritional deficiency")






# // change to elif afterwards 
# // bug is because there will be multiple outputs 
# // rearrange statements too 






# BMI CALCULATOR, PSEUDOCODE 
# ask for weight
# ask for height

# calculate bmi

# depending on BMI, go to appropriate range

# print BMI for user
# show user which range of BMI he/she belongs to

# inform user what health risk do they have with their current BMI



