def password_prompter():
  my_password = 'my_password'
  user_input = input("enter password: ")

  while user_input != my_password:
    user_input = input("enter password: ")

  print("You are logged in")

print(password_prompter())

