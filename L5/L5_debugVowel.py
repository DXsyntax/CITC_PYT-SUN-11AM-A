# https://replit.com/@CelesteAng1/Remove-Vowels-debug#main.py

word = input('Enter word: ')
result = ""

vowels = ["a", "e", "i", "o", "u"]
for char in word:
    if char in vowels:
        result = result + '*' 
    else:
        result = result + char 
print("Result:", result)

# TOTAL: 6 bugs

# if char in vowels:

# vowels = ["a", "e", "i", "o", "u"]


# word = input('Enter word: ')

# result = ""

# result = char + result

# result = '*' + result

# EXAMPLE OF OUTPUT
# igloo

# WHAT WE WANT
# **lg*

# WHAT WE HAVE NOW
# *gl**


# PSEUDO CODE FOR REFERENCE

# PROGRAM: REMOVE VOWEL

# #1
# input a word

# #2
# create a list to hold vowels
# A E I O U

# #3
# remove vowels

# !hint: use a condition to check if letter is a vowel

# #4
# look for the vowels, using a for loop

# #5
# replace vowels with *

# #6
# print new word without vowels that are replaced with *