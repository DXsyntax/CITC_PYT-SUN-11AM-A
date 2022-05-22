# explaining what is infinite looping
# explain what is the bug after demonstrating
# round robin discussion

# # 1, 
# password = ''
# while password != 'my_password':
#   password = input('Enter password: ')
#   print('You are logged in.')
# BUG: variable password is an empty string
# as long as password is not 'my_password'
# it will allow the print statement
#
#
# 2
# password = 'my_password'
# while password != 'my_password':
#   password = input('Enter password: ')
#   print('You are logged in.')
#print('You are logged in.')
# BUG: print statement has no indentation and will our while loop will not consider it as one of it's instructions to run 
#
#
# 4
# # password = input('Enter password: ')
# password = 'my_password'
# while password != 'my_password':
#   password = input('Enter password: ')
#   print('You are logged in.')
# if password is anything other than my_password, it will allow logging in, this condition is allowing a mistake to always be true, which is not what we want 
# change password string to anything else
# e.g password = 'my_sword'
#
#
# 5
# password = 'my_password'
# if password != 'my_password':
#   password = input('Enter password: ')
# else:
#   print('You are logged in.')
# BUG: instead of a while loop we are now demonstrating the SAME bug from #4 that IF password is anything other than my_password, it will allow logging in
# change password string to anything else
# e.g password = 'my_sword'